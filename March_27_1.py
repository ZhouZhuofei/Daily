#习题4.2
def main() :
    howMany(24)
    print("a pie")

def howMany(num) :
    what(num)
    print("baked in", end = " ")

def what(num) :
    print(num, "blackbirds", end = " ")

main()


def main0() :
    advice()

def advice() :
    print("Keep cool, but don't freeze.")
    source()

def source() :
    print("Source : A jar of mayonnaise.")

main0()

def main1() :
    cost = 250
    displayBill(cost, shippingCost(cost))

def shippingCost(costOfGoods) :
    if costOfGoods < 100 :
        return 10
    elif costOfGoods < 500:
        return 15
    else :
        return 20

def displayBill(cost, addedCost) :
    print("Cost: {0:.2f}".format(cost))
    print("Shipping cost: ${0:.2f}".format(addedCost))
    print("Total cost: ${0:.2f}".format(cost + addedCost))

main1()

def main2() :
    grade = int(input("Enter your numberic grade: "))
    showResult(grade)

def showResult(grade) :
    if passedExam(grade) :
        print("You passed with a grade of", str(grade) + '.')
    else :
        print("You failed the exam.")

def passedExam(grade) :
    if grade >= 60:
        return True
    else :
        return False

main2()


def main3() :
    gradeList = list(getThreeGrade())
    gradeList.sort()
    print(gradeList)

def getThreeGrade() :
    x = int(input("Enter first grade :"))
    y = int(input("Enter second grade :"))
    z = int(input("Enter third grade : "))
    return x, y, z

main3()
