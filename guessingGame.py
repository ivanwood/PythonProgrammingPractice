#01/17/21
#This is a guessing game that asks the user for a number and then outputs the correct guess to the user
import random                           #import random varible
import time

print("Welcome. This game will ask you to guess a number between 1 -100.")
time.sleep(2)
print("Picking a number....")
time.sleep(2)
guess = int(input("What is your guess?: ")) #ask for number from user. Make it an int.
corret_num = random.randint(1,100)          #this is the correct guess generated from the random varable
guess_count = 0                             #counts how many times users guesses


#while loop (if + for loop)
#"runs until the guess is equal to the correct number
while guess != corret_num:                  #will run until the guess is correct. True if operand is not equal.
    time.sleep(1)
    guess_count += 1
    if guess < corret_num:
        guess = int(input("Guess higher: "))
    else:
        guess = int(input("Guess lower: "))

#prints if the guess is corect
print(f"Congrats! The correct number was {corret_num}! It took you {guess_count} guesses. Thanks for playing.")