#!/usr/bin/python3

divider = "_" * 100

print(divider)

fd = open("show_version.txt")

output = fd.read()

print(output + "\n" + divider)
print("Type of printed output above:",type(output))
print(divider)

fd.close()


with open("show_version.txt") as fd:
    output = fd.readlines()

print("\n" + divider)
print(output,divider)
print("Type of printed output above:",type(output))
print(divider + "\n")
