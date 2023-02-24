from brain_games.logic import check
from brain_games.games.brain_calc_src import calc
import brain_games.cli


def rules():
    print("What is the result of the expression?")


name = brain_games.cli.welcome_user()


def main():
    rules()
    check(calc, name)


if __name__ == '__main__':
    main()
