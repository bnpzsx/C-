class table:
    __dic={}
    
    def __init__(self):
        print("字典创建成功")

    def __del__(self):
        print("删除字典")
        
    def set(self,key,value):
        self.__dic[key]=value

    def get(self,key):
        if key in self.__dic:
            return self.__dic[key]
        else:
            return 'None'

    def delete(self,key):
        if key in self.__dic:
            del self.__dic[key]
        else:
            return 'Not Found'

def split(string,fgf):
    '拆分字符串'
    i=0
    s=[]
    while 1: 
        b=i
        i=string.find(fgf,b+1)
        if i!=-1:
            if b==0:
                s.append(string[0:i])
            else:
                s.append(string[b+1:i])
        else:
            if b!=0:
                s.append(string[b+1:])
            else:
                s.append(string)
            break
    return s

test=table()
while(1):
    value=False
    Print=True
    Str=(input(""))
    s=split(Str," ")
        
    #from time import sleep
    #sleep(1)
    if s[0]=="exit":
        del test
        break
    elif s[0]=="set":
        if len(s)==3:
            test.set(s[1],s[2])
            value=True
            print("True")
            Print=False
    elif s[0]=="get":
        if len(s)==2:
            r=test.get(s[1])
            value=True
            print(r)
            Print=False
    elif s[0]=='delete':
        if len(s)==2:
            value=True
            r=test.delete(s[1])
            if r!=None:
                print(r)
                Print=False
    
    if value:
        if Print:
            print(1)
    else:
        print("Illeage Input")
    
