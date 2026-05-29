# This function contains the main logic of the program.
# You usually put the core workflow of your script here.
def main():
    print("Hello from main()!")


# __name__ is a special built-in variable in Python.
#
# When you run this file directly:
#     python myscript.py
# Python sets __name__ to "__main__"
#
# But when this file is imported from another file:
#     import myscript
# __name__ becomes "myscript" instead.
#
# This condition makes sure main() only runs
# when the file is executed directly.
if __name__ == "__main__":
    main()
