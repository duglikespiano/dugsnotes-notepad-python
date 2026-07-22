"""
Walrus Operator (:=) Example
Python 3.8+

The walrus operator is officially called the Assignment Expression Operator.

It allows you to:
1. Assign a value
2. Return that value immediately

Syntax:

variable := expression

Unlike "=" which only assigns,
":=" assigns AND returns the value.
"""

print("=" * 60)
print("1. Normal assignment")
print("=" * 60)

numbers = [3, 7, 12, 20]

length = len(numbers)

if length > 3:
    print(f"List has {length} items")


print("\n" + "=" * 60)
print("2. Using the walrus operator")
print("=" * 60)

numbers = [3, 7, 12, 20]

if (length := len(numbers)) > 3:
    print(f"List has {length} items")


print("\n" + "=" * 60)
print("3. Reading user input")
print("=" * 60)

# Traditional way
name = input("Enter your name: ")

if name:
    print(f"Hello, {name}!")

print()

# Walrus operator
if (name := input("Enter your name again: ")):
    print(f"Hello again, {name}!")


print("\n" + "=" * 60)
print("4. Reading a file")
print("=" * 60)

# Create a sample file
with open("sample.txt", "w") as f:
    f.write("Apple\n")
    f.write("Banana\n")
    f.write("Orange\n")

print("Traditional:")

with open("sample.txt") as f:
    line = f.readline()

    while line:
        print(line.strip())
        line = f.readline()

print()

print("Using walrus operator:")

with open("sample.txt") as f:
    while (line := f.readline()):
        print(line.strip())


print("\n" + "=" * 60)
print("5. Avoiding duplicate function calls")
print("=" * 60)


def expensive_function():
    print("Function executed")
    return 42


# Bad: function runs twice
print("Without walrus:")

if expensive_function() > 0:
    result = expensive_function()
    print(result)

print()

# Good: function runs once
print("With walrus:")

if (result := expensive_function()) > 0:
    print(result)


print("\n" + "=" * 60)
print("6. Using inside list comprehensions")
print("=" * 60)

words = ["Python", "C", "JavaScript", "Go", "Rust"]

# Save the length while filtering
long_words = [
    (word, length)
    for word in words
    if (length := len(word)) >= 5
]

print(long_words)


print("\n" + "=" * 60)
print("7. Regular expression example")
print("=" * 60)

import re

text = "Order number: 54321"

if match := re.search(r"\d+", text):
    print("Found:", match.group())


print("\n" + "=" * 60)
print("8. When NOT to use it")
print("=" * 60)

# Good
if (count := len(words)) > 3:
    print(f"There are {count} words")

# Less readable
# if (x := foo(bar(y := baz()))) > 10:
#     ...
#
# Avoid overly complicated expressions.
#
# The walrus operator is best when it improves readability,
# not when it makes code harder to understand.


print("\n" + "=" * 60)
print("Summary")
print("=" * 60)

print("""
Normal assignment:

    value = expression

Walrus operator:

    value := expression

Use it when you want to:
- compute a value once
- immediately test or use it
- avoid duplicate function calls
- simplify loops
- simplify input handling

Don't use it if it makes the code harder to read.
""")