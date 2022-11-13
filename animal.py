# inheritance
# inheritance allows for additional ways to reuse code

class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating!")

    def drink(self):
        print(f"{self.name} is drinking!")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping!")

puppy = Animal("Taro")
print(puppy.eat())
print(puppy.drink())

frog = Frog("Kermit")
print(frog.eat())
print(frog.drink())
print(frog.jump())