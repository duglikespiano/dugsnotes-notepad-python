# --------------------------------------------
# *args
# --------------------------------------------
def add_numbers(*args):
    """
    *args collects all positional arguments
    into a tuple.

    The name 'args' is just a convention.
    You could write *numbers, *values, etc.
    """

    print(args)
    print(type(args))

    return sum(args)


result = add_numbers(10, 20, 30, 40)

# Output:
# (10, 20, 30, 40)
# <class 'tuple'>
# 100


# --------------------------------------------
# **kwargs
# --------------------------------------------
def print_user(**kwargs):
    """
    **kwargs collects all keyword arguments
    into a dictionary.

    The name 'kwargs' is just a convention.
    """

    print(kwargs)
    print(type(kwargs))


print_user(name="Dug", age=30, country="Japan")

# Output:
# {
#     'name': 'Dug',
#     'age': 30,
#     'country': 'Japan'
# }
# <class 'dict'>
