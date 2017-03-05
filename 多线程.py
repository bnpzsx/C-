import threading
import time
l=threading.Lock()
ok=0
def 线程一(a=1,b=0): #发现python可以用中文作对象名
    global ok
    for i in range(10):     
        time.sleep(a)
        l.acquire()
        print ("线程一",b)
        l.release()
        b+=1
    ok+=1
        
def 线程二(a=2,b=0):
    global ok
    for i in range(10):  
        time.sleep(a)
        l.acquire()
        print ("线程二",b)
        l.release()
        b-=1
    ok+=1
threading.Thread(target = 线程一, args = (), name = 'thread-' + '1').start()
threading.Thread(target = 线程二, args = (), name = 'thread-' + '1').start()
while not ok>=2:
    time.sleep(0.1)
