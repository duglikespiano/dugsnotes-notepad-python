"""
os_module_example.py

This file demonstrates some of the most useful features
of Python's built-in os module.
"""

import os

print("=" * 60)
print("1. Current Working Directory")
print("=" * 60)

# Show where this Python script is currently running
print(os.getcwd())


print("\n" + "=" * 60)
print("2. List Files in Current Directory")
print("=" * 60)

for item in os.listdir():
    print(item)


print("\n" + "=" * 60)
print("3. Create a New Folder")
print("=" * 60)

folder_name = "example_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created '{folder_name}'")
else:
    print(f"'{folder_name}' already exists")


print("\n" + "=" * 60)
print("4. Rename Folder")
print("=" * 60)

new_name = "renamed_folder"

if os.path.exists(folder_name):
    os.rename(folder_name, new_name)
    print(f"Renamed '{folder_name}' -> '{new_name}'")
else:
    print("Nothing to rename.")


print("\n" + "=" * 60)
print("5. Remove Folder")
print("=" * 60)

if os.path.exists(new_name):
    os.rmdir(new_name)
    print(f"Deleted '{new_name}'")
else:
    print("Folder does not exist.")


print("\n" + "=" * 60)
print("6. Environment Variables")
print("=" * 60)

# HOME on Linux/macOS
# USERPROFILE on Windows
home = os.environ.get("HOME") or os.environ.get("USERPROFILE")

print("Home directory:")
print(home)


print("\n" + "=" * 60)
print("7. File and Folder Checks")
print("=" * 60)

print("Does example_folder exist?", os.path.exists("example_folder"))

print("Does this script exist?", os.path.isfile(__file__))

print("Is current directory a directory?", os.path.isdir("."))


print("\n" + "=" * 60)
print("8. Absolute Path")
print("=" * 60)

print(os.path.abspath("."))


print("\n" + "=" * 60)
print("9. Join Paths Correctly")
print("=" * 60)

path = os.path.join("documents", "python", "notes.txt")

print(path)


print("\n" + "=" * 60)
print("10. Execute an Operating System Command")
print("=" * 60)

if os.name == "nt":
    os.system("dir")
else:
    os.system("ls")


print("\nFinished!")
