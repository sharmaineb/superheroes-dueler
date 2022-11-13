# dog.py
class Dog: 
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    # methods are defined as their own named functions inside that class
    # remember to put the "self" parameter every time we make a class method!
    def bark(self):
        print("Woof!")

    # method to have dogs sit
    def sit(self):
        print(f"{self.name} sits")

    # method to have dogs roll over
    def roll_over(self):
        print(f"{self.name} rolls over")


# instantiation call that creates a Dog object:
# Dog("Rex")
# the same instantiation call that creates a Dog Object
# we've assigned it to the value of the my_dog variable
# my_dog = Dog("Rex", "Superdog")
# print(my_dog)
# print(my_dog.name)
# print(my_dog.breed)
# my_dog.bark()