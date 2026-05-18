#!/usr/bin/env python3

import os
import sys

# File should be executed with two arguement like newfile.txt
# python script.py hello.txt
# python script.py notes.txt
# python script.py mydata.txt

if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
print(filename)

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)
