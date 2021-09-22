#!/usr/bin/python3

divider = "_" * 77

ip_addr_list = ['0.0.0.0','1.1.1.1','99.99.99.99','3.3.3.3','4.4.4.4']

# Append a single IP address to the list
ip_addr_list.append('5.5.5.5')

# Extend the list with two IP addresses
ip_addr_list.extend(['6.6.6.6','7.7.7.7'])

# Cat three more IPs onto the list
ip_addr_list += ['8.8.8.8','9.9.9.9','10.10.10.10']

print(divider)

# Print list in column format
for ip in ip_addr_list:
    print(ip)

print(divider)

print("First IP in list:",ip_addr_list[0])
print("Last IP in list: ",ip_addr_list[-1])

print(divider)

# Pop first item in the list
ip_addr_list.pop(0)

# Pop last item in the list
ip_addr_list.pop(-1)

# Insert a new IP address (at the front)
ip_addr_list.insert(0,'2.2.2.2')

print("First IP in list:",ip_addr_list[0])
