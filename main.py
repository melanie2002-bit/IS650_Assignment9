import random

def chooseDifficulty() -> tuple[str, int]:
    difficultyRanges: dict[str, int] = {"easy": 10, "medium": 15, "hard": 20}

    while True:
        difficulty: str = input("Choose a difficulty (easy, medium, or hard): ").strip().lower()
        if difficulty in difficultyRanges:
            return difficulty, difficultyRanges[difficulty]
        print("Please choose easy, medium, or hard.")

def guessTheNumber(maxNumber: int) -> None:
    secretNum: int = random.randint(1, maxNumber)
    pastGuesses: list[int] = []
    rightGuesses: bool = False
    userPoints: int = 0

    while not rightGuesses:
        try:
            userNum: int = int(input(f"Pick a number between 1 and {maxNumber}: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= userNum <= maxNumber:
            print(f"Your guess must be between 1 and {maxNumber}.")
            continue

        pastGuesses.append(userNum)

        if userNum == secretNum:
            print("You got it! Great job!")

            if len(pastGuesses) == 1:
                userPoints = 5
            elif len(pastGuesses) == 2 or len(pastGuesses) == 3 or len(pastGuesses) == 4:
                userPoints = 3
            else:
                userPoints = 1        
            print("Great job! You have earned", userPoints, "points.")
            print("Here is a list of all your guesses:", pastGuesses)
            break
        elif userNum < secretNum:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

def main() -> None:
    print("Welcome to the Number Guessing Game!")
    difficulty, maxNumber = chooseDifficulty()
    print(f"I have chosen a secret number between 1 and {maxNumber} for {difficulty} mode!")

    guessTheNumber(maxNumber)

if __name__ == "__main__":
    main()
