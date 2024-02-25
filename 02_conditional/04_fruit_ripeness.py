fruit = input("Type fruit name: ")
fruit = fruit.lower()
# if fruit != "Banana" or fruit != "Apple":
#     print("Now your fruit is not available")
#     exit()


color = input("Type fruit color: ")
color = color.lower()

if fruit == "banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("OverRipe")
    else:
        print("Type valid color")

if fruit == "apple":
    if color == "green":
        print("Unripe")
    elif color == "red" or "brown":
        print("Ripe")
    elif color == "deep brown" or "black":
        print("OverRipe")
    else:
        print("Type valid color")