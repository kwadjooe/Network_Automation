
num_a = int(input("Please Provide a first Number: "))
num_b = int(input("Please Provide a second Number: ")) 

def add_numbers():
    result = num_a + num_b
    return result

res = add_numbers()

print(f"The sum of {num_a} and {num_b} is {res}")