from main import answer_logic, HORIZONTAL_LINE


def game(quiz):
    score = 0
    for question in quiz:  # for each question in the list, instead of repeating the code for each question
        print(question[0], f"\n{', '.join(question[1])}\nPlease enter a, b, c, or d")  # print the question
        if answer_logic(question[-1]):
            score += 1  # add to the score
        print(HORIZONTAL_LINE)
    print("Quiz complete!\nYour score was", score, "out of", len(quiz))  # print score out of total
