def load_questions_from_file(file_name):
    """
    Load questions from a file.
    """
    with open(file_name, 'r',) as file:
        for line in file:
            entry = line.split(' ! ')
            if entry[-1].endswith('\n'):
                entry[-1] = entry[-1][:-1]
            if entry[-1].endswith('\r'):
                entry[-1] = entry[-1][:-1]
            options = entry[1].split(", ")
            answers = entry[2].split(", ")
            try:
                elements.append([entry[0], options, answers])
            except (NameError, UnboundLocalError):
                elements: list = [[entry[0], options, answers]]
    return elements
