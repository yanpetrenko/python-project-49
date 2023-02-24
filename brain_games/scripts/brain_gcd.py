from brain_games.logic import check
from brain_games.games.brain_gcd_src import gcd
import brain_games.cli


def rules():
    print("Find the greatest common divisor of given numbers.")


name = brain_games.cli.welcome_user()


def main():
    rules()
    check(gcd, name)


if __name__ == '__main__':
    main()
