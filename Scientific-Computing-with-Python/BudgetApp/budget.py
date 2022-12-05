class Category:
    # Especial Methods
    def __init__(self, category_name):
        self.name = category_name
        self.ledger = list()
        self.funds, self.loss = 0,0
        
    def __str__(self):
        title = self.name.center(30,'*')+'\n'
        invoice = []
        for dic in self.ledger:
            line = f"{dic['description'][:23]:<23}{dic['amount']:>7.2f}"
            invoice.append(line+'\n')    
        total = f"Total: {self.funds - self.loss:.2f}"
        return title+''.join(invoice)+total

    # Class Methods
    def check_funds(self,amount):
        if self.funds < amount:
            return False
        else:
            return True 
        
    def deposit(self,amount,description= ""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })
        self.funds += amount
        return self.ledger
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == True:
            self.ledger.append({
                "amount": - float(amount),
                "description": description
            })
            self.loss += float(amount)
            return True
        else:
            return False
    
    def get_balance(self):
        total = self.funds - self.loss
        return total
    
    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.ledger.append({
                "amount": - float(amount),
                "description": f"Transfer to {category_name}"
            })
            self.loss += float(amount)

            category.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False    
        

# Creating Spend Chart
def create_spend_chart(list_of_categories = []):
    title = 'Percentage spent by category\n'
    spaces = ['' for i in range(11)]
    labels = [f'{(10-i)*10:>3}|' for i in range(11)]
    spaces = ['' for i in range(11)]
    col1 = [' ' for i in range(11)]
    col2 = [' ' for i in range(11)]
    col3 = [' ' for i in range(11)]
    col4 = [' ' for i in range(11)]
    
    # Defining Percentages
    total = 0
    for category in list_of_categories:
        total += category.loss

    for category in list_of_categories:    
        category.percent = category.loss/ total*100
        category.percent = round(category.percent,1)
        category.percent = int(category.percent)
        
    # Putting balls into lists
    for i in range(len(list_of_categories)):
        if i == 0:
            bar_level = round(list_of_categories[i].percent/10)+1
            for j in range(bar_level):
                col1.insert(11-bar_level,'o')
        elif i == 1:
            bar_level = round(list_of_categories[i].percent/10)+1
            for j in range(bar_level):
                col2.insert(11-bar_level,'o')
        elif i == 2:
            bar_level = round(list_of_categories[i].percent/10)+1
            for j in range(bar_level):
                col3.insert(11-bar_level,'o')
        else:
            bar_level = round(list_of_categories[i].percent/10)+1
            for j in range(bar_level):
                col4.insert(11-bar_level,'o')
                
    # Defining Bars
    table = ''
    for (a,b,c,d,e,f,g,h) in zip(labels,col1,spaces,col2,spaces,col3,spaces,col4):
        table +=' '.join((a,b,c,d,e,f,g,h))+'\n'
    
    # Separation Line
    num_line = 0

    if 'o' in col2:
        num_line+=3
    if 'o' in col3:
        num_line+=3
    if 'o' in col4:
        num_line+=3

    sep_line = f"{4*' '}----{num_line*'-'}"

    # Labels of Columns
    len_big_category = 0
    for category in list_of_categories:
        if len(category.name) > len_big_category:
            len_big_category = len(category.name)

    subtitle_names = [[4*' ' for i in range(len_big_category)]]
    i = 0
    while i < len(list_of_categories):
        letters_category = [j for j in list_of_categories[i].name.capitalize()]
        if len(letters_category) < len_big_category:
            for j in range(len_big_category - len(letters_category)):
                letters_category.append(' ')
        subtitle_names.append(letters_category)
        subtitle_names.append(['' for j in range(len_big_category)])
        i += 1 

    subtitle = ''
    t_subtitle_names = list(map(list,zip(*subtitle_names)))

    for i in t_subtitle_names:
        if i == t_subtitle_names[len(t_subtitle_names)-1]:
            subtitle += ' '.join(i)
        else:
            subtitle += ' '.join(i)+'\n'

    return title+table+sep_line+'\n'+subtitle
