"""
#水仙花数
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i**3+j**3+k**3==i*100+j*10+k:
                print(100*i+10*j+k)
#正整数反转
a=int(input("请输入一个正整数："))
sum=0
while a>=10:
    sum=sum+a%10
    sum=sum*10
    a=a//10
sum=sum+a
print(sum)
#百钱问题
for i in range (0,21):
    for j in range(0,33):
        z=100-i-j
        if z%3!=0:
            continue
        elif z/3+i*5+j*3==100:
            print("公鸡：%d,母鸡：%d,小鸡：%d"%(i ,j,z))


#Graps赌博游戏
from random import randint
money=1000
mm=1
while money>0:
    b=int(input("请下注："))
    a=randint(1,6)+randint(1,6)
    if a==7 or a==11:
        money=money+b
        print("所摇点数为：%d"%(a))
        print("你赢了，现有筹码为：%d"%(money))
        continue
    if a==2 or a==3 or a==12:
        money=money-b
        print("所摇点数为：%d"%(a))
        print("你输了，现有筹码为：%d"%(money))
        continue
    else:
        print("第一次所摇点数为：%d"%(a))
        while mm==1:
            c=randint(1,6)+randint(1,6)
            if c==7:
                money=money-b
                print("你摇出的点数为：%d"%(c))
                print("你输了，现有的筹码为：%d"%(money))
                break
            elif c==a:
                money=money+b
                print("你摇出的点数为：%d"%(c))
                print("你赢了，现有的筹码为：%d"%(money))
                break
            else:
                print("你摇出的点数为：%d"%(c))
                continue
print("你输了，远离赌博，从我做起")

#斐波那契数列前20个
print(1,end=" ")
print(1,end=' ')
a=1
b=1
for i in range(1,19):
    if i%2==0:
        a=a+b
        print(a,end=" ")
    if i%2!=0:
        b=a+b
        print(b,end=" ")

"""
#10000之内的完美数
for i in range(1,10001):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if sum==i:
        print(i)
        
#100以内的素数
print(2,end=' ')
for i in range(3,101,2):
    flag=1
    j=1
    while j*j<=i:
        j=j+1
        if i%j==0:
            flag=0
            break
    if flag==1:
        print(i,end=' ')

