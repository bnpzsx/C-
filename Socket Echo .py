from socket2 import *

con=0
if input("\'y\'为服务器，其他为客户端:")  =='y':
    class me(mysocket):
        def recv(self,who,string):
            self.L[1]()
            print("Server received:",string)
            self.L[2]()
            who[0].send(string.encode()) #Echo
            who[0].send(b"input something")

        def acpt(self,who):
            who[0].send(b"input something")
            self.L[1]()
            print("%d接受来自%s的连接" %(len(self.com)-1,who[1]))
            self.L[2]()
    a=me()
    a.load()
        
else:
    class me(mysocket):
        def recv(self,who,string):
            self.L[1]()
            print(string)
            self.L[2]()
            
        def acpt(self,who):pass

    a=me()
    a.connect()
    con=2
    
while 1:
    if con!=2:continue
    a.sendall(input(""))
