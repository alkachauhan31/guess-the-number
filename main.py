#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number of a number between 1 and 100")
answer=random.randint(1,100)
print(f"The correct answer is {answer}")
choice=input("choose a difficulty type if for 'easy' type  easy and for 'hard' type hard :  ").lower()
def easy_mode():
  attempt=10
  print(f"your have {attempt} attempt remaining to guess the number")
  while attempt>=1:
    guess=int(input("make a guess:"))
    if guess == answer:
      print("Hurry! you win the Game!!!!!!")
    elif guess > answer:
      print("Too high \nGuess again")
      attempt-=1
      print(f"your have {attempt} attempt remaining to guess the number")
      if attempt==0:
        print("you loose the game!")
    elif guess < answer:
      print("Too low \nGuess again")
      attempt-=1
      print(f"your have {attempt} attempt remaining to guess the number")
      if attempt==0:
        print("you loose the game!")
    else:
      print("Plzz enter number between 1 and 100!!!!!")

def hard_mode():
  attempt=5
  print(f"your have {attempt} attempt remaining to guess the number")
  while attempt >=1:
    guess=int(input("make a guess:"))
    if guess == answer:
      print("Hurry! you win the Game!!!!!!")
    elif guess > answer:
      print("Too high \nGuess again")
      attempt-=1
      print(f"your have {attempt} attempt remaining to guess the number")
      if attempt==0:
        print("you loose the game!")
    elif guess < answer:
      print("Too low \nGuess again")
      attempt-=1
      print(f"your have {attempt} attempt remaining to guess the number")
      if attempt==0:
        print("you loose the game!")
    else:
      print("Plzz enter number between 1 and 100!!!!!")

if choice=="easy":
  easy_mode()
elif choice=="hard":
  hard_mode()

      