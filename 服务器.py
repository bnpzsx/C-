import socket2
import Hash_table

class hashpool():
    
    base=Hash_table.HashTable()
    #find=lambda key:base.table[Hash_table.hash(key)% base.size].find(key,0) 

    def set(self,w,key,value):
        h=self.base.get(w)
        if h==False:
            print("Create hash",w)
            self.base.set(w,Hash_table.HashTable()) 
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
work=[] #事务表
back=[] #回滚列表

def 事务处理(string,who):
    global work
    global back
    if string=="exec":
        temp=work[1:]
        s=""
        work=[]
        print(temp)
        for i in temp:
            'who.send(str.encode(respond(i),who))'
            result=respond(i,"me")
            s+=result+'\n'
            if result=="False" or result=="Illegal Input":
                back=back[::-1] #倒序
                print(back)
                for i in back:
                    respond(i,"back")
                break
        back=[]    
        if s=="":return "empty routine"
        return s[:-1]
    
    elif string=="reset":
        work=["start"]
        back=[]
        return "True"
    
    else:
        work.append(string)
        return "QUEUED"
    
def respond(string,who=None):
    '根据命令操作数据库'
    global work
    global back
    if work!=[]:
        return 事务处理(string,who)
    c=str.split(string," ")
    lens=len(c)
    r=None
    if c[0]=="multi" and lens==1:
        r="OK"
        work.append("start")
        
    elif c[0]=="set" and lens==3:
        if who=="me":
            x=base.get(c[1])
            if x!=False:
                back.append("set "+c[1]+" "+x)
            else:
                back.append("delete "+c[1])
        
        r=base.set(c[1],c[2])
    elif c[0]=="get" and lens==2:
        r=base.get(c[1])
        if r==False:
            r="None"
    elif c[0]=="delete" and lens==2:
        if who=="me":
            x=base.get(c[1])
            if x!=False:
                back.append("set "+c[1]+" "+x)
            else:
                pass # 删除None没影响，甚至会直接back
                
        r=base.hdel(c[1])
    elif c[0]=="hset" and lens==4:
        if who=="me":
            x=hbase.get(c[1],c[2])
            if x!=False:
                back.append("hset "+c[1]+" "+c[2]+" "+x)
            else:
                back.append("hdelete "+c[1]+" "+c[2])

        r=hbase.set(c[1],c[2],c[3])
    elif c[0]=="hget" and lens==3:
        r=hbase.get(c[1],c[2])
        if r==False:
            r="None"
    elif c[0]=="hdelete" and lens==3:
        if who=="me":
            x=hbase.get(c[1],c[2])
            if x!=False:
                back.append("hset "+c[1]+" "+c[2]+" "+x)
            else:
                pass
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
        who[0].send(str.encode(respond(string,who[0])))
        '''try:who[0].send(str.encode(respond(string,who[0])))
        except:pass'''

    def acpt(self,who):
        who[0].send(b"Connect Success")
        
s=server()
s.load()
from time import sleep
while 1:sleep(0.1)
