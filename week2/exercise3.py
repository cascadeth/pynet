#!/usr/bin/python3
from pprint import pprint

lines = open('show_arp.txt').readlines()

# Remove the first line via a slice
lines = lines[1:]

# Pretty print the lines
pprint(lines)

# Sort the lines (in place - affects original object)
lines.sort()

# Create a new list via slice, of only the first three lines
first_three = lines[:3]

# Join the three lines in the list on a new line character to create a string object
first_three_string = '\n'.join(first_three)

open('arp_entries.txt','w').write(first_three_string)
