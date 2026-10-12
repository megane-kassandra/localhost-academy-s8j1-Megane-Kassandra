class BankAccount:
    
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
        
    def show_balance(self):
        print(f"Solde de {self.owner} : {self.balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depot effectue : {amount}")
        else:
            print("Montant invalide")
        
account = BankAccount("Alice", 1000)
account.show_balance()
account.deposit(500)
account.show_balance()
account.deposit(-100)
account.show_balance()