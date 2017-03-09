while(1):
    str = input("请输入：");
    if "cmd" in str:
        if str[0:4]=="cmd ":
            try:
                s=eval(str[4:])
                if s!=None:
                    print(s)
            except Exception as e:
                print("发生错误：",e)
    else:
        print("你输入的内容是: ", str)
