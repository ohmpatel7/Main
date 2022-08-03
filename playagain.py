def replay_game():
    while True:
        play_again = input("(yes/no)\n").lower().strip()
        if play_again == "yes":
            return True
        elif play_again == "no":
            return False
        else:
            print("Please enter a valid answer.")
