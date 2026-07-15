"""
=====================================================
Python Dynamic Typing Demonstration
=====================================================

This file explains:

1. What Dynamic Typing is
2. Variables can change type
3. Different objects have different methods
4. Type checking
5. Function examples
6. Common mistakes
7. Best practices

Run:

    python dynamic_typing_demo.py

=====================================================
"""

print("=" * 60)
print("1. Variables are NOT tied to one type")
print("=" * 60)

value = 100
print(value)
print(type(value))

value = "Python"
print(value)
print(type(value))

value = 3.14
print(value)
print(type(value))

value = True
print(value)
print(type(value))

value = [1, 2, 3]
print(value)
print(type(value))


print("\n" + "=" * 60)
print("2. Same variable, different object")
print("=" * 60)

data = 42
print("data =", data)
print(type(data))

data = "Forty Two"
print("data =", data)
print(type(data))

data = {"name": "Alice"}
print("data =", data)
print(type(data))


print("\n" + "=" * 60)
print("3. Objects determine available methods")
print("=" * 60)

text = "hello"

print(text.upper())

text = [1, 2, 3]

text.append(4)
print(text)

# Variables don't own methods.
# The object they reference does.


print("\n" + "=" * 60)
print("4. Dynamic typing inside loops")
print("=" * 60)

items = [
    100,
    "apple",
    3.14,
    False,
    [1, 2],
    {"x": 10},
]

for item in items:
    print(f"{item!r:15} -> {type(item).__name__}")


print("\n" + "=" * 60)
print("5. isinstance()")
print("=" * 60)

value = "123"

if isinstance(value, str):
    print("It's a string")

value = 123

if isinstance(value, int):
    print("It's an integer")


print("\n" + "=" * 60)
print("6. Dynamic typing in functions")
print("=" * 60)


def double(x):
    return x + x


print(double(10))
print(double(3.5))
print(double("Hi "))
print(double([1, 2]))


print("""
The same function works because each type defines
how '+' behaves.
""")


print("\n" + "=" * 60)
print("7. Not everything works")
print("=" * 60)

try:
    print(10 + "hello")
except TypeError as e:
    print("TypeError:", e)


print("\n" + "=" * 60)
print("8. Type can change at runtime")
print("=" * 60)

x = 5
print(type(x))

x = "Now I'm a string"
print(type(x))

x = {"language": "Python"}
print(type(x))


print("\n" + "=" * 60)
print("9. id() shows a new object")
print("=" * 60)

x = 10
print(id(x))

x = "hello"
print(id(x))

x = [1, 2, 3]
print(id(x))

print("""
Each assignment usually points the variable to
a completely different object.
""")


print("\n" + "=" * 60)
print("10. Everything is an object")
print("=" * 60)

objects = [
    1,
    3.14,
    "hello",
    True,
    (1, 2),
    [1, 2],
    {"a": 1},
    {1, 2},
]

for obj in objects:
    print(f"{type(obj).__name__:12} has id {id(obj)}")


print("\n" + "=" * 60)
print("11. Dynamic typing is NOT weak typing")
print("=" * 60)

print("Python is dynamically typed...")
print("...but strongly typed.")

print()

print("This works:")
print("5 + 6 =", 5 + 6)

print()

print("This does NOT work:")

try:
    print(5 + "6")
except TypeError as e:
    print(e)

print("""
Python does NOT automatically convert
integers into strings.

This is called strong typing.
""")


print("\n" + "=" * 60)
print("12. Optional type hints")
print("=" * 60)


def greet(name: str) -> str:
    return "Hello " + name


print(greet("Alice"))

print("""
Type hints improve readability,
autocomplete, and static analysis.

However, Python does NOT enforce them
at runtime.
""")

print("\nCalling with an integer:")

try:
    print(greet(123))
except TypeError as e:
    print(e)


print("\n" + "=" * 60)
print("13. Summary")
print("=" * 60)

print("""
Dynamic Typing Summary

✓ Variables have NO fixed type.

✓ Objects have types.

✓ Variables can reference different object types.

✓ Types are determined at runtime.

✓ Python is dynamically typed
  AND strongly typed.

✓ Use isinstance() when behavior depends
  on the object's type.

✓ Type hints are optional and are mainly
  for documentation and development tools.
""")
