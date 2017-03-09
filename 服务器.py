import socket2
import Hash_table

class hashpool():
    
    base=Hash_table.HashTable()
    #find=lambda key:base.table[Hash_table.hash(key)% base.size].find(key,0) 

    def set(self,w,key,value):
        h=self.base.get(w)
        if h==False:
            print("Create hash",w)
            self.base.set(w,Hash_table.HashTable()) #不加self好像指向了全局变量
        h=self.base.get(w)
        if h==False: 
            return False
        else:
            h.set(key,value)
            return True

    def get(self,w,key):
        h=self.base.get(w)
        if h==False:
            return False
        else:
            return h.get(key)
  
    def hdel(self,w,key):
        h=self.base.get(w)
        if h==False:
            return False
        else:
            return h.hdel(key)

    def hkeys(self,w):
        h=self.base.get(w)
        if h==False:
            return False
        else:
            return h.keys()
        
newhash=Hash_table.HashTable
base=newhash()
hbase=hashpool()


def respond(string):
    
    '根据命令操作数据库'
    c=str.split(string," ")
    lens=len(c)
    r=None
    
    if c[0]=="set" and lens==3:
        r=base.set(c[1],c[2])
    elif c[0]=="get" and lens==2:
        r=base.get(c[1])
    elif c[0]=="delete" and lens==2:
        r=base.hdel(c[1])
    elif c[0]=="hset" and lens==4:
        r=hbase.set(c[1],c[2],c[3])
    elif c[0]=="hget" and lens==3:
        r=hbase.get(c[1],c[2])
    elif c[0]=="hdelete" and lens==3:
        r=hbase.hdel(c[1],c[2])
    elif c[0]=="hkeys" and lens==2:
        r=hbase.hkeys(c[1])

    if r==False:
        return "False"
    elif r==None:
        return "Illegal Input"
    else:
        return str(r)

class server(socket2.mysocket):
    def recv(self,who,string):
        print("Server received:",string)
        who[0].send(str.encode(respond(string)))
        
    def acpt(self,who):
        who[0].send(b"Connect Success")
        
s=server()
s.load()
from time import sleep
while 1:sleep(0.1)
