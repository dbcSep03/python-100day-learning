a=int(input("请输入年份："))
"""
if a%4 != 0:
    print("不是闰年")
elif a%100==0 and a%400 !=0:
    print("不是闰年")
else:
    print("是闰年")
    """
if a%4!=0 or(a%100==0 and a%400!=0):
    print("不是闰年")
else:
    print("是闰年")        
    
