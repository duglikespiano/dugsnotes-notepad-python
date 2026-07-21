"""
==========================================
Python Dunder (Magic) Methods Explained
==========================================

A dunder method (Double UNDERscore) is a special
method that Python automatically calls when
certain operations happen.

Examples:

__init__      -> object creation
__str__       -> print(object)
__len__       -> len(object)
__add__       -> object1 + object2
__getitem__   -> object[index]
__eq__        -> object1 == object2

Instead of calling these directly,
Python calls them automatically.
"""


class Backpack:
    """
    A simple backpack class.
    """

    def __init__(self, owner):
        """
        Called automatically when creating an object.
        """
        self.owner = owner
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        """
        Called by print(object)
        """
        return f"{self.owner}'s Backpack: {self.items}"

    def __len__(self):
        """
        Called by len(object)
        """
        return len(self.items)

    def __getitem__(self, index):
        """
        Called by object[index]
        """
        return self.items[index]


bag = Backpack("Alice")

bag.add_item("Laptop")
bag.add_item("Notebook")
bag.add_item("Water Bottle")

print("=== __str__ ===")
print(bag)

print("\n=== __len__ ===")
print(len(bag))

print("\n=== __getitem__ ===")
print(bag[0])
print(bag[1])
