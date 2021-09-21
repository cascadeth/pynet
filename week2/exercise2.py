#!/usr/bin/python3

divider = "_" * 77

ip_addr_list = ['0.0.0.0','1.1.1.1','99.99.99.99','3.3.3.3','4.4.4.4']

# Append a single IP address to the list
ip_addr_list.append('5.5.5.5')

# Extend the list with two IP addresses
ip_addr_list.extend(['6.6.6.6','7.7.7.7'])

print(divider)

for ip in ip_addr_list:
    print(ip)

print(divider)

print(ip_addr_list[0])

print(divider)
