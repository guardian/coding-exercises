import itertools
from bag import flatten

def letters_from(hand):
    return [tile[0] for tile in hand]

def variations(hand):
    return flatten([[p for p in itertools.permutations(letters_from(hand), r)] for r in range(2, 8)])


def potential_words(hand):
    return ["".join(cs) for cs in variations(hand)]
