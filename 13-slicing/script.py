"""
Python Slicing Examples
=======================

Syntax:
    sequence[start:stop:step]

start -> inclusive
stop  -> exclusive
step  -> move this many positions each time

Works with:
- strings
- lists
- tuples
"""

# ----------------------------------
# Example data
# ----------------------------------

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
text = "Hello Python"

print("Original list:")
print(numbers)

print("\nOriginal string:")
print(text)

# ----------------------------------
# Basic slicing
# ----------------------------------

print("\n--- Basic slicing ---")

print(numbers[2:6])  # 2,3,4,5
print(text[0:5])  # Hello

# ----------------------------------
# Omitting start
# ----------------------------------

print("\n--- Omit start ---")

print(numbers[:5])  # beginning to index 5
print(text[:5])

# ----------------------------------
# Omitting stop
# ----------------------------------

print("\n--- Omit stop ---")

print(numbers[5:])
print(text[6:])

# ----------------------------------
# Copy everything
# ----------------------------------

print("\n--- Copy everything ---")

copy = numbers[:]

print(copy)
print(copy is numbers)  # False (new list)

# ----------------------------------
# Using step
# ----------------------------------

print("\n--- Step ---")

print(numbers[::2])  # every 2nd element
print(numbers[::3])  # every 3rd element
print(text[::2])  # every 2nd character

# ----------------------------------
# Reverse
# ----------------------------------

print("\n--- Reverse ---")

print(numbers[::-1])
print(text[::-1])

# ----------------------------------
# Negative indices
# ----------------------------------

print("\n--- Negative indices ---")

print(numbers[-1])  # last
print(numbers[-2])  # second last

print(numbers[-5:])
print(text[-6:])

# ----------------------------------
# Negative step
# ----------------------------------

print("\n--- Negative step ---")

print(numbers[8:2:-1])

# Starts at index 8
# Stops BEFORE index 2
# Moves backwards

# ----------------------------------
# Every other item
# ----------------------------------

print("\n--- Every other item ---")

print(numbers[1::2])  # odd positions
print(numbers[::2])  # even positions

# ----------------------------------
# Strings
# ----------------------------------

print("\n--- String slicing ---")

print(text[:5])
print(text[6:])
print(text[::2])
print(text[::-1])

# ----------------------------------
# Tuples
# ----------------------------------

print("\n--- Tuples ---")

colors = ("red", "green", "blue", "yellow", "black")

print(colors[1:4])
print(colors[::-1])

# ----------------------------------
# Practical examples
# ----------------------------------

print("\n--- Practical examples ---")

# Remove first and last character
word = "Python"
print(word[1:-1])

# Last three elements
print(numbers[-3:])

# Everything except last item
print(numbers[:-1])

# Everything except first item
print(numbers[1:])

# Middle of a string
print(word[1:5])

# ----------------------------------
# Common :: patterns
# ----------------------------------

print("\n--- Common :: patterns ---")

print("numbers[:]      =", numbers[:])  # copy
print("numbers[::]     =", numbers[::])  # copy
print("numbers[::2]    =", numbers[::2])  # every second
print("numbers[1::2]   =", numbers[1::2])  # every second starting at index 1
print("numbers[::-1]   =", numbers[::-1])  # reverse
print("numbers[::-2]   =", numbers[::-2])  # reverse, every second

# ----------------------------------
# Step cannot be zero
# ----------------------------------

print("\n--- Invalid ---")

try:
    print(numbers[::0])
except ValueError as e:
    print("Error:", e)
