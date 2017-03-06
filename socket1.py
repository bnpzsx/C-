import socket
import 加解密
sg=input("1为客户端，2为服务器")
a=socket.socket()
if sg=="1":
    
    host=input("请输入目标ip")
    if(host==""):
        host="newball.havealook.top"
    port=(input("请输入端口"))
    if(port==""):
        port=1234
    else:
        port=int(port)
    while(1):
        err=a.connect_ex((host,port))
        if err==0:
            print("连接成功")
            break;
        else:
            print("连接失败，%d,尝试重新连接" % err)
    while(1) :
        str=a.recv(256)
        if str!=b"":
            print (加解密.encry(a.recv(1024),13)[:-1])
            
elif sg=="2":
    host=socket.gethostname()  #"localhost" #难道 只能用这个方法获取到要连的地址
    print ("绑定ip:" ,host)
    while(1):
        port=(input("请输入监听端口"))
        if(port==""):
            port=1234
        else:
            port=int(port)
            
        try:
            a.bind((host, int(port)))    
        except:
            print ("端口可能已被占用")       
        else:
            print ("监听成功在%d" % port)
            break;
    a.listen(5)
    while True:
        c, addr = a.accept()    
        print ('连接地址：', addr)
        c.send(加解密.encry('hello',13).encode(encoding='utf_8')) #要实现其他功能估计要用到多线程
        #c.close()   #感觉c要单开一个线程             
        for i in range(10):
            c.send(加解密.encry('hello',13).encode(encoding='utf_8'))
        
