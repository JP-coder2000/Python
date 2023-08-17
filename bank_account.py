class BankAccount:
    def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self,add):
        self.balance += add
        return self.balance

    
    def withdraw(self,sub):
        self.balance -= sub
        return self.balance

    def printBalance(self):
        print(self.balance)
    
jp = BankAccount("Juan","Cabrera",12345,"Manager",1,10000.0)

jp.deposit(96)
jp.withdraw(80)
jp.printBalance()
