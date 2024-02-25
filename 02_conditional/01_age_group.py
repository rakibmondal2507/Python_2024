user_age =int(input("Enter your age: "))

if user_age < 13:
    print("You are a child")
elif user_age >= 13 and user_age <= 19:
    print("you are teenager")
elif user_age >= 20 and user_age <= 59:
    print("You are Adult now.")
else: print("You are Senior")
