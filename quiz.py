from datetime import time


def load_questions_from_file():
    pass


def game():
    pass


def replay_game():
    pass


def list_shuffler():
    pass


def main(HORIZONTAL_LINE=None):
    """
    Main function.
    """
    load_questions_from_file()
    playing = True
    while playing:
        print("Hey there!\n")
        name = input("What is your name?\n").capitalize()  # This to ask the end users name.
        print("Hey " + name + "!\n")  # Prints hey and the users name.
        time.sleep(1)
        print(
            "Welcome to my Zero Hunger Quiz" + " " + name + "!\n")  # Welcomes the user and prints
        # their name.
        time.sleep(1)
        game()  # Starts the quiz.
        print(HORIZONTAL_LINE)
        print("Would you like to play again?\n")  # play again logic
        if replay_game():
            print("Coming right up!")
            list_shuffler()
        else:
            print("Thanks for playing!")
            exit()
