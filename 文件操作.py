import os
class me:
    def get(self,str):
        str=input(str)
        return str

    def put(self,str,*s):
        print ("输出:")
        print (str)
        for var in s:
            print (var)
        return

a=me()
while(1):
    str=a.get("请输入文件名")
    try:
        b=open(str,'a+',-1)
    except:
        print ('打开文件失败')
    else:
        print ('打开文件成功')
        break;

str=a.get("请输入写入内容")
try:
    b.write(str)
except:
    print ('写入文件失败')
else:
    print ('写入文件成功')
    
b.seek(0,0) #定位当前位置到开头
a.put(b.read())
str=b.name
b.close()
if input("是否删除文件（y/n）")[0]=='y':
    try:
        os.remove(str)
    except:
        print ('删除文件失败')
    else:
        print ('删除文件成功')
        
a.put("当前工作目录为\n\t" +os.getcwd())
os.mkdir(a.get("请输入目录名称"))
try:
    os.remove(str)
except:
    print ('创建目录失败')
else:
    print ('创建目录成功')

os.chdir(a.get("请输入切换目录"))
a.put("当前工作目录为\n\t" +os.getcwd())
