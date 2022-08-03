import time
import random

HORIZONTAL_LINE = "-" * 80  # constant for horizontal line


def replay_game():  # Allows the user to replay the game if answered "yes"
    while True:
        play_again = input("(yes/no)\n").lower().strip()
        # asks to replay the game, also making answer lowercase
        if play_again == "yes":  # yes means the code will run again
            return True
        elif play_again == "no":  # no means it will end the code with an outro
            return False
        else:
            print(
                "Please enter a valid answer.")  # if typed something other than yes/no then user asked for a vaild
            # answer

def answer_logic(correct_answer):  # This def allows users to enter full written answers
    user_answer = input("Your answer: ").lower().strip()  # ask the user for their answer
    if user_answer in [element.lower() for element in correct_answer]:  # if the user answer matches the one in the list
        print("Correct!")
        return True
    else:
        print("Wrong answer! The correct answer was", ", ".join(correct_answer))  # if wrong, show the answer
        return False


def game(quiz, HORIZONTAL_LINE=None):
    score = 0
    for question in quiz:  # for each question in the list, instead of repeating the code for each question
        print(question[0],
              "\n{', '.join(question[1])}\nPlease enter a, b, c, or d")  # print the question
        if answer_logic(question[-1]):
            score += 1  # add to the score
        print(HORIZONTAL_LINE)
    print("Quiz complete!\nYour score was", score, "out of", len(quiz))  # print score out of total


def load_questions_from_file(file_name, elements=None):  # This def allows to load the questions from the selected imported file
    """
    Load questions from a file.
    """
    with open(file_name, 'r', ) as file:  # return carriage resets position to a new line
        for line in file:  # utf8 is a format the python can read(the encoding)
            entry = line.split(' ! ')
            if entry[-1].endswith(
                    '\n'):  # Endswitch is there for when a new line has been created
                entry[-1] = entry[-1][:-1]  # -1 is last item in a list
            if entry[-1].endswith('\r'):
                entry[-1] = entry[-1][:-1]
            options = entry[1].split(", ")  # splitting sepreates into strings in the list
            answers = entry[2].split(", ")
            try:
                elements.append([entry[0], options, answers])
            except (NameError, UnboundLocalError):  # errors that appear when a object hasn't been created
                elements: [[entry[0], options, answers]]
    return elements


def list_shuffler(list_to_shuffle):  # When user replays game, questions are reshuffled in a random order
    """
    Randomise the questions on replay.
    """
    random.shuffle(list_to_shuffle)
    return list_to_shuffle


def main(HORIZONTAL_LINE=None):  # main into and outro
    """
    Main function.
    """
    quiz_questions = load_questions_from_file("questions.txt")  # this loads questions from a selected file
    playing = True
    while playing:
        print("Hey there!\n")  # Welcomes users
        name = input("What is your name?\n").capitalize()  # This to ask the end users name.
        print("Hey " + name + "!\n")  # Prints hey and the users name.
        time.sleep(1)  # A pause for 1 second
        print(
            "Welcome to my Zero Hunger Quiz" + " " + name + "!\n")  # Welcomes the user and prints
        # their name.
        time.sleep(1)  # A pause for 1 second
        game(quiz_questions)  # Starts the quiz.
        print(HORIZONTAL_LINE)
        print("Would you like to play again?\n")  # play again logic
        if replay_game():  # if yes then code re runs code with questions randomised
            print("Coming right up!")
            list_shuffler(quiz_questions)
        else:
            print("Thanks for playing!")  # If no then code runs a outro
            exit()


if __name__ == "__main__":
    main()
