from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        # create instance variables named team_one and team_two that
        # will hold out teams
        self.team_one: Team("team_one")
        self.team_two: Team("team_two")

    def create_ability(self):
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")
        
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the name of the weapon? ")
        max_damage = input("What is the max damage of the weapon? ")
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the name of your armor?")
        max_block = input("What is the defense of the armor? ")
        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero
    
    # build_team_one is provided to you

    def build_team_one(self):
        numOfTeamMembers = int(input("How many members would you like on Team One?\n")) # Prompt the user for the number of Heroes on team one
        for i in range(numOfTeamMembers): # call self.create_hero() for every hero that the user wants to add to team one.
            hero = self.create_hero()
            self.team_one.add_hero(hero) # Add the created hero to team one.

    def build_team_two(self):
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n")) # Prompt the user for the number of Heroes on team two
        for i in range(numOfTeamMembers): # call self.create_hero() for every hero that the user wants to add to team two.
            hero = self.create_hero()
            self.team_two.add_hero(hero) # Add the created hero to team two.

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        # TODO: Now display the average K/D for Team Two
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))

        # Here is a way to list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        #TODO: Now list the heroes from Team Two that survived
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

# if __name__ == "__main__":
#     arena = Arena()
#     arena.build_team_one()
#     arena.build_team_two()
#     arena.team_battle()
#     arena.show_stats()



