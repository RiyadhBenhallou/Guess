from random import randint
from art import logo

number = randint(1, 100)

print(logo)


def set_difficulty():
    answer = input("Do you want the easy or hard level: ")
    if answer == 'easy':
        return 10
    else:
        return 5

attempts = set_difficulty()
print(attempts)
print("I'm thinking of a number between 1 and 100")

while attempts > 0:
    print(f"You have {attempts} attempts left")
    guess = int(input("Make a guess: "))
    if guess == number:
        print("Congratulations! You have won.")
        break
    elif guess > number:
        print("Too high")
        attempts -= 1
    elif guess < number:
        print("Too low")
        attempts -= 1

if attempts == 0:
    print(f"Sorry, you've run out of attempts. The number was {number}.")
