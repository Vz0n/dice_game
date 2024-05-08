# Just a function that simulate a 20-sided dice in a... strange way
import random
from math import ceil

def dice_roll() -> int:
    return ceil(random.randrange(1, 20))
