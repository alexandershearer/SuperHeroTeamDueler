import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        print(f"{weapon.name} has been added to {self.name}'s arsenal of abilities.")

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:

        hero = random.choice(living_heroes)
        opponent = random.choice(living_opponents)

        loser = hero.fight(opponent)

        for hero in living_heroes:
            if loser == hero.name:
                living_heroes.remove(hero)
        
        for opponent in living_opponents:
            if loser == opponent.name:
                living_opponents.remove(opponent)

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

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths


    def fight(self, opponent):  
        if self.is_alive() is True:
            opponent.take_damage(self.attack())
        else:
            opponent.add_kill(1)
            self.add_death(1) 
            print(f"{self.name} has been defeated")
            return self.name
        if opponent.is_alive() is True:
            self.take_damage(opponent.attack())
        else:
            opponent.add_death(1)
            self.add_kill(1)
            print(f"{self.name} has won!")
            return opponent.name
        self.fight(opponent)


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
