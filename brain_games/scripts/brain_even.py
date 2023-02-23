from brain_games.logic import check
from brain_games.src.brain_even_src import even
import brain_games.cli


def rules():
    print("Answer 'yes' if the number  is even, otherwise answer 'no'.")


name = brain_games.cli.welcome_user()


def main():
    rules()
    check(even, name)


if __name__ == '__main__':
    main()