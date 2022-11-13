# my_dogs.py
from dog import Dog # we need to specify exactly what we want

my_dog = Dog("Rex", "SuperDog")

my_other_dog = Dog("Annie", "SuperDog")
print(my_other_dog.name)

shars_dog = Dog("Pogie", "Pug")

print(my_dog.name)
print(my_dog.breed)
print(my_other_dog.name)
print(my_other_dog.breed)
print(shars_dog.name)
print(shars_dog.breed)
my_dog.bark
my_other_dog.sit
shars_dog.roll_over()