
# define the variable to hold your age
your_age = input("what is your age: ")

# convert the input into number
your_age_as_number = int(your_age)

# adding to to the initial age
your_age_as_number += 10

# print the result with a little formating
print(f"your age + 10 is {your_age_as_number} ")

# converting age into string
your_age_as_text = str(your_age_as_number)


print("your age + 10 is equal to : " + your_age_as_text)