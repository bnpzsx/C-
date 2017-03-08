import LinkedList

class item:
    key=None
    value=None
    
    def __init__(self,key,value):
        self.key=key
        self.value=value
        print("create hash ",key,value)
        
    def __def__(self):
        print("del hash ",self.key,self.value)
        del self.key
        del self.value
        
class HashTable:
    table=[LinkedList.linklist()]*7 #创建Hash表
    def __init__(self):
        print("建立Hash表")

    def set(self,key,value):
        i=hash(key)% 7  #计算位置
        d=self.table[i].find(key) #通过查找key判断是否存在
        if d==None :
            self.table[i].append(key,item(key,value))
        else:
            d.next.data=value #每个item正好存在key的后面
        
    def get(self,key):
        i=hash(key)% 7  
        d=self.table[i].find(key)
        if d==None :
            return False
        else:
            return d.next.data.value  #感觉直接把value存在data里就好了

    def hdel(self,key):
        i=hash(key)% 7  
        d=self.table[i].find(key)
        if d==None :
            return False
        else:
            self.table[i].remove(d.next.data) #效率低了
            self.table[i].remove(d.data)
            return True
    
