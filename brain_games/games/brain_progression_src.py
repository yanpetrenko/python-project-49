import random


def progression():
    question = []
    i = 0
    ind = 0
    exp = random.randint(1, 6)
    while i < 10:
        ind += exp
        question.append(ind)
        i += 1
    indRand = random.randint(0, 9)
    ansTrue = question[indRand]
    question[indRand] = '..'
    return [question, str(ansTrue)]


def main():
    progression()


if __name__ == '__main__':
    main()
