# Purpose: Check if an ip is in a specified ip-range
# https://docs.python.org/3/howto/ipaddress.html


# Necessary import
from ipaddress import ip_network, ip_address

ip = '1.1.1.1'
net = '1.1.1.0/24'

# Convert ip to an ip-address object
ip_obj = ip_address(ip)

# Convert net to network object
net_obj = ip_network(net)

# Check if ip is in network
print(ip_obj in net_obj)
