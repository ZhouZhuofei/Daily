def avg(x) :
    sum = 0
    for i in x :
        sum = i + sum
    avg = sum / len(x)

    return avg

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(avg(x))

def jiecheng(n) :
    sum = 1
    for i in range(1,n + 1) :
        sum = sum * i
        i = i + 1
    return sum
print(jiecheng(10))

def main() :
    firstPart()
    print(str(4) + ": from function main")

def firstPart() :
    print(str(1) + ": from function firstPart")
    secondPart()
    print(str(3) + ":from function firstPart")

def secondPart() :
    print(str(2) + ": from function secondPart")

main()

INTEREST_RATE = 0.04


def main0() :
    principal = eval(input("Enter the amount of the deposit: "))
    numberOfYear = eval(input("Enter the number of year : "))
    (bal, intEarned) = balanceAndInterest(principal, numberOfYear)
    print("Balance : ${0:,.2f}  Interest Earned : ${1:,.2f}".format(bal, intEarned))

def balanceAndInterest(prin, numberYears) :
    balance = prin * ((1 + INTEREST_RATE) ** numberYears)
    intEarned = balance - prin
    return (balance, intEarned)

main0()

