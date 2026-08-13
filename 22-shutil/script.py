"""
shutil Module in Python
=======================

The shutil module provides high-level file and directory operations.

It is useful when you want to:
    - Copy files
    - Copy entire directories
    - Move files or directories
    - Delete directories
    - Create and extract archives
    - Check disk usage

Unlike the os module, which provides lower-level operating-system
operations, shutil provides convenient functions for common
file-management tasks.

Documentation:
https://docs.python.org/3/library/shutil.html
"""

# shutil stands for "shell utilities".

import shutil
from pathlib import Path

# ============================================================
# 1. COPYING A FILE
# ============================================================

"""
shutil.copy()

Copies a file to another location.

Syntax:
    shutil.copy(source, destination)

Example:

    shutil.copy("example.txt", "backup/example.txt")

This copies example.txt into the backup directory.

The contents and file permissions are copied.
"""

source_file = Path("example.txt")
destination_file = Path("backup/example.txt")

# Uncomment this when example.txt exists:
# shutil.copy(source_file, destination_file)

print("1. shutil.copy()")
print("Copies a file to another location.")
print()


# ============================================================
# 2. COPYING A FILE WITH METADATA
# ============================================================

"""
shutil.copy2()

copy2() works similarly to copy(), but also attempts to preserve
metadata such as the file's modification time.

Example:

    shutil.copy2("example.txt", "backup/example.txt")
"""

print("2. shutil.copy2()")
print("Copies a file while preserving more metadata.")
print()


# ============================================================
# 3. COPYING ONLY FILE CONTENTS
# ============================================================

"""
shutil.copyfile()

copyfile() copies the contents of one file to another file.

It does NOT copy file metadata or permissions.

Example:

    shutil.copyfile("example.txt", "example_copy.txt")
"""

print("3. shutil.copyfile()")
print("Copies the contents of one file to another.")
print()


# ============================================================
# 4. COPYING A DIRECTORY
# ============================================================

"""
shutil.copytree()

copytree() copies an entire directory and everything inside it.

Example:

    shutil.copytree("project", "project_backup")

This creates:

    project_backup/
        file1.txt
        file2.txt
        images/
        ...

Python normally raises FileExistsError if the destination already
exists.

With dirs_exist_ok=True, an existing destination is allowed:

    shutil.copytree(
        "project",
        "project_backup",
        dirs_exist_ok=True
    )
"""

print("4. shutil.copytree()")
print("Copies an entire directory recursively.")
print()


# ============================================================
# 5. MOVING FILES OR DIRECTORIES
# ============================================================

"""
shutil.move()

move() moves a file or directory to another location.

Example:

    shutil.move("example.txt", "backup/example.txt")

It can also move entire directories:

    shutil.move("project", "backup/project")

If the destination is on the same filesystem, this is typically
implemented as a rename. Otherwise, shutil may copy the data and
then remove the original.
"""

print("5. shutil.move()")
print("Moves a file or directory.")
print()


# ============================================================
# 6. DELETING A DIRECTORY
# ============================================================

"""
shutil.rmtree()

rmtree() recursively deletes a directory and everything inside it.

Example:

    shutil.rmtree("old_project")

WARNING:

    This permanently deletes the directory and its contents.

Use this function carefully.
"""

print("6. shutil.rmtree()")
print("Recursively deletes a directory.")
print()


# ============================================================
# 7. FINDING DISK USAGE
# ============================================================

"""
shutil.disk_usage()

disk_usage() returns information about disk space.

Example:

    usage = shutil.disk_usage("/")

The result contains:

    usage.total
    usage.used
    usage.free

The values are returned in bytes.
"""

usage = shutil.disk_usage("/")

print("7. shutil.disk_usage()")
print(f"Total disk space: {usage.total:,} bytes")
print(f"Used disk space:  {usage.used:,} bytes")
print(f"Free disk space:  {usage.free:,} bytes")
print()


# ============================================================
# 8. CREATING AN ARCHIVE
# ============================================================

"""
shutil.make_archive()

make_archive() creates an archive such as ZIP or TAR.

Example:

    shutil.make_archive(
        "backup",
        "zip",
        "project"
    )

This creates:

    backup.zip

containing the contents of the project directory.
"""

print("8. shutil.make_archive()")
print("Creates an archive such as ZIP or TAR.")
print()


# ============================================================
# 9. EXTRACTING AN ARCHIVE
# ============================================================

"""
shutil.unpack_archive()

unpack_archive() extracts an archive.

Example:

    shutil.unpack_archive(
        "backup.zip",
        "restored_project"
    )

This extracts backup.zip into the restored_project directory.
"""

print("9. shutil.unpack_archive()")
print("Extracts an archive.")
print()


# ============================================================
# 10. CHECKING WHICH PROGRAM WILL RUN
# ============================================================

"""
shutil.which()

which() searches for an executable in the system PATH.

For example:

    shutil.which("python")

might return something like:

    /usr/local/bin/python

If the program cannot be found, it returns None.

This is useful when writing automation scripts that depend on
external programs.
"""

python_path = shutil.which("python")

print("10. shutil.which()")
print(f"Python executable: {python_path}")
print()


# ============================================================
# 11. PRACTICAL EXAMPLE: BACKUP A DIRECTORY
# ============================================================

"""
Here is a practical example using several shutil functions.

Suppose we have:

    my_project/
        app.py
        config.py
        images/
        data/

We can create a backup of the entire project:

    shutil.copytree(
        "my_project",
        "my_project_backup",
        dirs_exist_ok=True
    )

"""

print("11. Practical backup example")
print("""
# Create a backup of a directory:

shutil.copytree(
    "my_project",
    "my_project_backup",
    dirs_exist_ok=True
)
""")
print()


# ============================================================
# 12. PRACTICAL EXAMPLE: ORGANIZING FILES
# ============================================================

"""
shutil can also be useful for organizing files.

For example:

    downloads/
        photo.jpg
        document.pdf
        another_photo.jpg

We could move images into an images directory:

    shutil.move(
        "downloads/photo.jpg",
        "images/photo.jpg"
    )

"""

print("12. Practical file organization example")
print("""
# Move a file:

shutil.move(
    "downloads/photo.jpg",
    "images/photo.jpg"
)
""")
print()


# ============================================================
# 13. IMPORTANT DIFFERENCE BETWEEN COPY FUNCTIONS
# ============================================================

"""
The main copy functions can be summarized like this:

    shutil.copy()
        Copies file contents and permissions.

    shutil.copy2()
        Copies file contents, permissions, and more metadata.

    shutil.copyfile()
        Copies only the file contents.

    shutil.copytree()
        Copies an entire directory recursively.

Example:

    shutil.copy("a.txt", "b.txt")
    shutil.copy2("a.txt", "b.txt")
    shutil.copyfile("a.txt", "b.txt")

For directories:

    shutil.copytree("source", "destination")
"""


# ============================================================
# 14. COMMON shutil FUNCTIONS
# ============================================================

"""
Common shutil functions:

    copy()
        Copy a file.

    copy2()
        Copy a file and preserve more metadata.

    copyfile()
        Copy file contents.

    copytree()
        Copy an entire directory.

    move()
        Move a file or directory.

    rmtree()
        Delete a directory recursively.

    disk_usage()
        Get disk space information.

    make_archive()
        Create an archive.

    unpack_archive()
        Extract an archive.

    which()
        Find an executable in PATH.
"""


# ============================================================
# 15. shutil vs os
# ============================================================

"""
shutil and os are often used together.

os is useful for lower-level filesystem operations:

    os.mkdir()
    os.rename()
    os.remove()
    os.listdir()

shutil provides higher-level operations:

    shutil.copy()
    shutil.copytree()
    shutil.move()
    shutil.rmtree()

For example:

    import os
    import shutil

    os.mkdir("backup")

    shutil.copy(
        "example.txt",
        "backup/example.txt"
    )

The two modules complement each other and are commonly used
together in automation scripts.
"""


# ============================================================
# SUMMARY
# ============================================================

print("=" * 60)
print("shutil MODULE SUMMARY")
print("=" * 60)

print("""
shutil is a Python standard-library module for high-level
file and directory operations.

Most important functions:

    shutil.copy()
    shutil.copy2()
    shutil.copyfile()
    shutil.copytree()
    shutil.move()
    shutil.rmtree()
    shutil.disk_usage()
    shutil.make_archive()
    shutil.unpack_archive()
    shutil.which()

The module is especially useful for:

    - Backup scripts
    - File organization
    - Automation
    - Deployment scripts
    - Creating archives
    - Moving files
    - Copying project directories

Remember:

    import shutil

You do NOT need to install shutil with pip because it is
included in Python's standard library.
""")
