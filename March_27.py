# 列表解析
list1 = ['2', '3', '5', '6']
print([int(x) for x in list1])

def g(x) :
    return(int(x) ** 2)

print([g(x) for x in list1])

#默认值

def total(w, x, y = 10, z = 20) :
    return(w ** x) + y + z

print(total(2, 3))
print(total(2, 3, 4,5))

def main() :

    q = "What is the capital of California? "
    a = "Sacramento"
    askQuestion(q, a)

def askQuestion(question, answer, numberOfTries = 3) :
    numberTries = 0
    while numberTries < numberOfTries :
        numberTries = numberTries + 1
        ans = input(question)
        if ans == answer:
            print("Correct!")
            break

    if ans != answer:
        print("You have uesd up your allotment of guesses. ")
        print("The correct answer is", answer + '.')

main()
