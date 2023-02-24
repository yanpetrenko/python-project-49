import random


def even():
    quest = random.randint(1, 20)
    ansTrue = ''
    if quest % 2 > 0:
        ansTrue = 'no'
    else:
        ansTrue = 'yes'
    return [quest, ansTrue]


def main():
    even()


if __name__ == '__main__':
    main()
