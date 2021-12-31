# defining the Network portion of the IPv4 address
network_part = '192.168.1.'

# defining the host list on which to iterate
host_parts = [1, 24, 25, 10, 11]

# loop using the for each construct
for host_part in host_parts:
    IP = network_part + str(host_part)
    print('The Host IP address is: ' + IP)

