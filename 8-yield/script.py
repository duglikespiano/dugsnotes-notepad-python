# --------------------------------------------
# Basic example of the `yield` keyword
# --------------------------------------------


def count_to_three():
    # Execution starts here

    yield 1
    # Function pauses here and returns 1.
    # Local variables and execution state are preserved.

    yield 2
    # When next() is called again, execution resumes
    # from the previous yield and pauses here.

    yield 3
    # Resumes again and pauses here.

    # After this point, the function ends and raises
    # StopIteration automatically.


# Calling the function does NOT execute it.
# Instead, it creates a generator object.
generator = count_to_three()

print(next(generator))  # 1
# Function runs until first yield.

print(next(generator))  # 2
# Function resumes after the first yield.

print(next(generator))  # 3
# Function resumes after the second yield.

# print(next(generator))
# StopIteration
# No more values to yield.


# --------------------------------------------
# yield vs return
# --------------------------------------------


def using_return():
    return [1, 2, 3]
    # Entire list is created before returning.


def using_yield():
    yield 1
    yield 2
    yield 3
    # Values are produced one at a time as needed.


print(using_return())  # [1, 2, 3]
print(using_yield())  # <generator object ...>

for value in using_yield():
    print(value)


# --------------------------------------------
# Why yield is memory efficient
# --------------------------------------------


def read_large_file(path):
    with open(path) as file:

        # Read one line at a time
        for line in file:
            yield line

            # The line is returned to the caller.
            # The function pauses here.
            # Only one line needs to be in memory.


# Example usage
for line in read_large_file("huge.txt"):
    print(line)


# --------------------------------------------
# Infinite generator
# --------------------------------------------


def counter():
    current = 1

    while True:
        yield current

        # State is preserved between iterations.
        current += 1


numbers = counter()

print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers))  # 3


# --------------------------------------------
# Mental model
# --------------------------------------------


def example():
    print("Step 1")
    yield "A"

    print("Step 2")
    yield "B"

    print("Step 3")


g = example()

# next(g)
# Output:
# Step 1
# A

# next(g)
# Output:
# Step 2
# B

# next(g)
# Output:
# Step 3
# StopIteration

# Think of yield as:
# "Pause here, return a value, and continue later."
#
# Think of return as:
# "Return a value and exit forever."
