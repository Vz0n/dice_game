# Skeleton class for classes
class CharacterClass:
    def __init__(self, attack, health, defense):
        self.attack = attack
        self.health = health
        self.defense = defense
        self.critical = 0.50 * attack 

    # Get class name using python internal attributes.
    def __str__(self):
        return self.__class__.__name__

class Warrior(CharacterClass):

    def __init__(self, sword_sharpness = 1.5):
        # Default attributes for Warrior class 
        self.sword_sharpness = sword_sharpness
        super().__init__(15 + sword_sharpness, 100, 16)

    def get_sharpness(self):
        return self.sword_sharpness

class Wizard(CharacterClass):
    def __init__(self, mana = 1):
        # Default attributes for Wizard class
        self.mana = mana
        super().__init__(20 + mana, 100, 25)

    def get_mana(self):
        return self.mana
