import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health = 100):
        self.abilities = list()
        self.armors = list()
        self.name = name # we know the name of our hero, so we assign it here
        self.starting_health = starting_health # similarly, our starting health is passed in, just like name
        self.current_health = starting_health # always the same as their starting heatlh (no damage taken yet!)

    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0: # check if at least one hero has abilities. if no hero has abilites, print "Draw"
            print("Draw!")
        else: # else, start the fighting loop until a hero has won
            while self.is_alive() > 0 and opponent.current_health > 0:
                total_damage = self.attack() # the hero (self) and their opponent must attack each other and each must take damage from the other's attack
                opponent.take_damage(total_damage)
                if opponent.is_alive() == True: # after each attack, check if either the hero (self) or the opponent is alive
                    total_damage = opponent.attack()
                    self.take_damage(total_damage)
                    if self.is_alive() == True:
                        total_damage = total_damage(self.attack)
                        opponent.take_damage(total_damage)
                    else:
                        print(f"{opponent.name} won!")
                elif opponent.is_alive() == False: # check if one of them has died, print "heroName won!" replacing heroName with the name of the hero, and end the fight loop
                    return print(f"{self.name} won!")


    def add_ability(self, ability):
        self.abilities.append(ability) # we use the append method to add ability objects to our list
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_damage = 0 # start our total at 0
        for ability in self.abilities: # loop through all of our hero's abilites
            total_damage += ability.attack() # add the damage of each attack to our running total
        return total_damage # return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.attack()
        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        self.current_health -= damage - defense

    def is_alive(self): # check the current health of the hero
        if self.current_health <= 0: # if it is <=0, then return False. Otherwise, they stll have health
            return False
        else:
            return True # and are therfore alive, so return True


# define an ability and a weapon
# both have the same max damage
eye_rays = Ability('Eye Rays', 50)
laser_blast = Weapon('Laser Blast', 50)

# Let's put these in an array together
# This list contains different types: Ability and Weapon
powers = [eye_rays, laser_blast]

# We know that all Abilities and Weapons share the same attribute
for power in powers:
  print(power.max_damage)

# We know that all Abilities and Weapns implement the attack method
for power in powers:
  print(power.attack())

# Note! While both implement attack() a Weapon will always return 
# a higher average damage!










if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)
# if __name__ == "__main__":
#   # If you run this file from the terminal
#   # this block is executed.
#   my_hero = Hero("Grace Hopper", 200)
#   print(my_hero.name)
#   print(my_hero.current_health)
# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     print(hero.current_health)
    # If you run this file from the terminal
    # this block is executed.
    # hero1 = Hero("Wonder Woman", 300)
    # hero2 = Hero("Dumbledore", 250)

    # hero1.fight(hero2)
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())