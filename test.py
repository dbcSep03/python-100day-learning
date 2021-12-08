#当测试时将“6 day 函数和模块化使用”改为“day6”
from day6 import huiwenshu
from day6 import sushu
a=int(input())
if sushu(a) and huiwenshu(a):
    print("回文素数")
else:
    print("不是回文素数")
