#验证用户名和QQ号
#用户名6-20位字母数字下划线构成
#qq号位5-12位首位不为0的数字组成
"""
r'': 一般用在正则表达式中，称为原始字符串，作用是将Python语法中的反斜杠转义给

取消，将其设置成为一个普通的字符串。可以解决Python中的转义字符和正则表达式中的转义

字符之间的冲突问题。
"""
import re

def main():
    usename=input("请输入用户名：")
    QQ=input("请输入QQ号：")
    m1=re.match(r'^[0-9a-zA-Z_]{6,20}$',usename)
    m2=re.match(r'^[1-9]\d{4,11}$',QQ)
    if not m1:
        print("请输入正确的用户名：")
    if not m2:
        print("请输入正确的QQ：")
    if m1 and m2:
        print("输入正确")

if __name__=="__main__":
    main()
import re
def main():
    poem="锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒当辛苦。"
    sentences=re.split(r'[,。，。]',poem)#按照列表中分割，（。）分割后前后断裂，变成''
    print(sentences)
    while ''in sentences:
        sentences.remove('')
    print(sentences)
if __name__=="__main__":
    main()