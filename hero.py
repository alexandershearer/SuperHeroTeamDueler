import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        total_armor = 0
        for armor in self.armors:
            total_armor += armor.block()
        return damage_amt - total_armor
    
    def take_damage(self, damage):
        self.current_health -= self.defend(damage)
        print(f"{self.name} took {damage} damage and is now at {self.current_health}.")

    def is_alive(self):  
        if self.current_health <= 0:
            return False
        else:
            return True


    def fight(self, opponent):  
        if self.is_alive() is True:
            opponent.take_damage(self.attack())
        else:
            print(f"{self.name} has been defeated")
            return self.name
        if opponent.is_alive() is True:
            self.take_damage(opponent.attack())
        else:
            print(f"{self.name} has won!")
            return opponent.name
        self.fight(opponent)


if __name__ == "__main__":

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 2)
    ability4 = Ability("Wizard Beard", 2)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
