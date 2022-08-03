from random import random


def list_shuffler(list_to_shuffle):
    """
    Randomise the questions on replay.
    """
    random.shuffle(list_to_shuffle)
    return list_to_shuffle
