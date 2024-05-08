from classes import CharacterClass

class Character:
    def __init__(self, name, role_class: CharacterClass):
        self.name = name 
        self.role_class = role_class
    
    def get_health(self):
        return self.role_class.health
    
    def get_attack(self):
        return self.role_class.attack

    def get_defense(self):
        return self.role_class.defense

    def get_critical(self):
        return self.role_class.critical

    def say_hello(self):
        print(f"Hello! my name is {self.name} and i'm a {self.role_class}")
