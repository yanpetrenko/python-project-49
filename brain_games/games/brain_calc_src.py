import random


def calc():
    operatorArr = ['+', '-', '*']
    operator = operatorArr[random.randint(0, 2)]
    a = random.randint(1, 15)
    b = random.randint(1, 15)
    question = f'{a} {operator} {b}'
    ansTrue = ''
    if operator == '+':
        ansTrue = a + b
    elif operator == '-':
        ansTrue = a - b
    else:
        ansTrue = a * b
    return [question, str(ansTrue)]


def main():
    calc()


if __name__ == '__main__':
    main()
