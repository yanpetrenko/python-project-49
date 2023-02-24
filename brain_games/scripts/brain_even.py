#!/usr/bin/env python3
from brain_games.logic import check
from brain_games.games.brain_even_src import even
import brain_games.cli


def rules():
    print('Answer "yes" if the number  is even, otherwise answer "no".')


name = brain_games.cli.welcome_user()


def main():
    rules()
    check(even, name)


if __name__ == '__main__':
    main()
