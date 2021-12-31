network_part = "192.168.1."
host_parts = [1, 24, 25]

for idx in range (len(host_parts)):
    host_part = host_parts[idx]
    IP = network_part + str(host_part)
    print("The Host IP Address is: " + IP)