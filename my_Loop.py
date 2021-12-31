network_part = '192.168.1.'
host_parts = [1, 24, 25]

for host_part in host_parts:
    IP = network_part + str(host_part)
    print('The Host IP address is: ' + IP)

