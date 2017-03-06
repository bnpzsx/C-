import socket
import time
import threading

L=[threading.Lock()]
L.append(L[0].acquire)
L.append(L[0].release)
com=[socket.socket(socket.AF_INET,socket.SOCK_STREAM)]
con=0

def accept():
    '接收客户端连接'
    while 1:
        c,addr=com[0].accept()
        com.append((c,addr))
        index=len(com)-1 #服务器在列表中位置
        L[1]()
        print("%d接受来自%s的连接" %(index,addr))
        L[2]()
        global con
        con=1
        threading.Thread(target = recive, args = com[index], name = 'thread-' + 'addr[0]').start()
        
def recive(s,a):
    '循环检查消息'
    L[1]()
    print("%d开始监视缓冲区" % com.index((s,a)))
    L[2]()
    while 1:
        try:
            Str=s.recv(1024) #之前用关键字str没有报错
            if Str!="":
                L[1]()
                print(bytes.decode(Str))
                L[2]()
                global con
                if con==1:
                    s.send(Str) #Echo
        except ConnectionResetError:
                L[1]()
                print("%d %s断开连接" % (com.index((s,a)),a))
                L[2]()
                com.remove((s,a))
                return

def sendall(text,s=1):
    for i in range(s,len(com)):
            com[i][0].send(str.encode(text))
        
            
def load():
    '服务器初始化'
    while 1:
        port=1234
        host="localhost"
        try:
            com[0].bind((host,port))
        except socket.err:
            print("在端口%d绑定出错"%(port))
            port+=1
        else:
            print("%s在端口%d绑定成功"%(host,port))
            break
    com[0].listen(5)
    threading.Thread(target = accept, args = (), name = 'thread-' + '0').start()
    return

def connect():
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
                com[0].connect((host,port))
            except ConnectionError:
                print("连接%s:%d失败,尝试重连..." % (host,port))
            except KeyboardInterrupt: # 实际上直接退出了程序
                break
            else:
                ok=1
                break
        if ok==1:break
    global con
    
    con=2
    print("连接成功")
    com.append((com[0],'服务器'))
    threading.Thread(target = recive, args = (com[1]), name = 'thread-' + 'addr[0]').start()
    return

if input("\'y\'为服务器，其他为客户端:")  =='y':
    load()
else:
    connect()
    
while 1:
    if con!=2:continue
    sendall(input(""))
    

