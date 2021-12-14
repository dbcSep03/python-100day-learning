print(2015)
m_2015=open("读者借阅日志2015.csv","r",encoding='UTF-8-sig').readlines()
n_2015={}
for line_2015 in m_2015:
    line_2015=line_2015.split(",")
    if line_2015[4] in n_2015:
        n_2015[line_2015[4]] = n_2015[line_2015[4]]+1+int(line_2015[0])
    else:
        n_2015[line_2015[4]] = int(line_2015[0])
a_2015=list(n_2015.items())
a_2015.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    book,times=a_2015[i]
    print("{0:10}{1:>5}".format(book,times))
print(2016)
m_2016=open("读者借阅日志2016.csv","r",encoding='UTF-8-sig').readlines()
n_2016={}
for line_2016 in m_2016:
    line_2016=line_2016.split(",")
    if line_2016[4] in n_2016:
        n_2016[line_2016[4]] = n_2016[line_2016[4]]+1+int(line_2016[0])
    else:
        n_2016[line_2016[4]] = int(line_2016[0])
a_2016=list(n_2016.items())
a_2016.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    book,times=a_2016[i]
    print("{0:10}{1:>5}".format(book,times))
print(2017)
m_2017=open("读者借阅日志2017.csv","r",encoding='UTF-8-sig').readlines()
n_2017={}
for line_2017 in m_2017:
    line_2017=line_2017.split(",")
    if line_2017[4] in n_2017:
        n_2017[line_2017[4]] = n_2017[line_2017[4]]+1+int(line_2017[0])
    else:
        n_2017[line_2017[4]] = int(line_2017[0])
a_2017=list(n_2017.items())
a_2017.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    book,times=a_2017[i]
    print("{0:10}{1:>5}".format(book,times))
print(2018)
m_2018=open("读者借阅日志2018.csv","r",encoding='UTF-8-sig').readlines()
n_2018={}
for line_2018 in m_2018:
    line_2018=line_2018.split(",")
    if line_2018[4] in n_2018:
        n_2018[line_2018[4]] = n_2018[line_2018[4]]+1+int(line_2018[0])
    else:
        n_2018[line_2018[4]] = int(line_2018[0])
a_2018=list(n_2018.items())
a_2018.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    book,times=a_2018[i]
    print("{0:10}{1:>5}".format(book,times))
print(2019)
m_2019=open("读者借阅日志2019.csv","r",encoding='UTF-8-sig').readlines()
n_2019={}
for line_2019 in m_2019:
    line_2019=line_2019.split(",")
    if line_2019[4] in n_2019:
        n_2019[line_2019[4]] = n_2019[line_2019[4]]+1+int(line_2019[0])
    else:
        n_2019[line_2019[4]] = int(line_2019[0])
a_2019=list(n_2019.items())
a_2019.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    book,times=a_2019[i]
    print("{0:10}{1:>5}".format(book,times))
