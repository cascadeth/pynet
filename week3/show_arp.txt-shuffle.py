#!/usr/bin/python3

# Make use of the random library to shuffle a list
import random

# Open the original (already sorted for some reason) file
i_fd = open("show_arp.txt")

# Use readlines to the list of lines in the file
original = i_fd.readlines()

# Close the original file
i_fd.close()

# Create a copy of the original list
copy = list(original)

# Snag the first line of the list (the file header) and save it for later
header = copy.pop(0)

# Shuffle the remaining lines in the list
random.shuffle(copy)

# Insert the header at the beginning of the list
copy.insert(0,header)

# Open a new file to write the original list to
o_fd = open("original-show_arp.txt", "w")

for line in original:
    o_fd.write(line)

o_fd.close()

# Open the original file, to overwrite
o_fd = open("show_arp.txt", "w")

for line in copy:
    o_fd.write(line)

o_fd.close()

