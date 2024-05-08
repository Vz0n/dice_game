# Just a function that simulates a "20-sided dice"
import random
from math import ceil

def dice_roll() -> int:
    return ceil(random.randrange(1, 20))
