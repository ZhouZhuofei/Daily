# -*- coding: UTF-8 -*-
##[1,2,3]+[4,5,6]
print([1, 2, 3]+[4, 5, 6])
#>>>[1, 2, 3, 4, 5, 6]
a = [1, 2]
b = [3, 4]
print(a + b)
#>>>[1,2,3,4]
c = 'my name is'
d = "IG"
print(c + d)
#>>>my name is IG
print("Hello"*5)   #>>>HelloHelloHelloHelloHello
print([7]*8)       #>>>[7,7,7,7,7,7,7,7,7]
######check a in greeting = "Hello,world"
greeting = "hello,world"
print('a' in greeting) #>>>False

#Checks if the string is in the string list
uesr = ["me", "I", "our", "ours"]
print('I' in uesr)    #>>>True
##len, max, min
number = [300, 200, 100, 800, 500]
len(number)           #>>>5
max(number)           #>>>800
min(number)           #>>>100
max(5, 10, 3, 7)      #>>>10
################################
#updata list
e = [1, 2, 3, 4, 8]
e[0] = 10
print(e)               #>>>[10, 2, 3, 4, 8]
#add list elemnts

tring = ['happy', "sad"]
tring.append('hehe')
print(tring)           #>>>['happy', 'sad', 'hehe']
#delect list elements

del tring[0]
print(tring)           #>>>['sad', 'hehe']

################################
name = list('myname')
print(name)            #>>>['m', 'y', 'n', 'a', 'm', 'e']

test = list('hi')
print(test)            #>>>['h', 'i']
test[1:] = list('ello')
print(test)            #>>>['h', 'e', 'l', 'l', 'o']
################################
#nested list
field = ['a', 'b', 'c']
print(field)
num = [1, 2, 3]
max = [field, num]
print(max)             #>>>
