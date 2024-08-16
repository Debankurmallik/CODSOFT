import random
import string

def generate_password(length):
    if length < 1:
        return "Password length should be at least 1"
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length for the password: "))
        if length < 1:
            print("Please enter a length of at least 1.")
        else:
            password = generate_password(length)
            print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
