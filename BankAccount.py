class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount,acnt_name):
        self.balance = initial_amount
        self.name = acnt_name
        print(f'\n Account {self.name} created.\n Balance = ${self.balance:.2f}')
        
    def check_balance(self):
        print(f'\n Account {self.name} .\n Balance = ${self.balance:.2f}')
        
    def deposit_amnt(self, deposit_amnt):
       self.balance += deposit_amnt
       print('\nDeposit complete.')
       self.check_balance()
       
    def viable_transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, account {self.name} has only ${self.balance}.")
            
    def withdrawl(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("Withdrawl complete\n")
            self.check_balance()
        except BalanceException as error:
            print(f'Withdraw interrupted: {error}') 
            
    def transfer(self,amt,name):
        try:
            print("\n*******\n\nBeginning transfer..")
            self.viable_transaction(amt)
            self.withdrawl(amt)
            name.deposit_amnt(amt)
            print('Transfer complete')
        except BalanceException as error:
            print("\nTransfer interrupted\n\n*********")
        
        
John = BankAccount(1000,'John')
James = BankAccount(2000,'James')

James.withdrawl(200)

John.transfer(300,James)