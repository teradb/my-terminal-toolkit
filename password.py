import random
import string

print("\n==================================")
print("Terminal Password Generator")
print("==================================")

try:
    length = int(input("Enter desired password length (minimum 8): "))
    if length < 8:
        print("For security, length must be at least 8 characters. Setting to 8.")
        length = 8
        
    # Combine character sets: letters, digits, and punctuation symbols
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters from the pool
    password = "".join(random.choice(all_characters) for _ in range(length))
    
    print("\n🔒 Your secure password has been generated:")
    print(f"👉  {password}\n")

except ValueError:
    print("Invalid input! Please enter a valid number next time.")

