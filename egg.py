import random

def guess_the_number():
    number = random.randint(1, 20)
    attempts = 0

    print("Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 20.")

    while True:
        guess = input("Take a guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
