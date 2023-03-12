from random import randint

# Main Function That Calls and Utilizes All Methods
def main():
    letter = ''
    words = [""] * 10
    word = ""
    guessedLetters = ['_'] * 6
    noItems = 0
    noGuesses = 6

    words , noItems = enterWords()
    word = randomWord(words , noItems)
    wordSoFar = ["_"] * len(word)

    print()
    print()
    print("Welcome To Hangman!")
    print()
    print("You Get 6 Guesses ... Good Luck")
    print()

    flag = True

    while flag:
        if noGuesses > 0:
            letter = getLetter()
        
        isLetterInWord = checkLetter(letter , word)

        if isLetterInWord:
            wordSoFar = displayWordSoFar(wordSoFar , letter , word)
            print()
            print("Wuhu ... Correct Letter")
            print()
            print("Your Word So Far:" , wordSoFar)
            print("Guesses Remaining:" , noGuesses)
            print()
        else:
            noGuesses -= 1
            guessedLetters = displayGuessedLetters(guessedLetters , letter)
            print()
            print("Oh No :( ... Wrong Letter")
            print()
            print("Guessed Letters:" , guessedLetters)
            print("Guesses Remaining:" , noGuesses)
            print()
        
        if len(wordSoFar) == len(word):
            c = 0
            for i in range(len(word)):
                if word[i] == wordSoFar[i]:
                    c += 1
            if c == len(word):
                print("Congratulations! ... You Win")
                flag = False
        
        if noGuesses <= 0:
            print("Reached Number of Guesses :(")
            print("The Correct Word Was ..." , word)
            print()
            flag = False

# User Enters Words for Dictionary
def enterWords():
    i = 0
    noItems = 0
    words = [""] * 10

    flag = True

    while flag and i <= 10:
            
        if i == 10:
            print()
            print("Reached Maximum")
            print()
            flag = False
        else:
            w = input("Enter Word (Type 'Done' When Finished .. Max 10): ").lower()


        if noItems < 0 and w == "done":
            print("Enter Atleast 1 Word")

        elif w == "done" and noItems == 0:
            print("Enter Minimum of 1 Letter")
        
        elif w == "done" and noItems > 0:
            flag = False
        
        elif i < 10:
            words[i] = w
            noItems += 1
            i += 1

    return words , noItems

# Choose Random Word From Given Entry
def randomWord(words , noItems):
    index = randint(0 , noItems - 1)

    return words[index]

# User Enters Guessed Letter
def getLetter():
    while True:
        letter = input("Enter Letter ... ")

        if len(letter) > 1:
            print("Please Enter a Letter")
            continue
        else:
            break
    
    return letter

# Check if Letter is in Random Word
def checkLetter(letter , word):
    
    for i in range(len(word)):
        if letter == word[i]:
            return True
    
    return False

# Display Word You Have So Far With Entered Guessed Letters
def displayWordSoFar(wordSoFar , letter , word):

    for i in range(len(word)):
        if letter == word[i]:
            wordSoFar[i] = letter

    return wordSoFar

# Display Wrong Guessed Letters
def displayGuessedLetters(guessedLetters , letter):

    for i in range(len(guessedLetters)):
        if guessedLetters[i] == '_':
            guessedLetters[i] = letter
            break
        else:
            continue
    
    return guessedLetters




main()