"""
import getpass
a=getpass.getpass()
输入不显示，改用*表示。
练习1：英制单位和公制单位转换
练习2：扔骰子
练习3：百分制成绩转换
练习4：三边计算周长面积
"""
#练习1
a=float(input("请输入长度："))
b=input("请输入单位：")
if b=="英寸"or b=="in":
    print("%.2f英寸=%.2f厘米"%(a,a*2.54))
elif b=="厘米" or b=="cm":
    print("%.2f厘米=%.2f英寸"%(a,a/2.54))
else:
    print("请输入有效单位")
#练习二
#from random import randint
"""
randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。
randint 产生的随机数是在指定的某个区间内的一个值，
而 randrange 产生的随机数可以设定一个步长，也就是一个间隔。
"""
from random import randint
a=randint(1,6)
if a==1:
    print("1")
elif a==2:
    print("2")
elif a==3:
    print("3")
elif a==4:
    print("4")
elif a==5:
    print("5")
elif a==6:
    print("6")

#练习三
score=float(input("分数为："))
if score>=90:
    grade='A'
elif score>=80 and score<90:
    grade='B'
elif score>=70 and score<80:
    grade='C'
elif score>=60 and score<70:
    grade='D'
else:
    grade='E'
print('对应的等级为:',grade)
#练习四
import math
a=float(input("第一边为："))
b=float(input("第二边为："))
c=float(input("第三边为："))
if a+b<=c or b+c<=a or a+c<=b:
    print("三边无法组成三角形")
else:
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("面积为%.2f,周长为：%.2f"%(s,a+b+c))
