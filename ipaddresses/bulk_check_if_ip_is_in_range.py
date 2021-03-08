# Purpose: Bulk check if ips are in any of the specified ip-ranges
# https://docs.python.org/3/howto/ipaddress.html


# Necessary import
from ipaddress import ip_network, ip_address


# Example list of IP-ranges from Google and Cloudflare
# copied from:
#   Google: https://www.gstatic.com/ipranges/cloud.json
#   Cloudflare: https://www.cloudflare.com/en-gb/ips/
network_list_str = [
        '34.96.64.0/18',\
        '104.199.112.0/20',\
        '173.245.48.0/20',\
        '2405:b500::/32'
        ]

# Convert list of ip-ranges from string to ip network objects
# This example adds the objects to a new list, so you don't have to convert again later
network_list_obj = []
for e in network_list_str:
    network_list_obj.append(ip_network(e))


# Example of IP-addresses to check
ips_list_str = [
        '104.196.2.43',\
        '8.8.8.8',\
        '173.245.48.99',\
        '1.1.1.1',\
        '9.9.9.9',\
        '104.199.113.23'
        ]

# Convert list of ip-s from string to ip address objects
# This example adds the objects to a new list, so you don't have to convert again later
ips_list_obj = []
for e in ips_list_str:
    ips_list_obj.append(ip_address(e))

# Check if IP-address in in any of the specified IP-ranges
for ipaddress in ips_list_obj:
    for net in network_list_obj:
        if ipaddress in net:
            print(ipaddress)
