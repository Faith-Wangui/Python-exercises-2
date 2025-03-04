class BankAccount:
    def _init_(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdrawn: ${amount}"
    
    def check_balance(self):
        print(f"Current Balance: ${self.balance}")
    
    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: ${self.balance}")

account = BankAccount("0462854092397", "Faith Wamae", "202-08-07", 60000)
print(account.deposit(10000))
print(account.withdraw(6000))
account.check_balance()
account.customer_details()