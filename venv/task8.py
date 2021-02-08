stop = False

while(not stop):

    answerP1 = input('Player 1: Please type your choice: Rock, Paper or Scissors:')

    answerP2 = input('Player 2: Please type your choice: Rock, Paper or Scissors:')

    if answerP1 == answerP2:
        print('DRAW GAME')
    elif answerP1 == 'Rock' and answerP2 == 'Paper':
        print('PLAYER 2 WINS')
    elif answerP1 == 'Rock' and answerP2 == 'Scissors':
        print('PLAYER 1 WINS')
    elif answerP1 == 'Paper' and answerP2 == 'Rock':
        print('PLAYER 1 WINS')
    elif answerP1 == 'Paper' and answerP2 == 'Scissors':
        print('PLAYER 2 WINS')
    elif answerP1 == 'Scissors' and answerP2 == 'Rock':
        print('PLAYER 2 WINS')
    elif answerP1 == 'Scissors' and answerP2 == 'Paper':
        print('PLAYER 1 WINS')
    else:
        print('Wrong answer, please type Rock, Paper or Scissors in your next attempt!')


    answer = input('Do you want to start a new game? (Yes/No)')

    if answer == 'Yes':
        print('New game will start')
    elif answer == 'No':
        stop = True
        print('Game over')
