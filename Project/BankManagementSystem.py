#create a bank account class that encapsulates the attributes account number, account holder and balance
class BankAccount:
    def __init__(self, accountNumber,accountHolder,balance):
        self.accountNumber = accountNumber
        self.accountHolder= accountHolder
        self.balance = balance
    def deposit(self, amount): #method for depositing 
        self.balance += amount
        print("Amount Deposited", self.balance)

    def withdrawal(self, amount): #method for withdrawal 
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("<-- Insuficiant Balance -->")

#create a saving account class that ingerits from bankaccount and assa and aditional attribute interest rate.
# Override the calculate interest method to calculate interest based on the balance and intest rate.
class SavingAccount(BankAccount):
    def __init__(self, accountNumber, accountHolder, balance, interestRate):
        super().__init__(accountNumber, accountHolder, balance)
        self.interestRate = interestRate
    
    def calculateInterest(self):
        return self.balance *(self.interestRate/100)
    
#example usage
#apply abstaction by using base class bank account to handle generic bank account functionality and derived class SavingAccount to handle saving account specific operations.
AccountDetails = SavingAccount(8187851005, "Pablo Thakur", 500000,6)
AccountDetails.deposit(6000)
AccountDetails.withdrawal(300)

#demonstrate polymorphism by calling the calculate interest method on both Bank account and savingAccount objects,
#which will execute the appropiate implementation based on the objext type. 
AccountInterst = AccountDetails.calculateInterest()
print("Available Balance = ", AccountDetails.balance)
print("Interest Calculated = ", AccountInterst)
