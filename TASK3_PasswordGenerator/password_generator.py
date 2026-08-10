import random
import string

def generate_password():
    print("Password Generator")
    length = int(input("Enter desired password length: "))

    if length < 4:
        print("Please choose a length of at least 4 for a secure password.")
        return

    print("Select complexity:")
    print("1. Letters only")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Symbols (most secure)")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        characters = string.ascii_letters
    elif choice == '2':
        characters = string.ascii_letters + string.digits
    elif choice == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    generate_password()