from LinkedList import linklist,node
mylist=linklist()
def newlist(key):
    if mylist.find(key,0)==None:
        mylist.append([key,linklist()])
        return True
    else:
        return "Failed"
        
def rpush(key,value):
    l=mylist.find(key,0)
    if l==None:return False
    l.data[1].append(value)
    return True
    
def lpush(key,value):
    l=mylist.find(key,0)
    if l==None:return False
    t=l.data[1].root
    if t==None:
        l.data[1].append(value)
    else:
        t.pre=node(value,None,t)
        l.data[1].root=t.pre
    return True

def lpop(key):
    l=mylist.find(key,0)
    if l==None:return False
    t=l.data[1].root
    if t==None:
        return None
    else:
        if t.next==None:
             l.data[1].root=None
        else:
            l.data[1].root=t.next
        return t.data

def rpop(key):
    l=mylist.find(key,0)
    if l==None:return False
    t=l.data[1].root
    if t==None:
        return None
    else:
        while t.next!=None:
            t=t.next
        if t.pre==None:
             l.data[1].root=None
        else:
            t.pre.next=None
        return t.data

def lrange(key,start,end):
    l=mylist.find(key,0)
    if l==None:return False
    t=l.data[1].root
    b=0
    r=[]
    while t.next!=None and b<=end:
        if b>=start:
            r.append(t.data)
        b+=1
        t=t.next
    if b<end:r.append(t.data)
    return r

def llen(key):
    l=mylist.find(key,0)
    if l==None:return False
    t=1
    r=l.data[1].root
    if r==None:return 0
    while r.next!=None:
        r=r.next
        
        t+=1
    return t

    
