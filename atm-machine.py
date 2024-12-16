# This is a dictionary to store account details. The key is the ATM PIN, and the value is a dictionary.
accounts = {
    1234: {"type": "Savings", "balance": 2000, "transaction_history": []},
    3232: {"type": "Checking", "balance": 1400, "transaction_history": []},
    7890: {"type": "Business", "balance": 1800, "transaction_history": []}
}

# A function to check the balance of the account.
def check_balance(account):
    print(f"Account Type: {account['type']}") # Print the type of account (e.g., Savings, Checking)
    print(f"Your current balance is £{account['balance']:.2f}") # Print the balance, formatted to two decimal places

# A function to withdraw money from the account
def withdraw_amount(account):
    try:
        # Asking user for withdrawal amount
        amount = float(input("Please enter withdraw amount: ")) # Convert input to float for decimal amounts
        # Check if the withdrawal amount is valid (positive and less than or equal to the balance)
        if amount <= 0:
            print("Withdrawal amount must be positive.")  # Error if amount is less than or equal to 0
        elif amount <= account['balance']:
            account['balance'] -= amount  # Deduct the amount from the balance
            # Add the withdrawal transaction to the history
            account['transaction_history'].append(f"Withdrew £{amount:.2f}")
            print(f"Withdrawal successful. Your new balance is £{account['balance']:.2f}")
        else:
            print("Low balance.")
    except ValueError:
        print("Invalid amount. Please enter a number.")  # Handle invalid input

# Function to deposit money into the account
def deposit_amount(account):
    try:
        # Asking user for deposit amount
        amount = float(input("Please enter the deposit amount: "))
        # Check if the deposit amount is valid (positive number
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            account['balance'] += amount # Add the deposit amount to the balance
            # Add the deposit transaction to the history
            account['transaction_history'].append(f"Deposited £{amount:.2f}")
            print(f"Deposit successful. Your new balance is £{account['balance']:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a number.")  # Handle invalid input

# Function to view the transaction history of the account
def view_transaction_history(account):
    print("Transaction History:")
    # Check if there are no transactions in the history
    if not account['transaction_history']:
        print("No transactions found.")
    else:
        # Print each transaction in the history
        for transaction in account['transaction_history']:
            print(transaction)

# Main function to simulate ATM behavior
def atm():
    print("Welcome to the ATM Simulator!")
    print("Please insert your ATM Card")

    max_attempts = 3 # Maximum number of attempts for entering the correct PIN
    attempts = 0 # Counter to track the number of failed attempts

    # Loop until the user enters the correct PIN or reaches max attempts

    while attempts < max_attempts:
        try: # Asking for the 4-digit ATM PIN
            pin = int(input("Enter your 4 digit ATM Pin: "))
        except ValueError:
            print("Invalid PIN. Please enter a 4 digit number.")
            attempts += 1 # Increase the number of attempt
            continue # Prompt the user again for the PIN

        # Verify if the the entered PIN exists in the accounts dictionary
        if pin in accounts:
            account = accounts[pin]
            while True:
                print("Options:")
                print("1 = Check Balance")
                print("2 = Withdraw Amount")
                print("3 = Deposit Amount")
                print("4 = View Transaction History")
                print("5 = Exit")
                try:
                    # Ask the user to choose an option from the ATM options
                    option = int(input("Please enter your choice: "))
                except ValueError:
                    print("Please enter a valid option") # Handle non-integer input for menu choice
                    continue # Asking again for a valid option

                # Act according to the user selection
                if option == 1:
                    check_balance(account)
                elif option == 2:
                    withdraw_amount(account)
                elif option == 3:
                    deposit_amount(account)
                elif option == 4:
                    view_transaction_history(account)
                elif option == 5:
                    print("Thank you for using our ATM. Goodbye!") # Exit the ATM
                    break # Exit the inner loop, ending the session
                else:
                    print("Invalid option. Please try again.") # Invalid menu option
            break # Exit the loop after a valid PIN is entered and a session ends

        else:
            print("Invalid PIN. Please try again.") # PIN not found in accounts
            attempts += 1 # Increase the number of attempt

    # If maximum attempts are reached, notify the user
    if attempts == max_attempts:
        print("Too many invalid attempts. Please contact our customer service.")

# Run the ATM program if this script is executed directly. 
if __name__ == "__main__":
    atm()
