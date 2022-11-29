class Category:
    nome = ''
    
    ledger = list()
    
    percent = 0
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

# Método extralista 
def create_spend_chart(list_of_categories = []):
    if list_of_categories == []:
        print("Percentage spent by category")
        for i in range(11):
            print(f"{abs((i-10))*10:>3}|\n",end='')
        print(" "*4+'---')
    else:
        total = 0
        for category in list_of_categories:
            total+= abs(category.loss)
        for category in list_of_categories:    
            percent = abs(round(category.loss / total,2))*100
            category.percent += percent
        for category in list_of_categories:
            
            tabela=f'''
            {100:>3}|{} {} {}
            {90:>3}| {} {} {}
            {80:>3}| {} {} {} 
            {70:>3}| {} {} {}
            {60:>3}| {} {} {}
            {50:>3}| {} {} {}
            {40:>3}| {} {} {}
            {30:>3}| {} {} {}
            {20:>3}| {} {} {}
            {10:>3}| {} {} {}
            {0:>3}|  {} {} {}
            '''

food = Category('food')
entertainment = Category('entertainment')
business = Category('business')

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

create_spend_chart([food, entertainment, business])
print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
