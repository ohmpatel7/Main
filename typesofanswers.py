def answer_logic(correct_answer):
    user_answer = input("Your answer: ").lower().strip()  # ask the user for their answer
    if user_answer in [element.lower() for element in correct_answer]:  # if the user answer matches the one in the list
        print("Correct!")
        return True
    else:
        print("Wrong answer! The correct answer was", ", ".join(correct_answer))  # if wrong, show the answer
        return False
