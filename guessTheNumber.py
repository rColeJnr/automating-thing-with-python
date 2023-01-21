import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

for guesesTaken in range(1, 7):
    print ('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('go higher')
    elif guess > secretNumber:
        print('go lower')
    else: break 

if guess == secretNumber:
    print(f"Good job! you guessed the number in {guessesTaken} guesses!")
else: print (f'The number was {secretNumber}')
