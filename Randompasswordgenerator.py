import random
import string

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters to create a password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_multiple_passwords():
    # Ask user how many passwords they want to generate
    num_passwords = int(input("How many passwords would you like to generate? "))
    
    while True:
        # Ask user for desired password length with no limit
        password_length = input("Enter the desired length of each password (or 'exit' to quit): ")
        
        if password_length.lower() == 'exit':
            break
        
        # Ensure the entered length is a valid integer
        if password_length.isdigit():
            password_length = int(password_length)
            # Generate and display the passwords
            for _ in range(num_passwords):
                print(generate_password(password_length))
        else:
            print("Please enter a valid number for password length.")

# Call the function to generate passwords
generate_multiple_passwords()