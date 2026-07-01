import random
import string

print("========== PASSWORD GENERATOR ==========")

# Get password length
length = int(input("Enter the desired password length: "))

print("\nChoose Password Complexity:")
print("1. Letters only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Special Characters")

choice = input("Enter your choice (1/2/3): ")

# Character sets
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# Select character pool based on user choice
if choice == "1":
    characters = letters
elif choice == "2":
    characters = letters + numbers
elif choice == "3":
    characters = letters + numbers + symbols
else:
    print("Invalid choice! Using default (Letters + Numbers + Symbols).")
    characters = letters + numbers + symbols

# Generate password
password = "".join(random.choice(characters) for _ in range(length))

# Display password
print("\nGenerated Password:")
print(password)