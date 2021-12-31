# defining both network portion 
Data_vlan_network_part = '10.1.10.'
Voice_vlan_network_part = '172.16.10.'

# defining the device type
device_type = input('What device type Data/Voice: ')
host_part = input('what is the Host IP? ')

# defining the condition
if device_type == 'Data':
     IP = str(Data_vlan_network_part) + str(host_part)
     print(f'Your Data Network Device IP is : {IP}')
elif device_type == 'Voice':
    IP = str(Voice_vlan_network_part) + str(host_part)
    print(f'Your Voice Network Device IP is: {IP}')
else:
    print(f"Sorry, I am not sure what Network is {device_type} and won't be able to provide you with a valid IP Address")
