"""
Mutable Default Argument Example
Python 3+

A function's default arguments are evaluated only ONCE
when the function is defined, not every time it is called.

If the default argument is mutable (list, dict, set),
changes persist across future function calls.
"""

print("=" * 60)
print("1. The Problem")
print("=" * 60)


def add_item(item, shopping_list=[]):
    """
    BAD EXAMPLE

    shopping_list is created only once.
    Every function call shares the same list.
    """
    shopping_list.append(item)
    return shopping_list


print(add_item("Apple"))
print(add_item("Banana"))
print(add_item("Orange"))

print("""
Expected by beginners:
['Apple']
['Banana']
['Orange']

Actual:
['Apple']
['Apple', 'Banana']
['Apple', 'Banana', 'Orange']
""")


print("=" * 60)
print("2. Why does this happen?")
print("=" * 60)

print("""
Python creates the default list only once.

          Function Definition

shopping_list ---> []

Call #1
append("Apple")

shopping_list ---> ['Apple']

Call #2
append("Banana")

shopping_list ---> ['Apple', 'Banana']

Call #3
append("Orange")

shopping_list ---> ['Apple', 'Banana', 'Orange']

Every call uses the SAME list.
""")


print("=" * 60)
print("3. Correct Solution")
print("=" * 60)


def add_item(item, shopping_list=None):
    """
    GOOD EXAMPLE

    Create a new list every time the argument
    wasn't supplied.
    """
    if shopping_list is None:
        shopping_list = []

    shopping_list.append(item)
    return shopping_list


print(add_item("Apple"))
print(add_item("Banana"))
print(add_item("Orange"))

print("""
Now every call gets a fresh list.
""")


print("=" * 60)
print("4. Passing your own list")
print("=" * 60)

my_list = ["Milk"]

print(add_item("Eggs", my_list))
print(add_item("Bread", my_list))

print("Original list:", my_list)

print("""
Because we explicitly passed a list,
the function modifies THAT list.
""")


print("=" * 60)
print("5. Mutable dictionary")
print("=" * 60)


def add_score(name, score, scores={}):
    scores[name] = score
    return scores


print(add_score("Alice", 90))
print(add_score("Bob", 80))
print(add_score("Charlie", 95))

print("""
The dictionary keeps growing.
""")


print("=" * 60)
print("6. Correct dictionary version")
print("=" * 60)


def add_score(name, score, scores=None):
    if scores is None:
        scores = {}

    scores[name] = score
    return scores


print(add_score("Alice", 90))
print(add_score("Bob", 80))
print(add_score("Charlie", 95))


print("=" * 60)
print("7. Mutable set")
print("=" * 60)


def add_tag(tag, tags=set()):
    tags.add(tag)
    return tags


print(add_tag("python"))
print(add_tag("django"))
print(add_tag("flask"))

print("""
Same issue with sets.
""")


print("=" * 60)
print("8. Function defaults are stored")
print("=" * 60)


def demo(data=[]):
    data.append("X")
    return data


print("Function defaults:")
print(demo.__defaults__)

demo()

print("After one call:")
print(demo.__defaults__)

demo()

print("After another call:")
print(demo.__defaults__)

print("""
Notice that the default value itself changed.
""")


print("=" * 60)
print("9. When mutable defaults ARE useful")
print("=" * 60)


def counter(history=[]):
    """
    This intentionally remembers previous calls.
    Normally you shouldn't do this,
    but it can occasionally be useful.
    """
    history.append(len(history) + 1)
    return history


print(counter())
print(counter())
print(counter())

print("""
This acts like a tiny piece of persistent state.
""")


print("=" * 60)
print("10. Summary")
print("=" * 60)

print("""
BAD:

def func(data=[]):
    ...

GOOD:

def func(data=None):
    if data is None:
        data = []

The same idea applies to:

- list
- dict
- set

Remember:

Default arguments are evaluated ONCE
when the function is defined.
""")
