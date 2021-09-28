#!/usr/bin/python3

data_lines = open("show_vlan.txt").readlines()

# vlans = [(line.split()[0], line.split()[1]) for line in data_lines]

vlans = []

for line in data_lines:
    if not line.split()[0].isdigit():
        continue
    vlans.append((line.split()[0], line.split()[1]))

print(vlans)
