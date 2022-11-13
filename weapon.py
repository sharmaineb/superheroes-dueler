# polymorphism: allows us to use differnt implementations of the same method.

from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        random_value = random.randint(self.max_damage // 2, self.max_damage) # use integer division to find hald of the max_damage value
        return random_value # return a random integer between half of max_damage and max_damage
        # return super().attack()
