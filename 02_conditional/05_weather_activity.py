weather = input("Enter weather: ")
weather = weather.lower()

if weather == "sunny":
    activity = "Go for Walk"
elif weather == "rainy":
    activity = "Read a book"
elif weather == "snowy":
    activity = "Make a snowman"
else:
    print("Go to Sleep")
    exit()

print(activity)