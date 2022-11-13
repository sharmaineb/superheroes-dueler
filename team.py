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