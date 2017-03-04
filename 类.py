class date:
    '日期'
    __year=0
    __month=0
    __day=0
    daytable=[31,28,31,30,31,30,31,31,30,31,30,31]
    def __init__(self,year=1998,month=1,day=1):
        self.__year=year
        self.__month=month
        self.__day=day
        
    def show(self):
        print('今天是%d年%d月%d日' %(self.__year,self.__month,self.__day))

    def nextday(self):
        y=self.__year # 不是引用?
        d=self.__day
        m=self.__month
        d+=1
        if m==2:
            if (y%4==0 and y%100!=0) or (y%400==0):
                self.daytable[1]=29
            else:
                self.daytable[1]=28
        if d>self.daytable[m-1]:
            d=1
            m+=1
            if m>12 :
                y+=1
                m=1    
        self.__year=y
        self.__day=d
        self.__month=m
        self.show()
        
class people(date):
    '人类'
    def __init__(self,name,age=0):
        date.__init__(self,2016,1,1) # 初始化父类
        self.show()
        print ('%s 今年 %d 岁'%(name,age))


a=people('by',18)
for i in range(365):
    a.nextday()
