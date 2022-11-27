class Category:
    nome = ''
    
    ledger = list()
    
    funds = 0
    
    loss = 0
    
    def __init__(self, nome_categoria):
        self.nome = nome_categoria
    
    def __str__(self):
        print(self.nome.center(30,'*'))
        for dic in self.ledger:
            linha = f"{dic['description'][:23]:<23}{dic['amount']:>7.2f}"
            print(linha)    
        total = f"total: {self.funds - self.loss:.2f}"
        print(total)
        return ''

    # Métodos
    def check_funds(self,amount):
        if self.funds < amount:
            return False
        else:
            return True 
        
    def deposit(self,amount,description=''):
        self.ledger.append({
            "amount": amount,
            "description": description
        })
        self.funds += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == True:
            self.ledger.append({
                "amount": - int(amount),
                "description": description
            })
            self.loss += - int(amount)
            return True
        else:
            return False
    
    def get_balance(self):
        return self.funds
    
    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.ledger.append({
                "amount": - int(amount),
                "description": f"Transfer to {category}"
            })
            self.loss += - int(amount)

            category.deposit(amount,description =f"Transfer to {category}")
            return True
        else:
            return False

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)