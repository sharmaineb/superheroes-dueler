import random

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name # we know the name of our hero, so we assign it here
        self.starting_health = starting_health # similarly, our starting health is passed in, just like name
        self.current_health = starting_health # always the same as their starting heatlh (no damage taken yet!)

    def fight(self, opponent):
        winner = random.randint(0, 1)
        if winner == 0:
            print(f"{opponent.name} wins!")
        else:
            print(f"{self.name} wins!")






# if __name__ == "__main__":
#   # If you run this file from the terminal
#   # this block is executed.
#   my_hero = Hero("Grace Hopper", 200)
#   print(my_hero.name)
#   print(my_hero.current_health)
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman", 300)
    hero2 = Hero("Dumbledore", 250)

    hero1.fight(hero2)