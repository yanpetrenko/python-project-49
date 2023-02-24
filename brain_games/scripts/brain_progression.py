from brain_games.logic import check
from brain_games.src.brain_progression_src import progression
import brain_games.cli


def rules():
    print("What number is missing in the progression?")


name = brain_games.cli.welcome_user()


def main():
    rules()
    check(progression, name)


if __name__ == '__main__':
    main()
