#function

def occurringVowels(word) :
    word = word.upper()
    vowels = ('A', 'E', 'I', 'O', 'U')
    includedVowels = []
    for vowel in vowels :
        if (vowel in word) and (vowel not in includedVowels) :
            includedVowels.append(vowel)

    return includedVowels

word = input("Enter a word:")
listOfVowels = occurringVowels(word)
print("The following vowels occur in the world: ", end = " ")
stringOfVowels = " ".join(listOfVowels)
print(stringOfVowels)

# no return

def oldMcDonald(animal, sound) :
    print("Old McDonald had a farm. Eyi eyi oh.")
    print("And on his farm he had a", animal + ".", "Eyi eyi oh.")
    print("With a", sound, sound, "here, and a", sound, sound, "there.")
    print("Here a", sound + ",", "there a", sound + ",", "everywhere a", sound, sound + ".")
    print("Old McDonald had a farm. Eyi eyi oh.")



oldMcDonald("lamb", "baa")
print()
oldMcDonald("duck", "quack")
print()


def main() :
    fullName = input("Enter a person's full name: ")
    print("First name: ", firstName(fullName))

def firstName(fullName) :
    firstSpace = fullName.index(" ")
    givenName = fullName[:firstSpace]
    return givenName

main()


def main1() :
    describeTask()
    calculateDensity("Hawaii", 1375000, 6423)
def describeTask() :
    print("This program display the population")
    print("density of the last state to become")
    print("part of the United States.\n")
def calculateDensity(state, pop, landArea) :
    density = pop / landArea
    print("The density of", state, "is")
    print("{0:,.2f} people per square mile.".format(density))

main1()
