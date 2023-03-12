from random import randint

def main():
    userInput = askUserInput()
    print("User:" , userInput)
    randInput = randomObject()
    print("Computer:" , randInput)

    winner = checkWinner(userInput , randInput)

    if winner == None:
        print("It's a Tie! Try Again")
        main()
    elif winner == userInput:
        print("User Wins!")
    else:
        print("Computer Wins!")

def askUserInput():
    flag = True

    while flag:
        user = input("Choose Between Rock, Paper, Or Scissors ... ").lower()

        if user == "rock":
            return user

        elif user == "paper":
            return user

        elif user == "scissors":
            return user

        else:
            print()
            print("Please Enter a Valid Option!")

def randomObject():
    arr = ["rock" , "paper" , "scissors"]
    index = randint(0,2)
    return arr[index]

def checkWinner(userInput , randInput):
    if userInput == "rock" and randInput == "paper":
        return randInput
    elif userInput == "rock" and randInput == "scissors":
        return userInput
    elif userInput == "paper" and randInput == "scissors":
        return randInput
    elif userInput == "paper" and randInput == "rock":
        return userInput
    elif userInput == "scissors" and randInput == "rock":
        return randInput
    elif userInput == "scissors" and randInput == "paper":
        return userInput
    elif userInput == randInput:
        return None

main()