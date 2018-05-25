import random

print('----------------------')
print('GUESS THAT NUMBER GAME')
print('----------------------')
print()

name = input('What is your name? ')
the_number = random.randint(0, 100)
guess = -1

while guess != the_number:

    guess_text = input('Guess the number ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {} , your guess of {} was too low.' .format(name, guess))
    elif guess > the_number:
        print('Sorry {} , your guess of {} was too high.'.format(name, guess))
    else:
        print('You win')
print('Done')



