#class 创建类
class student:
    def __init__(self,name,age):  #__init__:初始化类,在使用类的同时自动调用
        self.name=name #实例属性/实例变量
        self.age=age
    def study(self,course_name):
        print("%s正在学习%s."%(self.name,course_name))
def main():
    stu1=student("小董","19")#stu1为类的实例
    stu1.study('python100天课程')
    stu2=student("小陈","18")
    stu2.study("英语")
if __name__=='__main__':
    main()

#数字时钟
from time import sleep

class clock:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def run(self):
        self.second=self.second+1
        if self.second==60:
            self.second=0
            self.minute=self.minute+1
            if self.minute==60:
                self.minute=0
                self.hour=self.hour+1
                if self.hour==24:
                    self.hour=0
    def show(self):
        return "%02d:%02d:%02d"%(self.hour,self.minute,self.second)
def main():
    hour=int(input("hour:"))
    minute=int(input("second:"))
    second=int(input("second:"))
    Clock=clock(hour,minute,second)
    while True:
        print(Clock.show())#调用类内部的方法时要加括号
        sleep(1)#sleep(推迟执行的秒数)
        Clock.run()

if __name__=="__main__":
    main()

#计算坐标移动的类
from math import sqrt

class Point:
    def __init__(self,x=0,y=0):
        #原有的坐标
        self.x=x
        self.y=y
    def move_to(self,x,y):
        #新的坐标
        self.x=x
        self.y=y
    def move_by(self,dx,dy):
        #坐标的移动
        self.x=self.x+dx
        self.y=self.y+dy
    def distance_to(self,other):
        dx=self.x-other.x
        dy=self.y-other.y
        return sqrt(dx**2+dy**2)

    def __str__(self):
        return '(%s,%s)'%(str(self.x),str(self.y))

p1=Point(3,5)
p2=Point()
print(p1)
print(p2)

"""
1	__init__ ( self [,args...] )   构造函数
简单的调用方法: obj = className(args)
2	__del__( self )                析构方法, 删除一个对象
简单的调用方法 : del obj
3	__repr__( self )               转化为供解释器读取的形式
简单的调用方法 : repr(obj)
4	__str__( self )                用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
5	__cmp__ ( self, x )            对象比较
简单的调用方法 : cmp(obj, x)



























    
