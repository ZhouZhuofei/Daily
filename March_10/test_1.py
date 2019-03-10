# -*- coding: UTF-8 -*-
#count
field = list('hellow, world')
print(firld.count('o'))

#expend
a = ['hello', 'world']
b = ['python', 'is', 'funny']
a.extend(b)
print(a)

#index
f = ['python', 'is', 'better']
field.extend(f)
print(field)
print(field.index('python'))

#insert
num = [1, 2, 3]
print('before insert',num)
num.insert(2,'insert number')
print('after',num)

#pop
print(field)
field.pop(11)
print(field) #delect 'python'

num1 = [1, 2, 3]
num1.append(num1.pop())
print(num1)

#remove
field.remove('python')
print(field)

#reverse

num.reverse()
print(num)

#sort
num1.sort()
print(num1)

#clear
field.clear()
print(field)

#copy
field1 = field.copy()
print(field)

#advance sort
field = ['study', 'python', 'is', 'happy']
field.sort(key = len)
num = [5, 8, 1, 3, 6]
num.sort(reverse = True)
