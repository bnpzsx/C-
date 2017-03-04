while(1):
    str = input("请输入：");
    print ("input你输入的内容是: ", str)
    if "cmd" in str:
        print ("cmd")
        if str[0:4]=="cmd ":
            try:
                print("执行输入命令")
                eval(str[4:])
            except : #ValueError as Argument
                print (r"发生错误: /n 退出程序")
                break
            else:
                pass
