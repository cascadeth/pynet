#!/usr/bin/python3

vlans = []

for line in open("show_vlan.txt").readlines():
    if not line.split()[0].isdigit():
        continue
    vlans.append((line.split()[0], line.split()[1]))

print(vlans)
