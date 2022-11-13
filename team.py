import random

class Team:
    def __init__(self, name): # initialize your team with its team name and an empty list of heroes
        self.name = name
        self.heroes = list()

    # remove a hero from the team
    def remove_hero(self, name):
        found_hero = False
        for hero in self.heroes: # loop through each hero in our list
            if hero.name == name: 
                self.heroes.remove(hero) # if we find them, remove them from the list
                found_hero = True # set our indicator to True
        if not found_hero: # if we looped through our list and did not find our hero
            return 0 # the indicator would have never changed, so return 0

    def view_all_heroes(self):
        for hero in self.heroes: # loop over the list of heroes and print their names to the terminal one by one
            print(hero.name) # print their names to the terminal one by one

    def add_hero(self, hero):
        self.heroes.append(hero) # add the hero object that is passed in to the list of heroes in self.heroes

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths: {kd}")

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health # set the hero's current_health to their starting_health

    def attack(self, other_team): # battle each team against each other
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero = random.choice(living_heroes) # randomly select a living hero from each team
            opponent = random.choice(living_opponents)
            hero.fight(opponent) # have the heroes fight each other
            
            # update the list of living_heroes and living_opponents
            # to reflect the result of the fight
            if hero.is_alive() == True:
                living_opponents.remove(opponent)
            else:
                living_heroes.remove(hero) 
