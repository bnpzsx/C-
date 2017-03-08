import LinkedList

def hash(key):
    prime=10007
    if type(key)==int:
        return key
    elif type(key)==str:
        x=id(key)
        for i in key:
            #print(x)
            x=(prime*x)^id(i) 
        x^=len(key)
        return x
    else:
        return id(key)

class HashTable:
    size=40289 #9973 49999 
    table=[]
    def __init__(self,size=324757): #内存与数组大小不成比例
        self.size=size
        self.table=[LinkedList.linklist() for i in range(self.size)] #之前只是建立了n个引用
        print("建立Hash表")

    def set(self,key,value):
        i=hash(key)% self.size  #计算位置
        d=self.table[i].find(key,0) #通过查找key判断是否存在
        if d==None :
            self.table[i].append([key,value]) # 数据以[key,value]的形式存于链表中
        else:
            d.data[1]=value 
        
    def get(self,key):
        i=hash(key)% self.size 
        d=self.table[i].find(key,0)
        if d==None :
            return False
        else:
            return d.data[1]

    def hdel(self,key):
        i=hash(key)% self.size 
        d=self.table[i].find(key,0)
        
        if d==None :
            return False
        else:
            self.table[i].remove(d,True)
            return True
    
    def keys(self):
        r=[] # 之前用字符串复杂了
        for i in self.table:
            if i.root==None:continue
            n=i.root
            while n.next!=None:
                r.append(n.data[0])
                n=n.next
            r.append(n.data[0])
        return r

'''
 #测试代码
import time
a=HashTable()
start = time.time()
for i in range(100000):
    a.set(str(i)+str(i+1)+str(i+3),i)
end = time.time()
print ("总用时",end-start)
'''

