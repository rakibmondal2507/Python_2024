chai_types = {"Masala": "Spicy", "Ginger": "Zesty","Green":"Mild"}
# print(chai_types)

# print(chai_types["Masala"])
# print(chai_types.get("Ginger"))

# print(chai_types.get("Gingery"))
# print(chai_types["Masalaa"])

chai_types["Green"] = "Fresh"
# print(chai_types)

# for chai in chai_types:
#     print(chai, chai_types[chai])


# for key, value in chai_types.items():
#     print(key, value)


# if "Masala" in chai_types:
    # print("I have Masala chai")

# print(len(chai_types))

chai_types["Earl Grey"] = "Citrus"
# print(chai_types)

chai_types.pop("Ginger")

chai_types.popitem()

del chai_types["Green"]
# print(chai_types)

chai_types_copy = chai_types.copy()
# print(chai_types_copy)

tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea" : {"Green": "Mild", "Black":"Strong "}
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])

squared_num = {x:x**2 for x in range(6)}
print(squared_num)

squared_num.clear()
print(squared_num)

keys = ["Masala", "Ginger", "Lemon"]
default_values = "Delicious"

new_dict = dict.fromkeys(keys, default_values)
print(new_dict)



