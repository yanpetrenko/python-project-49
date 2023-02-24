def check(func, name):
    counter = 0
    mass = [0, 1, 2]
    for counter in mass:
        [question, answer] = func()
        print(f'Question: {question}')
        print('Your answer: ')
        ans_user = input()
        wrong = f'{ans_user} is wrong answer ;(. Correct answer was {answer}.'
        again = f"Let's try again, {name}!"
        if ans_user == answer:
            print('Correct!')
        else:
            print(wrong)
            print(again)
            break
        counter += 1
        if counter == 3:
            return print(f'Congratulations, {name}!')
        else:
            continue
