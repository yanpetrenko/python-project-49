#!/usr/bin/env python3
from brain_games.logic import check
from brain_games.games.brain_prime_src import prime
import brain_games.cli


def rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


name = brain_games.cli.welcome_user()


def main():
    rules()
    check(prime, name)


if __name__ == '__main__':
    main()
