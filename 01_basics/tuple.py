tea_types = ("Black", "Green", "Oolong")
print(tea_types[0])

# tea_types[0] = "Masala"  //TypeError: 'tuple' object does not support item assignment

more_tea = ("Herbal", "Earl Grey")
all_tea = tea_types + more_tea
print(all_tea)

if "Black" in all_tea:
    print("I have Black tea")

more_tea = ("Herbal", "Earl Grey" , "Herbal")
print(more_tea.count("Herbal"))

(black, green , oolong) = tea_types
print(green)

print(type(tea_types))