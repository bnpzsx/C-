import LinkedList

class HashTable:
    table=[LinkedList.linklist()]*100 #创建Hash表
    def __init__(self):
        print("建立Hash表")

    def set(self,key,value):
        i=hash(key)% 100  #计算位置
        d=self.table[i].find(key,0) #通过查找key判断是否存在
        if d==None :
            self.table[i].append([key,value]) # 数据以[key,value]的形式存于链表中
        else:
            d.next.data[1]=value 
        
    def get(self,key):
        i=hash(key)% 100  
        d=self.table[i].find(key,0)
        if d==None :
            return False
        else:
            return d.data[1]

    def hdel(self,key):
        i=hash(key)% 100  
        d=self.table[i].find(key,0)
        if d==None :
            return False
        else:
            self.table[i].remove(d,True)
            return True
    
