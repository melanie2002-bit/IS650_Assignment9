import random

def guessTheNumber() -> None:
    secretNum: int = random.randint(1, 10)
    pastGuesses: list = []
    rightGuesses: bool = False

    while not rightGuesses:
        try:
            userNum: int = int(input("Pick a number between 1 and 10: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= userNum <= 10:
            print("Your guess must be between 1 and 10.")
            continue

        pastGuesses.append(userNum)

        if userNum == secretNum:
            print("You got it! Great job!")
            print("Here is a list of all your guesses:", pastGuesses)
            break
        elif userNum < secretNum:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

def main() -> None:
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a secret number between 1 and 10!")

    guessTheNumber()

if __name__ == "__main__":
    main()
