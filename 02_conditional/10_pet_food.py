pet = input("which is your pet: ")
pet = pet.lower()

age = int(input("Enter your pet age: "))

if pet == "dog":
    if age <2:
        print("Take puppy food")
    elif age <7:
        print("Take Dog food")
    else:
        print("Take senior Dog food")


if pet == "cat":
    if age <1:
        print("Take kitty food")
    elif age <5:
        print("Take cat food")
    else:
        print("Take senior cat food")



