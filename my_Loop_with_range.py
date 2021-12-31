# define the network portion of the IPv4 Address
network_part = "192.168.1."

# define the host list on which to iterate
host_parts = [1, 24, 25, 10, 11]

# loop using the range with the len function
for idx in range (len(host_parts)):
    host_part = host_parts[idx]
    IP = network_part + str(host_part)
    print("The Host IP Address is: " + IP)
