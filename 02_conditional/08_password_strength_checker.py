password = input("Check your password strength: ")
pass_len = len(password)

if pass_len <= 6:
    val = "Weak"
elif pass_len <= 10:
    val = "Medium"
elif pass_len > 10:
    val = "Strong"

print("Your password is ",val)
