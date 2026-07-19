"""
duck_typing_example.py

This file demonstrates Duck Typing in Python.

Duck Typing means:
    "If an object behaves like what we need,
     we don't care what its actual type is."

Python focuses on behavior rather than inheritance.
"""

# ---------------------------------
# Three completely different classes
# ---------------------------------


class Duck:
    def speak(self):
        print("Duck: Quack!")


class Dog:
    def speak(self):
        print("Dog: Woof!")


class Robot:
    def speak(self):
        print("Robot: Beep Boop!")


# ---------------------------------
# Function using Duck Typing
# ---------------------------------


def make_it_speak(creature):
    """
    This function doesn't care what type
    the object actually is.

    It only assumes the object has
    a speak() method.
    """
    creature.speak()


print("=== Duck Typing ===")

duck = Duck()
dog = Dog()
robot = Robot()

make_it_speak(duck)
make_it_speak(dog)
make_it_speak(robot)


# ---------------------------------
# A class WITHOUT speak()
# ---------------------------------


class Cat:
    def meow(self):
        print("Meow!")


cat = Cat()

print("\n=== Error Example ===")

try:
    make_it_speak(cat)
except AttributeError as e:
    print("Error:", e)
