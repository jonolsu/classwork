import random

print('-------------------------------------')
print('       Guess that number game')
print('-------------------------------------')
print()

the_number = random.randint(0,100)

guess = -1
name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {1}, Your guess of {0} was too low'.format(guess, name))
    elif guess > the_number:
        print('Sorry {}, Your guess of {} was too high'.format(name, guess))
    else:
        print('you win!')

print('done')