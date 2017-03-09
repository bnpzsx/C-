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
        c.sendall(input(""))
        turn=1
    else:sleep(0.1)
