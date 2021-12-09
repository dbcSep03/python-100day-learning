"""
#屏幕显示
import os
import time 
def main():
    content='我爱数学！'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content=content[1:]+content[0]
        
if __name__=='__main__':
    main()
"""
"""
#验证码
import random

def getcode(code_len=4):
    mima="123456789bacdefghijklmnopqrstuvwxyz"#去除大写，逻辑一样
    code=''
    for i in range(code_len):
        A=random.randint(0,len(mima)-1)
        code=code+mima[A]
    return code

if __name__=='__main__':
    print(getcode(4))
"""
"""
#得到文件名
def get_name(name,has_dot=True):
    a=name.rfind('.')#rfind查找.出现的最后一个位置。不存在返回-1
    if a>=0 and a< len(name)-1:
        index=a if has_dot else a+1
        return name[index:]
    else:
        return ''

    
if __name__=='__main__':    
    a=get_name('.text',False)
    print(a)
    
"""
"""
#最大的两个数
def self_max(L):
    a,b=(L[0],L[1]) if L[0]>L[1] else (L[1],L[0])
    for i in range(2,len(L)):
        if L[i]>a:
            a = L[i]
        elif L[i]<b:
            b=L[i]
    return a,b

if __name__=='__main__':
    l=[1,2,321,23,235132,2332,12,22,3553,9120]
    print(self_max(l))
"""
#今天是本年第几天

def is_runyear(year):
    return year%4==0 and year%100 !=0 or year%400==0

def is_what_day(year,month,day):
    a=[[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]][is_runyear(year)]
    totle = 0
    for i in range(0,month-1):
        totle=totle+a[i]
    return totle+day

if __name__=="__main__":
    print(is_what_day(2021,12,9))
#杨辉三角
def yanghui(x):
    yh=[[]]*x
    for row in range(len(yh)):
        yh[row]=[None]*(row+1)
        for col in range(len(yh[row])):
            if col==0 or col==row:
                yh[row][col]=1
            else:
                yh[row][col]=yh[row-1][col]+yh[row-1][col-1]
            print(yh[row][col],end='\t')
        print()
        
if __name__=="__main__":
    yanghui(3)















    
