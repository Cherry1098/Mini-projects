# Base ATM class (Handles balance operations)
class ATM1:
    def __init__(self, balance=0):
        self.balance = balance  # Account balance

    def check_balance(self):
        return f"Current Balance: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        return "Invalid deposit amount."

# ATM2 extends ATM1 and adds PIN-based authentication + Withdraw function
class ATM2(ATM1):
    def __init__(self, balance=0, pin="1234"):
        self.balance = balance  # Inheriting balance handling
        self.pin = pin  # User's PIN for authentication

    def authenticate(self, entered_pin):
        return self.pin == entered_pin  # Returns True if PIN matches

    def change_pin(self, old_pin, new_pin):
        if self.authenticate(old_pin):
            self.pin = new_pin
            return "PIN changed successfully."
        return "Incorrect old PIN."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn ${amount:.2f}. New balance: ${self.balance:.2f}"
        return "Insufficient funds or invalid amount."

# ATM3 extends ATM2 and adds username-password login for multiple users
class ATM3(ATM2):
    def __init__(self, username, password, balance=0, pin="1234"):
        self.username = username
        self.password = password
        self.balance = balance
        self.pin = pin

    def login(self, entered_username, entered_password):
        return self.username == entered_username and self.password == entered_password

# Dictionary to store multiple users
users = {
    "charishma": ATM3("charishma", "mypassword", balance=1000, pin="5678"),
    "pavan": ATM3("pavan", "securepass", balance=500, pin="1234"),
    "rahul": ATM3("rahul", "pass123", balance=2000, pin="4321")
}

# User login
entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

if entered_username in users and users[entered_username].login(entered_username, entered_password):
    print(f"Welcome, {entered_username}!")

    # PIN Authentication
    entered_pin = input("Enter PIN: ")
    user = users[entered_username]

    if user.authenticate(entered_pin):
        print("Authentication successful!")
        
        while True:
            print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Change PIN\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                print(user.check_balance())
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                print(user.deposit(amount))
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                print(user.withdraw(amount))
            elif choice == "4":
                old_pin = input("Enter current PIN: ")
                new_pin = input("Enter new PIN: ")
                print(user.change_pin(old_pin, new_pin))
            elif choice == "5":
                print("Exiting... Thank you!")
                break
            else:
                print("Invalid choice. Try again.")

    else:
        print("Incorrect PIN. Access denied.")
else:
    print("Invalid username or password.")
