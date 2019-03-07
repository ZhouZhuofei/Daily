# -*- coding: UTF-8 -*-
#int(x)将x转化成一个整数
print(int(352.1))


#float(x)将x转化成为一个浮点数

print（float（int(352.1)))


##常量PI and e
##变量赋值
A = 'my name'
B = "your name"
c = 3452
print(A,B,C)

#>>>my name your name 3452


#type确定变量类型

type(A)
type(C)
#>>>str int

########
a = 'ABC'
b = a
a = 'XYZ'
print(b)

#>>>ABC
print("this is some esay work")
###########################################
#索引
D = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(D[0])#>>> A

print(D[1])#>>> B
print(D[-1])   #>>> z

E = input()
print(E)
print(E[0])
##>>>

#分片
num = [1,2,3,5,4,6,7,8,9,10]
num[1:3]      #>>> [2,3]
num[-3:-1]    #>>> [8,9]
num[0:3]      #>>> [1,2,3]
num[:]        #>>> [1,2,3,5,4,6,7,8,9,10]
num[0:10:2]   #>>> [1,3,4,7,9]
num[::3]      #>>> [1,5,7,10]

