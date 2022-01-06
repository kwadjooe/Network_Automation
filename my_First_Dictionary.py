print("\n")
config = {}
with open("config.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        key, value = line.split("=")
        value = value.replace("\n", "")
        config[key] = value
        print(f"Added key {key} with value {value}")
print("\n")
print(f"Here is the content of my dictionary\n{config}")
print("\n")
user_key = input("Which key would you like to see? ")
if user_key not in config:
    print(f"The key ({user_key}) you've requested is not in the config file")
else:
    val = config[user_key]
    print(f"The Current value for {user_key} : {val} ")
    next_step = input("Would you like to change it? [y/n] ")

    if next_step == "y":
        new_val = input("What is the new value? ")
        config[user_key] = new_val

print('\n')
print(f"Here is the content of my dictionary after modification\n{config}\n")

with open("config.txt", "a") as f:
    for key, value in config.items():
        l = f"{key}={value}\n"
        f.write(l)
