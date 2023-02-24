import random


def gcd():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    question = f'{a} {b}'
    i = a
    ansTrue = ''
    if a >= b:
        i = b
    while i > 0:
        if a % i == 0 and b % i == 0:
            ansTrue = i
            break
        i -= 1
    return [question, str(ansTrue)]



def main():
    gcd()


if __name__ == '__main__':
    main()
