# -*- coding: UTF-8 -*-
#function
print(int(2.6))
print(chr(65))
print(ord('A'))
print(round(2.34,1))

#2,'A',65,2.3
#temperature
def fahrenheitToCelsius(t):
    convertedTemperature = (5 / 9) * (t - 32)
    return convertedTemperature

fahrenheitTemp = eval(input("Enter a temperature in degrees Fahrenheit:"))
celsiusTemp = fahrenheitToCelsius(fahrenheitTemp)
print("Celsius equivalent: ", celsiusTemp, "degree")


#name
def firstname(fullname) :
    firstSpace = fullname.index(" ")
    givenname = fullname[:firstSpace]
    return givenname

fullName = input("Enter a person name: ")
print("first name: ",firstname(fullName))

#

def triple(num) :
    num = 3 * num
    return num

num = 2
print(triple(num))
print(num)

#
def pay(wage, hours) :
    if hours <= 40:
        amount = wage * hours

    else :
        amount = (wage * 40) + ((1.5) * wage * (hours - 40))

    return amount

print(pay(10, 50))

def futureValue(p, r, m, t) :
    i = r / m
    n = m * t
    amount = p * ((1 + i) ** n)
    return amount
p = eval(input("Enter amount deposited : "))
r = eval(input("Enter annual rate of interest in decimal form : "))
m = eval(input("Enter number of times interest is compounded per year: "))
t = int(input("Enter number of years: "))
print("money: ${0:,.2f}".format(futureValue(p, r, m, t)))

#return False or True

def isVoweWord(word) :
    word = word.upper()
    vowels = ('A', 'E', 'I', 'O', 'U')
    for vowel in vowels :
        if vowel not in word:
            return False
    return True

word = input("Enter a word: ")
if isVoweWord(word) :
    print(word, "contains every vowel")

else :
    print(word, "does not contains every vowel")

