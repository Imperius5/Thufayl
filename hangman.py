import random

with open("words.txt","r") as textFile:
    words  = textFile.readlines()
    word = random.choice(words)[:-1]



Chances = 6
guessedLetters = []
temp = 1

def hangman():
    global temp
    global Chances
    while temp:
        for char in word.upper():
            if char in guessedLetters:
                print(char, end = " ")
            else:
                print("_", end = " ")
        print("")


        
        print("\n""Chances left:", Chances)
        guessedWord = input("\n""Guess a word:").upper()
        guessedLetters.append(guessedWord)
        if guessedWord not in word.upper():
            Chances -= 1
            if Chances == 0:
                break

        temp = 0

        for char in word.upper():
            if char not in guessedLetters:
                temp = 1

hangman()

if temp == 0:
    print("\n""Congratulations!!!, You've found the word. It was", word.upper())

else:
    print("\n""You've ran out of tries :(, The word was", word.upper())


for i in range(1000):
    temp = 1
    Chances = 6
    choice = input("\n""Do you want to play again? (Y/N):").upper()

    if choice == "Y":
        with open("words.txt","r") as textFile:
            words  = textFile.readlines()
            word = random.choice(words)[:-1]
        guessedLetters = []
        hangman()
        if temp == 0:
            print("\n""Congratulations!!!, You've found the word. It was", word.upper())

        else:
            print("\n""You've ran out of tries :(, The word was", word.upper())
    else:
        print("\n""Thanks for Playing.")
        break






    