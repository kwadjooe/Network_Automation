# defining both network portion 
Data_vlan_network_part = ['10.1.10.', '10.1.20.']
Voice_vlan_network_part = ['172.16.10.', '172.16.20.']

# defining my function
def check_ip(ip_addr):
    for network_part in Data_vlan_network_part:
        if ip_addr.startswith(network_part):
            print(f"{ip_addr} is an Address in the 'Data VLAN Network'")
    for network_part in Voice_vlan_network_part:
        if ip_addr.startswith(network_part):
            print(f"{ip_addr} is an Address in the 'Voice VLAN Network'")


check_ip("10.1.10.1")

check_ip("172.16.20.24")