def check(func, name):
    counter = 0
    mass = [0, 1, 2]
    for counter in mass:
        [question, answer] = func()
        print(f'Question: {question}')
        print('Your answer: ')
        answerUser = input()
        if answerUser == answer:
            print('Correct!')
        else:
            print(f'{answerUser} is wrong answer ;(. Correct answer was {answer}.')
            break
        counter += 1
        if counter == 3:
            return print(f'Congratulations, {name}!')
        else:
            continue
