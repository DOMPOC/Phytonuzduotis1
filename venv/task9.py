import random

rNumber = random.randint(1,9)
count = 0

while(True):
    guessNumber = input("Please, type your guess number or 'exit' to stop the game:")

    if guessNumber == 'exit':
        print('Thanks for playing!')
        break

    elif rNumber == int(guessNumber):
        count += 1
        print("Congratulations! You have type {} and the random number is {}".format(guessNumber, rNumber))
        break
    elif int(guessNumber) > rNumber:
        count += 1
        count = 0
        print("Error! Your guess number {} is too high, please try a smaller number".format(guessNumber))

    else:
        count += 1
        print("Error! Your guess number {} is too low, please try a higher number".format(guessNumber))

    print('You have typed {} guesses'.format(count))
    print('The random number was {}'.format(rNumber))