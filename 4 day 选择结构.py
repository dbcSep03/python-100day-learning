
#判断1个正整数是不是素数
a=int(input("请输入一个正整数："))
flag =1;
i=1;
if a==1:
    print("1不是素数")
elif a==2:
    print("2是素数")
else:
    while i*i<=a:
        i=i+1
        if a%i==0:
            flag=0
            break
    if flag==1:
        print("%d是素数"%(a))
    else:
        print("%d不是素数"%(a))
#计算最大公因数和最小公倍数
a=int(input("请输入第一个数："))
b=int(input("请输入第二个数："))
c=min(a,b)+1
e=max(a,b)
d=1#储存最大公因数
f=i#储存最小公倍数
for j in range(2,c):
    if a%j==0 and b%j==0:
        d=j
        break
for i in range(e,a*b+1):
    if i%a==0 and i%b==0:
        f=i
        break
print("最小公倍数为：%d,最大公因数为：%d"%(f,d))

#练习三打印三角形图案
a=int(input("请输入行数："))
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end='')
    print()
for i in range(1,a+1):
    for j in range(1,a-i+1):
        print(" ",end='')
    for k in range(1,i+1):
        print("*",end='')
    print()
for i in range(1,a+1):
    for j in range(1,a-i+1):
        print(" ",end='')
    for k in range(1,2*i):
        print("*",end='')
    for j in range(1,a-i+1):
        print(" ",end='')
    print()






























    
