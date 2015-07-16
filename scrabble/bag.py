import random

default_distribution =[
    (1, 'E', 12),
    (1, 'A', 9),
    (2, 'D', 4),
    (10, 'Q', 1),
    (10, 'Z', 1),
]

def create_tiles(distribution):
    value = distribution[0]
    letter = distribution[1]
    return [(letter, value) for i in range(0, distribution[2])]

def flatten(tiles):
    return [item for sublist in tiles for item in sublist]

def create_game_bag(distribution=None):
    if not distribution:
        distribution = default_distribution
    a_bag = flatten([create_tiles(d) for d in distribution])
    random.shuffle(a_bag)
    return a_bag
