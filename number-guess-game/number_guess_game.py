from random import randint
import string
import time

# constants
LOWEST_NUMBER = 1


#  -- Define and validate user name --

def get_username():
    return input('Please enter a username! ')

def validate_username():
    """This function cleans the user name. rejects if it contains invalid characters - anything other
    that letters, digits and underscores """
    print('Username can contain only letters, numbers and underscores.')

    allowed = string.ascii_letters + string.digits + '_'
    while True:
        raw_username = get_username()
        cln_username = raw_username.strip().lower()
        if not cln_username:
            print('Please enter a username!')
            continue
        elif len(cln_username) < 4 or len(cln_username) > 20:
            print('Username is too short/long!')
            continue
        elif not all(char in allowed for char in cln_username):
            print('Username contains invalid characters!')
            continue
        else:
            return cln_username


# User chooses game difficulty based on the number range
# 30 - easy mode; 50 - medium; 100 - hard mode.


def get_difficulty():
    return input('Please enter maximum number - 30, 50, 100 ')

def validate_difficulty():
    """This function validates the highest number from given range
     (rejects unwanted characters of numbers)
     and returns the highest number."""

    while True:
        highest_number = get_difficulty()
        if highest_number.strip() not in ['30', '50', '100']:
            print('Please enter valid number either 30, 50 or 100!')
            continue
        else:
            highest_number = int(highest_number)
            return highest_number


def generate_number(maximum):
    return randint(LOWEST_NUMBER, maximum)

def award_points(maximum_number):
    award = 0
    if maximum_number == 30:
        award = 5
    elif maximum_number == 50:
        award = 10
    elif maximum_number == 100:
        award = 20
    return award

def deduct_points(maximum_number):
    deduct = 0
    if maximum_number == 30:
        deduct = 2
    elif maximum_number == 50:
        deduct = 3
    elif maximum_number == 100:
        deduct = 8
    return deduct

def start_game():
    """This function starts the game. It generates a random number and asks user to guess it.
     It also counts points, the number of attempts and gives feedback to user."""
    pass




# program runs here
def rules(user):
    """Rules of games. This function explains what players can do."""

    print(f'''Welcome {user} to the Number Guessing Game!
                          Here are rules😁
          • First, you must choose the game difficulty level.
          • 30 - easy mode; 50 - medium; 100 - hard mode.
          • Then, you will have to guess the number that the game will generate.
          • You will get points for each correct guess and lose points for each wrong guess.
          • The points you get or lose depend on the difficulty level you choose.
          • Rewards: easy mode +5 points, medium mode +10 points, hard mode +20 points.
          • Penalties: easy mode -2 points, medium mode -3 points, hard mode -8 points.
        =======================================================================================
                                        GOOD LUCK! 🍀

    ''')


def main():
    user = validate_username()
    maximum_number = validate_difficulty()
    rules(user)
    start_game()


if __name__ == '__main__':
    main()



