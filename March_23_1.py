def main() :
    x = 2
    print(str(x) + ": function main")
    trivial()
    print(str(x) + ": function main")
def trivial() :
    x = 3
    print(str(x) + ": function trivial")

main()

import finance

p = eval(input("Enter amount deposited: "))
r = eval(input("Enter annual rate of interest in decimal form: "))
m = eval(input("Enter number of times interest is compounded per year: "))
t = int(input("Enter number of years: "))
balance = finance.futureValue(p, r, m, t)
print("Balance after", t, "years: ${0:,.2f}".format(balance))
