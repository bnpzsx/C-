import socket2
import Hash_table

class hashpool():
    
    base=Hash_table.HashTable(10007)
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
hbase=hashpool()
user=newhash(100)
user.set("admin",("admin"))
user.set("root",("admin"))
user.set("bnpzsx",("root"))

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
            result=respond(i,who,"multi")
            s+=result+'\n'
            if result=="False" or result=="Illegal Input":
                back=back[::-1] #倒序
                print(back)
                for i in back:
                    respond(i,who,"back")
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
    
def respond(string,who=None,sta=None):
    '根据命令操作数据库'
    
    which=user.get(who)
    #print(string,",",who,",",which)
    if which==False or which==["wait"]:
        g=user.get(string)
        if g==False:
            return "wrong username"+'\n'+"username:"
        else:
            which=[]
            which.append("pass")
            which.append(g) # hash(password)，问题在这
            which.append(string) # which[2]
            user.set(who,which) # 列表似乎不是引用
            return "password:"
    elif which[0]=="pass":
        if which[1]==string: #验证密码
            which[0]="succeed"
            who=which[2]
            user.set(who,which)
            #print("success",hash(string),which[1])
            return "login successfully!"
        else:
            return "wrong password"+'\n'+"password:"
    elif which[0]=="succeed":
        who=which[2]
    else:
        return "False"
    global work
    global back
    if work!=[]:
        return 事务处理(string,who)
    c=str.split(string," ")
    lens=len(c)
    if lens>=2 and c[0][0]=='h':c[1]=who+'_'+c[1] # 加上区分用户的标志
    r=None
    if c[0]=="multi" and lens==1:
        r="OK"
        work.append("start")
        
    elif c[0]=="set" and lens==3:
        if sta=="multi":
            x=hbase.get(who,c[1])
            if x!=False:
                back.append("set "+c[1]+" "+x)
            else:
                back.append("delete "+c[1])
        
        r=hbase.set(who,c[1],c[2])
    elif c[0]=="get" and lens==2:
        r=hbase.get(who,c[1])
        if r==False:
            r="None"
    elif c[0]=="delete" and lens==2:
        if sta=="multi":
            x=bhase.get(who,c[1])
            if x!=False:
                back.append("set "+who+" "+c[1]+" "+x)
            else:
                pass # 删除None没影响，甚至会直接back
                
        r=hbase.hdel(who,c[1])
    elif c[0]=="hset" and lens==4:
        if sta=="multi":
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
        who[0].send(str.encode(respond(string,str(who[1]))))

    def acpt(self,who):
        who[0].send(b"Connect Success\nusernamme:")
        
s=server()
s.load()
from time import sleep
while 1:sleep(0.1)
