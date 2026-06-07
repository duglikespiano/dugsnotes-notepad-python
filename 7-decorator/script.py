# A decorator is just a function that accepts another function
# as an argument and returns a new function.

def logger(func):
    """
    Decorator that logs when a function starts and finishes.
    """

    # This inner function replaces the original function.
    # *args and **kwargs allow it to work with any arguments.
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting '{func.__name__}'")

        # Execute the original function
        result = func(*args, **kwargs)

        print(f"[LOG] Finished '{func.__name__}'")

        # Return the original function's result
        return result

    # Return the wrapper function
    return wrapper


# @logger is equivalent to:
# greet = logger(greet)
@logger
def greet(name):
    print(f"Hello, {name}!")
    return "Greeting completed"


# Call the decorated function
message = greet("Suho")

print(message)