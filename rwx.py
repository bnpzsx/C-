import os

def allfile(filepath):
    '遍历指定目录所有文件'
    pathDir =  os.listdir(filepath)
    dic=[]
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        if type(child)==bytes:   
            child.decode('gbk')
        dic.append(child)
    return dic

def createdic(path):
    'outnewpath=os.path.dirname(path)'
    if not os.path.exists(path):  
        os.makedirs(path)
        
class MyFile:
    path = ""
    file = None

    def __init__(self, path):
        self.path = path
        try:
            self.file = open(self.path, "a")
        except Exception as err:
            print("打开文件失败",path,err)
        else:
            print("打开文件成功",path)
        self.file.close()

    def write(self, string):
        self.file = open(self.path, "a")
        try:
            self.file.write(string)
        except Exception as err:
            print("追加失败", err)
        finally:
            self.file.close()

        
    def read(self):
        self.file = open(self.path, "r")
        s=self.file.readlines()
        self.file.close()
        return s 

    def rewrite(self, string):
        self.file = open(self.path, "w")
        self.file.write(string)
        self.file.close()
  
    def name(self):
        return os.path.basename(self.path)

