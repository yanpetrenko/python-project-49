import random


def even():
    quest = random.randint(1, 20)
    answer_true = ''
    if quest % 2 > 0:
        answer_true = 'no'
    else:
        answer_true = 'yes'
    return [quest, answer_true]


def main():
    even()


if __name__ == '__main__':
    main()
