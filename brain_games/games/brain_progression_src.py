import random


def progression():
    list = []
    i = 0
    index = 0
    exponent = random.randint(1, 6)
    while i < 10:
        index += exponent
        list.append(index)
        i += 1
    index_random = random.randint(0, 9)
    answer_true = list[index_random]
    list[index_random] = ".."
    question = str(list).replace("'",'').replace(",",'')
    return [str(question)[1:-1:], str(answer_true)]


def main():
    progression()


if __name__ == '__main__':
    main()
