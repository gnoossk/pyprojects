def new_game():
    guesses = list()
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print( '---------------------------')
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input('Enter A,B,C or D:')
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num +=1
    display_score(correct_guesses, guesses)


def check_answer(answer,guess):
    if answer == guess:
        print('correct!')
        return 1
    else:
        print('wrong!')
        return 0
def display_score(correct_guesses,guesses):
    print('---------------')
    print('results')
    print('---------------')

    print('Answers: ',end ='')
    for i in questions:
        print(questions.get(i), end =' ')
    print()

    print('Guesses: ', end='')
    for i in guesses:
        print(i, end=' ')
    print()

    score = int((correct_guesses/len(questions)*100))
    print('your score is: ' +str(score)+'%')

def play_again():
    response = input('do you want to play again? (y/n): ')
    response = response.upper()

    if response == 'YES':
        return True
    else:
        return False


questions = {
    'Who created python?:': 'A',
    'What year was Python created?:': 'B',
    'Python is attributed to which comedy group?:': 'C',
    'Is the Earth round?: ': 'A'
}

options = [['A. Guido van Rossum', 'B. Me', 'C. Bill gats', 'D. penguzin0'],
          ['A.1989','B.1991','C:2000','D:2016'],
          ['A. Lonely island','B. Smosh','C. Monty Python and the holy grail','D.SNL'],
          ['A.False','B.True','C.maybe','D.its a turtle']]
new_game()

while play_again():
    new_game()

print('See you next time')
