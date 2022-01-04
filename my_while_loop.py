# define IP address collector
ips = []
user_in = ""

# while loop block
while user_in != "Done":
    user_in = input("Please provide an IP Address or type Done to quit the program: ")
    if user_in != "Done":
        ips.append(user_in)
    else:  
        break 
        # print("Thank you. You did not provided any input")
    

print(f"The IP Addresses provided are: {ips} ")