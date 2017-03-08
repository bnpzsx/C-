class node:
    pre=None
    next=None
    data=None
    def __init__(self,data,pre=None,next=None):
        self.data=data
        self.pre=pre
        self.next=next
        # print("creat a node",data)

    def __del__(self):pass
        # print("del a node",self.data)

class linklist:
    root=None
    def append(self,data):
        if data==self:return False #添加自身引用在print时会死循环
        i=self.root
        if i!=None:
            while i.next!=None:
                i=i.next
            i.next=node(data,i)
        else:
            self.root=node(data)
        
    def find(self,data):
        if self.root==None:return None
        i=self.root
        while i.next!=None and i.data!=data:
            i=i.next
        if i.data==data:
            return i
        else:
            return None

    def remove(self,data):
        i=self.find(data)
        if i==None:
            return False
        else:
            if i!=self.root:
                i.pre.next=i.next
            else:
                self.root=i.next
                
            if i.next!=None:
                i.next.pre=i.pre
            del i
            return True

    def cstr(self,data):
        if type(data)==str:
            return "\""+data+"\""
        else:
            return str(data)

    def __str__(self):
        i=self.root
        if i==None:
            return "[]"
        else:
            string='['
            while i.next!=None:
                string=string+self.cstr(i.data)+','
                i=i.next
            string=string+self.cstr(i.data)+']'
        return string

    def __del__(self):
        i=self.root
        if i==None:return
        while i.next!=None:
            i=i.next
        while i.pre!=None:
            i=i.pre
            del i.next
            

