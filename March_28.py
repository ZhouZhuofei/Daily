# exercise

#P174.7

list1 = ["pear", "Banana", "apple"]
list1.sort()
print(list1)
list1.sort(key=lambda x: x.upper())
print(list1)
list1.sort(reverse = True)
print(list1)
list1.sort(key=lambda x: len(x), reverse = True)
print(list1)

#p174.9
def main() :
    display("numdge ")
    display("nudge ", 4)
def display(x, times = 2) :
    print(x * times)

main()

#p174.10
def main1() :
    for i in range(3) :
        print(func())

def func(x = []) :
    x.append("wink")
    return x
main1()

#p174.11
def main2() :
    display("spam", "and", "eggs", 5)
    display("spam", "and", "eggs")

def display(x, y, z, spacing = 1) :
    print(x + (" " * spacing) + y + (" " *spacing) + z)

main2()

#p174.12
def main3() :
    x, y = getTwoIntegers()
    x, y = calculateSumAndProduct(x, y)
    displaySumAndProduct(x, y)

def getTwoIntegers() :
    a = int(input("Enter first integer :"))
    b = int(input("Enter second integer :"))
    return a, b
def calculateSumAndProduct(x, y) :
    return x + y, x * y
def displaySumAndProduct(x, y):
    print("sum" + ':', x)
    print("Product" + ':', y)

main3()

#p175.13

presidents = [("John Adams", 61), ("George Washington", 57)]
presidents.sort(key=lambda pres: pres[1])
for pres in presidents:
    print(pres[0])


#p175.14

def main4() :
    composers = ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Franz Joseph Haydn", "Ralph Vaughan Williams"]
    composers.sort(key=lengthOfLastname)
    for composer in composers :
        print(composer)

def lengthOfLastname(composer) :
    complist = composer.split()
    return len(complist[-1])

main4()

#p175.15

def main5() :
    composers = ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Franz Joseph Haydn", "Ralph Vaughan Williams"]
    composers.sort(key=middlename)
    for composer in composers :
        print(middlename(composer))

def middlename(composer) :
    complist = composer.split()
    return complist

main5()



