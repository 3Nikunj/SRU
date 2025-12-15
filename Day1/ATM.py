class Operations:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount:.2f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        elif amount <= 0:
            return "Withdrawal amount must be positive."
        else:
            self.balance -= amount
            return f"Withdrew: ${amount:.2f}"

    def get_balance(self):
        return f"Current balance: ${self.balance:.2f}"
    
class SBI (Operations):
    def __init__(self, balance=0, interest_rate=0.04):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Applied interest: ${interest:.2f}"
    
class HDFC (Operations):
    def __init__(self, balance=0, interest_rate=0.05):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Applied interest: ${interest:.2f}"
    
class ICICI (Operations):
    def __init__(self, balance=0, interest_rate=0.045):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Applied interest: ${interest:.2f}"

class AXIS (Operations):
    def __init__(self, balance=0, interest_rate=0.042):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Applied interest: ${interest:.2f}"
    
