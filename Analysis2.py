import codecs
import itertools 
from itertools import islice
import numpy as np
import decimal
decimal.getcontext().rounding = "ROUND_HALF_UP"#四舍五入


line_num = 0 

f = codecs.open('sys_summary.tab', mode='r', encoding='GBK')  # 打开txt文件，以‘utf-8’编码读取
#任务1
for line_num in islice(f, 0, None): 
    line = f.readline()   # 以行的形式进行读取文件
    list1 = []
    list3 = []
    while line:
        a = line.split()
        c = line.split()
        b = a[2:3]  # 这是选取需要读取的位数
        list1.append(b)  # 将其添加在列表之中
        d = c[15:16]
        list3.append(d)
        line = f.readline()    
#任务3
   
  
f.close()


c = np.array(list1)
d = np.array(list3)





# d = np.array(c)
list1_float = []
list3_float = []

def intoFloat ():#转换为浮点

    
    for x in range(len(c)):
        a = float(c[x])
        
        
        # print(a)
        list1_float.append(a)

def intoFloat3 ():
    
    
    for x in range(len(d)):
        a = float(d[x])
        
        
        # print(a)
        list3_float.append(a)
   
    

intoFloat()
intoFloat3()
list2 = sorted(list1_float,reverse=True)
list4 = sorted(list3_float,reverse=True)
# print(list2)
# print('length =',len(list1_float))
# print(decimal.Decimal((len(list1_float)) * 0.9).quantize(decimal.Decimal("0")))
count = int(decimal.Decimal((len(list1_float)) * 0.9).quantize(decimal.Decimal("0"))-1)#四舍五入并取整
# print('count =',count)

def average(num):
    x = 0
    for i in range(len(num)):
        x += num[i]
    return x / len(num)


def covertSize(size):
    kb=1024;
    mb=kb*1024;
    gb=mb*1024;
    tb=gb*1024;
 
   
    if size>=gb:
        return "%.5f TB"% float(size / gb)
    if size>=mb:
        return "%.5f GB"% float(size / mb)
    if size>=kb:
        return "%.5f MB"% float(size / kb)


print('RLFPS这一列的平均值 =',average(list2))

print('RLFPS这一列从大到小排序得到第90%位的数据 =',list2[count])#数组下标-1   

print('虚拟内存 =',covertSize(max(list4)))

intoFloat()




