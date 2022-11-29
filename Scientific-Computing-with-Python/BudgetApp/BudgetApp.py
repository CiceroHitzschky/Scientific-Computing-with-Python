import numpy as np
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
        
    def deposit(self,amount,description='initial deposit'):
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
    def adicionar(self,valor):
        self.percent = self.percent + valor
        
        
        
# Método extralista 
def create_spend_chart(list_of_categories = []):
    rotulos = [f'{(10-i)*10:>3}|' for i in range(10)]
    col1 = [' ' for i in range(11)]
    col2 = [' ' for i in range(11)]
    col3 = [' ' for i in range(11)]
    col4 = [' ' for i in range(11)]
    
    if list_of_categories == []:
#         print("Percentage spent by category")
        for i in range(11):
            print(f"{abs((i-10))*10:>3}|\n",end='')
        print(" "*4+'---')
    else:
        total = 0
        for category in list_of_categories:
            total += abs(category.loss)
            # ok
        for category in list_of_categories:    
            percento = round(abs(category.loss) / total,2)*100
            percento = int(percento)
            t = category.adicionar(percento)
            print(category.percent+1)
        for i in range(len(list_of_categories)):
            if i == 0:
                n_ball = round(list_of_categories[i].percent/10)
                for j in range(n_ball+1):
                    col1[-1-j] = col1[j].replace(' ','o') 
            if i == 1:
                n_ball = round(list_of_categories[i].percent/10)
                
                for j in range(n_ball+1):
                    col2[-1-j] = col2[j].replace(' ','o') 
            if i == 2:
                n_ball = round(list_of_categories[i].percent/10)
                
                for j in range(n_ball+1):
                    col3[-1-j] = col3[j].replace(' ','o') 
            if i == 3:
                n_ball = round(list_of_categories[i].percent/10)
                for j in range(n_ball+1):
                    col4[-1-j] = col4[j].replace(' ','o') 

        # Bolas do Gráfico
        table = f"""Percentage spent by category
100| {col1[0]}  {col2[0]}  {col3[0]}  {col4[0]}         
 90| {col1[1]}  {col2[1]}  {col3[1]}  {col4[1]}         
 80| {col1[2]}  {col2[2]}  {col3[2]}  {col4[2]}         
 70| {col1[3]}  {col2[3]}  {col3[3]}  {col4[3]}
 60| {col1[4]}  {col2[4]}  {col3[4]}  {col4[4]}
 50| {col1[5]}  {col2[5]}  {col3[5]}  {col4[5]}
 40| {col1[6]}  {col2[6]}  {col3[6]}  {col4[6]}
 30| {col1[7]}  {col2[7]}  {col3[7]}  {col4[7]}
 20| {col1[8]}  {col2[8]}  {col3[8]}  {col4[8]}
 10| {col1[9]}  {col2[9]}  {col3[9]}  {col4[9]}
  0| {col1[10]}  {col2[10]}  {col3[10]}  {col4[10]}   
"""        
        constant = 0
        if 'o' in col2:
            constant+=3
        if 'o' in col3:
            constant+=3
        if 'o' in col4:
            constant+=3
        # Linha de baixo
        linha = f"{3*' '}----{constant*'-'}"
        print(table,linha)


        k = 0
        for category in list_of_categories:
            if len(category.nome) > k:
                k = len(category.nome)
        
        nomes_categorias = [[4*' ' for i in range(k)]]
        
        l = 0
        while l < len(list_of_categories):
            lista = [i for i in list_of_categories[l].nome.capitalize()]
            if len(lista) < k:
                for i in range(k - len(lista)):
                    lista.append(' ')
            nomes_categorias.append(lista)
            nomes_categorias.append(['' for i in range(k)])
            l = l+1
        matrix = np.array(nomes_categorias)
        for i in matrix.T:
            print(' '.join(i))
        