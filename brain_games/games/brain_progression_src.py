import random


def progression():
    question = []
    i = 0
    index = 0
    exponent = random.randint(1, 6)
    while i < 10:
        index += exponent
        question.append(index)
        i += 1
    index_random = random.randint(0, 9)
    answer_true = question[index_random]
    question[index_random] = '..'
    return [question, str(answer_true)]


def main():
    progression()


if __name__ == '__main__':
    main()
