from character import Character
from utils import dice_roll

# Do a fight and return the health of both characters fighting.
def fight(fighter1: Character, fighter2: Character, dice_number = dice_roll()) -> list[int]:
    f1_attack = fighter1.get_attack() + (fighter1.get_critical() * dice_number)
    f2_attack = fighter2.get_attack() + (fighter2.get_critical() * dice_number)
    f1_total_h = fighter1.get_health() + fighter1.get_defense()
    f2_total_h = fighter2.get_health() + fighter1.get_defense()
    
    m1 = f1_total_h - f2_attack
    print(f"{fighter1.name} has received {f2_attack} of damage!")

    if m1 < 1:
        print(f"{fighter1.name} has died in hands of {fighter2.name}...")
        return [m1, f2_total_h]

    m2 = f2_total_h - f1_attack
    print(f"{fighter2.name} has received {f1_attack} of damage!")

    if m2 < 1:
        print(f"{fighter2.name} has died...")
    else:
        print("Both survived!")

    # If both survived, just return their remaining health.
    return [m1,m2]
