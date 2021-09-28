#!/usr/bin/python3

search_default_gtwy_ip = "10.220.88.1"
search_arista_ip = "10.220.88.30"

found_default_gtwy_ip = False
found_arista_ip = False

for line in open("show_arp.txt").readlines():
    if line.split()[0] == "Protocol":
        continue
    elif found_default_gtwy_ip and found_arista_ip:
        break
    else:
        ip_addr = line.split()[1]
        mac_addr = line.split()[3]

        if ip_addr == search_default_gtwy_ip:
            found_default_gtwy_ip = True
            print("Default gateway IP/Mac is:  {:20} {:20}".format(ip_addr, mac_addr))

        elif ip_addr == search_arista_ip:
            found_arista_ip = True
            print("Arista3 IP/Mac is:          {:20} {:20}".format(ip_addr, mac_addr))
