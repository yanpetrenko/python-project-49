import random


def prime():
    integer = random.randint(1, 101)
    counter = 0
    i = integer
    while i > 0:
        if integer % i == 0:
            counter += 1
        i -= 1
    if counter == 2:
        answer_true = 'yes'
    else:
        answer_true = 'no'
    return [integer, answer_true]


def main():
    prime()


if __name__ == '__main__':
    main()
