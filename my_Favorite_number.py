while True:
    fav_num = input("What is your Favorite Number? ")
    if fav_num == "24":
        break
    else:
        print(f"{fav_num} is not your favorite number. Please try again")

print(f"Great {fav_num} is in fact your favorite number")
