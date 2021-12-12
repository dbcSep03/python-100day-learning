# 文件和异常
## 读取文件
|操作模式|具体含义|
|----|----|
|‘r’|读取（默认）|
|‘w’|覆盖写模式，不存在创建，存在则完全覆盖|
|‘x'|创建写模式，不存在则创建，存在则返回FileExistsError|
|’a‘|追加写模式，不存在则创建，存在则在文件最后追加内容|
|’b'|二进制文件模式|
|‘t'|文本模式（默认）|
|’+‘|与/r/w/x/a一同使用，增加读写功能|

读取文件时，利用 open（）函数，先为文件名，其次为文件模式设置，最后为编码模式（encoding=）

### try 函数
try...except ...else..模式：

```
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
```
try...except...finally..模式：
```
try:
<语句>
finally:
<语句>    #退出try时总会执行
```
可以通过python的try except语法结构来调试
### with()函数的使用
### 文件的读写
|操作方法|含义|
|----|----|
|<file>.readall（）|读入整个文件内容，返回一个字符串或者字节流|
|<file>.read（size=-1）|从文件中读入整个文件内容，如果给出参数，读入前size长度的字符串或字节流|
|<file>.readline(size=-1)|从文件中读取一行内容，如果给出参数，读入前size长度的字符串或字节流|
|<file>.readlines(hint=-1)|从文件中读入所有行，以每一行每一个列表，如果给出参数，读入hint行|

### 读取JOSN文件
|JOSN|Python|
|----|----|
|object|dict|
|array|list|
|string|str|
|number(int/list)|int/float|
|true/false|True/False|
|null|None|

|Python|JSON|
|----|----|
|dict|object|
|list,tuple|array|
|str|string|
|int,flaot,int-&float-derived Enums|number|
|True/False|true/false|
|None|null|
在python中引入JOSN文件时，需要引入JOSN库
```
import josn
```
josn模块四个重要的函数
* dump-将python对象按照JOSN格式序列化到文件中
* dumps-将python对象处理成JOSN格式字符串
* load-将文件中的数据反序列化成对象
* loads-将字符串内容反序列化成python对象
注：序列化（serialization）在计算机科学的数据处理中，是指将数据结构或对象状态转换为可以存储或传输的形式，这样在需要的时候能够恢复到原先的状态，而且通过序列化的数据重新获取字节时，可以利用这些字节来产生原始对象的副本（拷贝）。与这个过程相反的动作，即从一系列字节中提取数据结构的操作，就是反序列化（deserialization）