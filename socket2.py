import socket
from threading import Lock,Thread

class mysocket():
    L=[Lock()]
    L.append(L[0].acquire)
    L.append(L[0].release)
    com=[socket.socket(socket.AF_INET,socket.SOCK_STREAM)]

    
    def recv(self,who,string):pass
    
    def acpt(self,who):pass

    def accept(self):
        '接收客户端连接'
        while 1:
            c,addr=self.com[0].accept()
            self.com.append((c,addr))
            Thread(target = self.recive, args = (c,addr), name = 'thread-' + 'addr[0]').start()
            self.acpt((c,addr)) #传参不用加self
            
    def recive(self,s,a):
        '循环检查消息'
        self.L[1]()
        print("%d开始监视缓冲区" % self.com.index((s,a)))
        self.L[2]()
        global con
        while 1:
            try:
                Str=s.recv(1024)
                string=bytes.decode(Str)
                if string!="":
                    self.recv((s,a),string) #注意输出时加锁 
            except ConnectionResetError:
                    self.L[1]()
                    print("%d %s断开连接" % (self.com.index((s,a)),a))
                    self.L[2]()
                    self.com.remove((s,a))
                    return

    def sendall(self,text,s=1):
        for i in range(s,len(self.com)):
                self.com[i][0].send(str.encode(text))
            
                
    def load(self):
        '服务器初始化'
        while 1:
            port=1234
            host="localhost"
            try:
                self.com[0].bind((host,port))
            except socket.err:
                print("在端口%d绑定出错"%(port))
                port+=1
            else:
                print("%s在端口%d绑定成功"%(host,port))
                break
        self.com[0].listen(5)
        Thread(target = self.accept, args = (), name = 'thread-' + '0').start()
        return

    def connect(self):
        '客户端'
        while 1:
            ok=0 #连接成功标志
            host=input("主机:")
            if host=='':host='localhost'
            while 1:
                port=input("端口号:")
                if port=='':
                    port=1234
                    break
                else:
                    try:
                        port=int(port)
                    except:
                       print("输入有误，请重输")
                    else:
                        break
            while 1:
                try:
                    self.com[0].connect((host,port))
                except ConnectionError:
                    print("连接%s:%d失败,尝试重连..." % (host,port))
                except KeyboardInterrupt: # 实际上直接退出了程序
                    break
                else:
                    ok=1
                    break
            if ok==1:break

        print("连接成功")
        self.com.append((self.com[0],'服务器'))
        Thread(target = self.recive, args = (self.com[1]), name = 'thread-' + 'addr[0]').start()
        return


    
