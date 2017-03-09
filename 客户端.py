import socket2
from time import sleep
turn=0
class me(socket2.mysocket):
    def recv(self,who,string):
        self.L[1]()
        print(string)
        self.L[2]()
        global turn
        turn=0

    def con(self):
        global turn
        turn=1

c=me()
c.connect()
while turn==0:
    sleep(0.1)
while 1:
    if turn ==0:
        s=input("").strip() #去除字符串两端空格
        if s=="":
            pass
        else:
            turn=1
            c.sendall(s)
    else:sleep(0.1)
