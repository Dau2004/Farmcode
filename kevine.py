import re  # Import the regular expression module

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

def is_valid_email(email):
    # Use a simple regular expression to check for a valid email format
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def register():
    username = input("Enter your username: ")
    email = input("Enter your email address: ")

    # Check if the email is valid
    if not is_valid_email(email):
        print("Invalid email address format. Please enter a valid email.")
        return

    password = input("Enter your password: ")
    users.append(User(username, email, password))
    print("Registration successful! Welcome to the home.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user.username == username and user.password == password:
            print("Login successful! Welcome to the home.")
            return

    print("Invalid username or password.")

users = []

while True:
    print("\nOptions:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
