#Number Game

import random
num =  random.randint(1,50)
print("The computer has chosen a number between 1 and 100 (including both). Now it’s your turn to guess the number -")
turns = 0

while True:
    guess = int(input("Enter your guessed number:"))
    if (guess==num):
        print("Yay! you guessed it correct")
        turns +=1
        break
    elif(guess<num):
        print("Wrong guess! Try a bigger number.")
        turns +=1
    elif(guess>num):
        print("Wrong guess! Try a smaller number.")
        turns +=1

print("Total attempts = ",turns)