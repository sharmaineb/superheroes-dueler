import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name # assign the "name" and "max_damage"
        self.max_damage = max_damage

    def attack(self):
        random_value = random.randint(0, self.max_damage) # pick a random value between 0 and self.max_damage
        return random_value

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  ability = Ability("Debugging Ability", 20)
  print(ability.name)
  print(ability.attack())