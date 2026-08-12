#!/usr/bin/env python3

"""
Python Shebang Explanation
==========================

This script explains why we put a shebang at the beginning of a Python script.

A shebang is the first line of a script that tells the operating system
which interpreter should be used to execute the script.

Example:

    #!/usr/bin/env python3

The "#!" characters are called "shebang".

"env" searches for the program in the user's PATH, and "python3"
specifies that Python 3 should be used.
"""


def explain_shebang():
    print("Python Shebang Explanation")
    print("=" * 30)

    print("\n1. What is a shebang?")
    print("-" * 30)
    print("A shebang is the first line of a script that tells")
    print("the operating system which interpreter should execute it.")

    print("\nExample:")
    print("#!/usr/bin/env python3")

    print("\n2. Why do we need a shebang?")
    print("-" * 30)
    print("The shebang allows us to execute a Python script directly")
    print("without explicitly typing 'python3' before the filename.")

    print("\nWithout a shebang:")
    print("python3 my_script.py")

    print("\nWith a shebang and executable permission:")
    print("./my_script.py")

    print("\n3. What does this mean?")
    print("-" * 30)
    print("#!               -> tells the OS this is an interpreter directive")
    print("/usr/bin/env     -> finds a program using the PATH environment variable")
    print("python3          -> specifies that Python 3 should be used")

    print("\n4. Why use /usr/bin/env?")
    print("-" * 30)
    print("Python may be installed in different locations on different systems.")
    print("Using /usr/bin/env python3 allows the system to find Python 3")
    print("based on the user's PATH instead of hard-coding its location.")

    print("\n5. Making the script executable")
    print("-" * 30)
    print("On Linux or macOS, you can make the script executable with:")

    print("\n    chmod +x my_script.py")

    print("\nThen you can run it with:")

    print("\n    ./my_script.py")

    print("\n6. Important point")
    print("-" * 30)
    print("A shebang is especially useful when a Python script is")
    print("used as a command-line program, shell script, automation script,")
    print("or executable tool.")

    print("\nSummary")
    print("-" * 30)
    print("The shebang tells the operating system:")
    print("'Use Python 3 to execute this file.'")
    print("\nThe most common Python shebang is:")
    print("#!/usr/bin/env python3")


if __name__ == "__main__":
    explain_shebang()
