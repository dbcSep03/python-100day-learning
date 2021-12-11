#餐馆
class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        self.number_served=0
    
    def describe_restaurant(self):
        print("餐馆的名字为："+self.name.title())
        print("菜单为："+self.cuisine_type.title())
    def open_restaurant(self):
        print(self.name.title()+"正在营业")
    def set_number_served(self,number): #通过方法对属性的值进行设定
        self.number_served =number
    def increment_number_served(self,number): #通过方法对属性进行增值
        self.number_served += number
class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine_name):
        super().__init__(name,cuisine_name)
        self.flavor=[]
        pass
    
    def flavors(self,*a):
        self.flavor =self.flavor+list(a) 
"""        
def main():
    first=Restaurant('meishi','chess')
    second=Restaurant('zhongshi','yangzhoufan')
    third=Restaurant('gangshi','zaocha')
    first.describe_restaurant()
    first.open_restaurant()
    print("服务过："+str(first.number_served))
    first.number_served=100#直接修改属性的值
    print("服务过: "+str(first.number_served))
    first.set_number_served(1000)
    print("服务过："+str(first.number_served))
    first.increment_number_served(50)
    print("服务过: "+str(first.number_served))

 if __name__=='__main__':
    main()
"""

def main():
    first=IceCreamStand("mishengke","tiantong")
    first.flavors("chocolate","Math","English")
    print(first.flavor)
    
    
if __name__=="__main__":
    main()
    
    
#继承 当子类调用继承父类是，可用super().__init__(),来继承，而__init__()括号中不用加self.且在定义子类名时，括号内，加入父名
#且父类与子类的方法重名时，优先的为子类。
#类与类之间可以相互引用。与实例的引用类似self.(属性名)=类名.()
#从其他文件中引用类 from （文件名为英语）import （类名）   #多个之间，用逗号隔开
#若要导入所有库，则为： from (文件名) import*    (不推荐)
