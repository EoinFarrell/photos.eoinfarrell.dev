#!/usr/bin/python

import os
import sys

name = str(sys.argv[1])
path = '../assets/' + name
index_path = '../content/' + name + "/_index.md"

print(index_path)

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(os.path.join(path, file))
        with open(index_path, "a") as index_file:
	        index_file.write("- src: " + name + "/" + str(file) + "\n  type: image\n")