#!/usr/bin/python3

for line in open("original-show_arp.txt").readlines():
    arp_entry = line.split()
    if arp_entry[0] != "Internet":
        continue
    elif arp_entry[0] == "Internet":
        unformatted_mac = arp_entry[3]
        semi_formatted_mac = "{}:{}:{}:{}:{}:{}".format(unformatted_mac[0:2], unformatted_mac[2:4], unformatted_mac[5:7], unformatted_mac[7:9], unformatted_mac[10:12], unformatted_mac[12:14])
        print(semi_formatted_mac.upper())
    else:
        print("HULL BREACH!!!")
