#!/usr/bin/python3

from classes import Wizard, Warrior
from character import Character
from game_actions import fight
from random import randrange

def get_random_name() -> str:
    try:
        lines = open("./names.txt", "r").readlines()
        return lines[randrange(0, len(lines) - 1)].strip("\n") # Strip and omit new line character(s).
    except OSError:
        print("Please create a file called names.txt with some character names.")
        exit(1)

def create_random_characters() -> list[Character]:
    name1 = get_random_name()
    name2 = get_random_name()
    
    # A bit of recursivity doesn't do bad... *halts on stack overflow*
    if name1 == name2:
        return create_random_characters()

    c1 = Character(name1, Wizard(5))
    c2 = Character(name2, Warrior(5))

    return [c1, c2]


if __name__ == "__main__":
    print("A simple game test")

    players = create_random_characters()
    result = fight(players[0], players[1])
    
    for n, player in enumerate(players):
        print("\n\n")
        print(f"Summary for {player.name}")
        print(f"Attack damage: {player.get_attack()}")
        print(f"Critical damage: {player.get_critical()}")
        print(f"Defense: {player.get_defense()}")
        print(f"Health: {result[n]}")
        print(f"Class: {player.role_class}")


