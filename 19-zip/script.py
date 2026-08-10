# ============================================================

# Python zip()

# ============================================================

#

# zip() combines elements from multiple iterables together.

#

# Basic syntax:

#

# zip(iterable1, iterable2, ...)

#

# zip() returns a zip object, which is an iterator.

#

# The most common use is to process multiple lists together.

# ============================================================

# ------------------------------------------------------------

# 1. Basic Example

# ------------------------------------------------------------

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

result = zip(names, ages)

print(result)

# <zip object at ...>

# Convert the zip object to a list to see the result.

print(list(result))

# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# ------------------------------------------------------------

# 2. How zip() Works

# ------------------------------------------------------------

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(name, age)

# Output:

#

# Alice 25

# Bob 30

# Charlie 35

# Conceptually, zip() creates pairs like this:

#

# names:  Alice    Bob    Charlie

# ages:   25       30     35

# ↓       ↓       ↓

# (Alice, 25)

# (Bob, 30)

# (Charlie, 35)

# ------------------------------------------------------------

# 3. zip() with Three or More Iterables

# ------------------------------------------------------------

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Seoul", "Tokyo", "New York"]

people = zip(names, ages, cities)

print(list(people))

# Output:

#

# [

# ("Alice", 25, "Seoul"),

# ("Bob", 30, "Tokyo"),

# ("Charlie", 35, "New York")

# ]

# ------------------------------------------------------------

# 4. Unpacking Values from zip()

# ------------------------------------------------------------

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# Output:

#

# Alice is 25 years old.

# Bob is 30 years old.

# Charlie is 35 years old.

# ------------------------------------------------------------

# 5. zip() Stops at the Shortest Iterable

# ------------------------------------------------------------

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30]

print(list(zip(names, ages)))

# Output:

#

# [('Alice', 25), ('Bob', 30)]

#

# "Charlie" is ignored because ages has no third value.

# Another example:

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30]

print(list(zip(numbers1, numbers2)))

# Output:

#

# [(1, 10), (2, 20), (3, 30)]

#

# zip() stops when the shortest iterable is exhausted.

# ------------------------------------------------------------

# 6. zip() with Strings

# ------------------------------------------------------------

letters = ["A", "B", "C"]
numbers = [1, 2, 3]

print(list(zip(letters, numbers)))

# Output:

#

# [('A', 1), ('B', 2), ('C', 3)]

# Strings themselves are also iterable:

word = "ABC"
numbers = [1, 2, 3]

print(list(zip(word, numbers)))

# Output:

#

# [('A', 1), ('B', 2), ('C', 3)]

# ------------------------------------------------------------

# 7. zip() with Dictionaries

# ------------------------------------------------------------

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

people = dict(zip(names, ages))

print(people)

# Output:

#

# {

# "Alice": 25,

# "Bob": 30,

# "Charlie": 35

# }

# This is a very common use of zip():

#

# Two lists -> dictionary

# ------------------------------------------------------------

# 8. Creating a Dictionary with More Data

# ------------------------------------------------------------

keys = ["name", "age", "city"]
values = ["Alice", 25, "Seoul"]

person = dict(zip(keys, values))

print(person)

# Output:

#

# {

# "name": "Alice",

# "age": 25,

# "city": "Seoul"

# }

# ------------------------------------------------------------

# 9. Using zip() in a List Comprehension

# ------------------------------------------------------------

numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

sums = [a + b for a, b in zip(numbers1, numbers2)]

print(sums)

# Output:

#

# [11, 22, 33]

# Another example:

prices = [100, 200, 300]
quantities = [2, 3, 4]

totals = [price * quantity for price, quantity in zip(prices, quantities)]

print(totals)

# Output:

#

# [200, 600, 1200]

# ------------------------------------------------------------

# 10. Comparing Two Lists

# ------------------------------------------------------------

list1 = [1, 2, 3]
list2 = [1, 5, 3]

for a, b in zip(list1, list2):
    if a == b:
        print(f"{a} == {b}")
    else:
        print(f"{a} != {b}")

# Output:

#

# 1 == 1

# 2 != 5

# 3 == 3

# ------------------------------------------------------------

# 11. Finding Differences Between Two Lists

# ------------------------------------------------------------

old_prices = [100, 200, 300]
new_prices = [120, 180, 300]

for old, new in zip(old_prices, new_prices):
    if old != new:
        print(f"Changed: {old} -> {new}")

# Output:

#

# Changed: 100 -> 120

# Changed: 200 -> 180

# ------------------------------------------------------------

# 12. zip() Returns an Iterator

# ------------------------------------------------------------

numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

zipped = zip(numbers1, numbers2)

print(zipped)

# <zip object at ...>

# You can iterate over it:

for item in zipped:
    print(item)

# Output:

#

# (1, 10)

# (2, 20)

# (3, 30)

# IMPORTANT:

#

# A zip object is an iterator.

#

# Once it has been consumed, it cannot be reused.

zipped = zip(numbers1, numbers2)

print(list(zipped))

# [(1, 10), (2, 20), (3, 30)]

print(list(zipped))

# []

# If you need to use the result multiple times,

# convert it to a list first.

zipped = list(zip(numbers1, numbers2))

print(zipped)
print(zipped)

# ------------------------------------------------------------

# 13. Unzipping with * (Star Operator)

# ------------------------------------------------------------

pairs = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

names, ages = zip(*pairs)

print(names)

# ('Alice', 'Bob', 'Charlie')

print(ages)

# (25, 30, 35)

# The * operator unpacks the list:

#

# zip(*pairs)

#

# is conceptually similar to:

#

# zip(

# ("Alice", 25),

# ("Bob", 30),

# ("Charlie", 35)

# )

# ------------------------------------------------------------

# 14. Converting the Result of Unzipping to Lists

# ------------------------------------------------------------

pairs = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

names, ages = zip(*pairs)

names = list(names)
ages = list(ages)

print(names)

# ['Alice', 'Bob', 'Charlie']

print(ages)

# [25, 30, 35]

# ------------------------------------------------------------

# 15. zip() with enumerate()

# ------------------------------------------------------------

names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(index, name)

# Output:

#

# 0 Alice

# 1 Bob

# 2 Charlie

# You can also use zip() when you already have

# multiple collections to process together.

names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# ------------------------------------------------------------

# 16. Strict Mode

# ------------------------------------------------------------

#

# By default, zip() silently stops at the shortest iterable.

#

# Python also supports:

#

# zip(..., strict=True)

#

# This raises ValueError when the iterables have

# different lengths.

#

# This feature is available in Python 3.10+.

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30]

# This would raise ValueError:

#

# for name, age in zip(names, ages, strict=True):

# print(name, age)

# Example:

#

# ValueError: zip() argument 2 is shorter than argument 1

#

# strict=True is useful when the lists are expected

# to have exactly the same length.

# ------------------------------------------------------------

# 17. zip() vs zip(strict=True)

# ------------------------------------------------------------

numbers1 = [1, 2, 3]
numbers2 = [10, 20]

# Normal zip():

print(list(zip(numbers1, numbers2)))

# Output:

#

# [(1, 10), (2, 20)]

#

# The extra 3 is ignored.

# Strict zip():

# print(list(zip(numbers1, numbers2, strict=True)))

# Raises:

#

# ValueError

# ------------------------------------------------------------

# 18. zip() with range()

# ------------------------------------------------------------

names = ["Alice", "Bob", "Charlie"]

for index, name in zip(range(len(names)), names):
    print(index, name)

# Output:

#

# 0 Alice

# 1 Bob

# 2 Charlie

#

# However, enumerate() is usually better for this situation:

#

# for index, name in enumerate(names):

# print(index, name)

# ------------------------------------------------------------

# 19. Practical Example: Products

# ------------------------------------------------------------

products = ["Laptop", "Mouse", "Keyboard"]
prices = [1200, 50, 100]

for product, price in zip(products, prices):
    print(f"{product}: ${price}")

# Output:

#

# Laptop: $1200

# Mouse: $50

# Keyboard: $100

# ------------------------------------------------------------

# 20. Practical Example: Calculate Total Price

# ------------------------------------------------------------

products = ["Laptop", "Mouse", "Keyboard"]
prices = [1200, 50, 100]
quantities = [1, 2, 3]

for product, price, quantity in zip(products, prices, quantities):
    total = price * quantity


print(f"{product}: " f"${price} x {quantity} = ${total}")


# Output:

#

# Laptop: $1200 x 1 = $1200

# Mouse: $50 x 2 = $100

# Keyboard: $100 x 3 = $300

# ------------------------------------------------------------

# 21. Practical Example: Calculate Two Lists

# ------------------------------------------------------------

a = [10, 20, 30]
b = [1, 2, 3]

result = []

for x, y in zip(a, b):
    result.append(x - y)

print(result)

# Output:

#

# [9, 18, 27]

# ------------------------------------------------------------

# 22. zip() with a Generator

# ------------------------------------------------------------

#

# zip() works with any iterable, not just lists.

#

# For example, generators are iterators.


def numbers():
    yield 1
    yield 2
    yield 3


letters = ["a", "b", "c"]

for number, letter in zip(numbers(), letters):
    print(number, letter)

# Output:

#

# 1 a

# 2 b

# 3 c

# ------------------------------------------------------------

# 23. Important: zip() Is Lazy

# ------------------------------------------------------------

#

# zip() does not immediately create a list containing

# every combination.

#

# It produces values as they are requested.

#

# This is called lazy evaluation.

#

# Therefore, zip() can be memory-efficient when working

# with large iterables.

numbers1 = range(1, 4)
numbers2 = range(10, 13)

zipped = zip(numbers1, numbers2)

for pair in zipped:
    print(pair)

# Output:

#

# (1, 10)

# (2, 11)

# (3, 12)

# ------------------------------------------------------------

# 24. Common Pattern: Loop Over Multiple Lists

# ------------------------------------------------------------

names = ["Alice", "Bob", "Charlie"]
scores = [90, 80, 95]

# Without zip():

for i in range(len(names)):
    print(names[i], scores[i])

# With zip():

for name, score in zip(names, scores):
    print(name, score)

# zip() is generally cleaner and easier to read.

# ------------------------------------------------------------

# 25. Common Pattern: Convert Two Lists to a Dictionary

# ------------------------------------------------------------

keys = ["name", "age", "city"]
values = ["Alice", 25, "Seoul"]

data = dict(zip(keys, values))

print(data)

# Output:

#

# {

# "name": "Alice",

# "age": 25,

# "city": "Seoul"

# }

# ------------------------------------------------------------

# 26. Common Mistake

# ------------------------------------------------------------

# Don't forget that zip() returns an iterator.

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

zipped = zip(numbers1, numbers2)

print(zipped)

# This does NOT print:

# [(1, 4), (2, 5), (3, 6)]

#

# It prints something like:

# <zip object at 0x...>

# Use list() if you want to see all results:

print(list(zip(numbers1, numbers2)))

# ------------------------------------------------------------

# 27. Another Common Mistake: Reusing a zip Object

# ------------------------------------------------------------

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

zipped = zip(numbers1, numbers2)

first = list(zipped)
second = list(zipped)

print(first)

# [(1, 4), (2, 5), (3, 6)]

print(second)

# []

# The zip iterator was already consumed.

#

# If you need the data more than once:

zipped = list(zip(numbers1, numbers2))

first = zipped
second = zipped

print(first)
print(second)

# ============================================================

# SUMMARY

# ============================================================

#

# zip() combines elements from multiple iterables.

#

# Basic syntax:

#

# zip(iterable1, iterable2, ...)

#

#

# Most common usage:

#

# for a, b in zip(list1, list2):

# ...

#

#

# Convert to a list:

#

# list(zip(list1, list2))

#

#

# Create a dictionary:

#

# dict(zip(keys, values))

#

#

# Unzip:

#

# values1, values2 = zip(*pairs)

#

#

# Strict mode:

#

# zip(list1, list2, strict=True)

#

#

# Important characteristics:

#

# 1. zip() can combine multiple iterables.

#

# 2. zip() returns a zip iterator.

#

# 3. It is lazy.

#

# 4. By default, it stops at the shortest iterable.

#

# 5. strict=True raises ValueError when lengths differ.

#

# 6. zip() is commonly used to process multiple lists

# together.

#

# 7. dict(zip(keys, values)) is a common way to create

# a dictionary from two lists.

#

# ============================================================

#

# Quick mental model:

#

# names  = ["Alice", "Bob", "Charlie"]

# scores = [90, 80, 95]

#

# zip(names, scores)

#

# ↓

#

# ("Alice", 90)

# ("Bob", 80)

# ("Charlie", 95)

#

# ============================================================
