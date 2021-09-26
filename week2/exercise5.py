#!/usr/bin/python3

lines = open("show_ip_bgp_summ.txt").readlines()

print("Local AS number: {}".format(lines[0].split()[-1]))
print("BGP peer IP address: {}".format(lines[-1].split()[0]))
