#!/usr/bin/python3

system_name = "false"
port_id = "false"

for line in open("show_lldp_neighbors_detail.txt").readlines():
    if "System Name" in line:
        system_name = line.split(':')[1].split()[0]

    if "Port id" in line:
        port_id = line.split(':')[1].split()[0]
    if system_name != "false" and port_id != "false":
        print("Sys Name: {}\nPortID:   {}".format(system_name, port_id))
        break
