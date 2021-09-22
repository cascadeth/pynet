#!/usr/bin/python3

interfaces_brief = open("show_ip_int_brief.txt").readlines()

interface_name = interfaces_brief[5].strip().split()[0]
interface_ip = interfaces_brief[5].strip().split()[2]

interface_tuple = (interface_name, interface_ip)
