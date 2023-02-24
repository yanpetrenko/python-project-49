import random


def calc():
    operator_array = ['+', '-', '*']
    operator = operator_array[random.randint(0, 2)]
    a = random.randint(1, 15)
    b = random.randint(1, 15)
    question = f'{a} {operator} {b}'
    answer_true = ''
    if operator == '+':
        answer_true = a + b
    elif operator == '-':
        answer_true = a - b
    else:
        answer_true = a * b
    return [question, str(answer_true)]


def main():
    calc()


if __name__ == '__main__':
    main()
