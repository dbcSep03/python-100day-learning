#函数定义最小公倍数和最大公因数
def max_yin(a,b):
    c=1
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            c=i
    return c
def min_bei(a,b):
    c=1
    for i in range(max(a,b),a*b+1):
        if i%a==0 and i%b==0:
            c=i
            break
    return c
#a=int(input())
#b=int(input())
#print("最大公因数为：%d,最小公倍数：%d"%(max_yin(a,b),min_bei(a,b)))
#判断回文数
def huiwenshu(a):
    b=a
    sum=0
    while a>=10:
        sum=sum+a%10
        sum=sum*10
        a=a//10
    sum=sum+a
    if sum==b:
        return  1
    else:
        return 0
#a=int(input())
#print(huiwenshu(a))        
        
#素数
def sushu(a):
    if a==1:
        return 0
    if a==2:
        return 1
    i=1
    flag=1
    while i*i<=a:
        i=i+1
        if a%i==0:
            flag=0
            break;
    if flag:
        return 1
    else:
        return 0
    #a=int(input())
    #print(sushu(a))






















