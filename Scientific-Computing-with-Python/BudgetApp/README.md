# Aplicativo de Orçamento

### Instruções
---
Conclua a **Category** aula em budget.py. Ele deve ser capaz de instanciar objetos com base em diferentes categorias de orçamento, como _alimentação , vestuário e entretenimento_ . Quando os objetos são criados, eles são passados ​​no nome da categoria. A classe deve ter uma variável de instância chamada **ledger** que é uma lista. A classe também deve conter os seguintes métodos:

- Um **deposit** método que aceita um valor e uma descrição. Se nenhuma descrição for fornecida, o padrão deve ser uma string vazia. O método deve anexar um objeto à lista de **ledger** na forma de **{"amount": amount, "description": description}.**
- Um **withdraw** método que é semelhante ao **deposit** método, mas o valor passado deve ser armazenado no razão como um número negativo. Se não houver fundos suficientes, nada deve ser adicionado ao livro razão. Este método deve retornar **True** se a retirada ocorreu e **False** caso contrário.
- Um **get_balance** método que retorna o saldo atual da categoria de orçamento com base nos depósitos e saques ocorridos.
- Um **transfer** método que aceita um valor e outra categoria de orçamento como argumentos. O método deve adicionar um saque com o valor e a descrição **"Transfer to \[Destination Budget Category\]"**. O método deve então adicionar um depósito à outra categoria de orçamento com o valor e a descrição "Transfer from [Source Budget Category]". Se não houver fundos suficientes, nada deve ser adicionado a nenhum dos livros contábeis. Este método deve retornar **True** se a transferência ocorreu e **False** caso contrário.
- Um **check_funds** método que aceita um valor como argumento. Retorna **False** se o valor for maior que o saldo da categoria orçamentária e retorna **True** caso contrário. Este método deve ser usado tanto pelo **withdraw** método quanto pelo **transfer** método.

Quando o objeto de orçamento for impresso, ele deve exibir:

- Uma linha de título de 30 caracteres onde o nome da categoria é centralizado em uma linha de ***** caracteres.
- Uma lista dos itens no razão. Cada linha deve mostrar a descrição e o valor. Os primeiros 23 caracteres da descrição devem ser exibidos e, em seguida, o valor. A quantidade deve estar alinhada à direita, conter duas casas decimais e exibir no máximo 7 caracteres.
- Uma linha exibindo o total da categoria.

Aqui está um exemplo da saída:
~~~
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
~~~
    
Além da **Category** classe, crie uma função (fora da classe) chamada **create_spend_chart** que receba uma lista de categorias como argumento. Ele deve retornar uma string que é um gráfico de barras.

O gráfico deve mostrar o percentual gasto em cada categoria repassado para a função. A porcentagem gasta deve ser calculada apenas com saques e não com depósitos. No lado esquerdo do gráfico, devem estar os rótulos de 0 a 100. As "barras" no gráfico de barras devem ser feitas com o caractere "o". A altura de cada barra deve ser arredondada para o 10 mais próximo. A linha horizontal abaixo das barras deve passar dois espaços após a barra final. Cada nome de categoria deve ser escrito verticalmente abaixo da barra. Deve haver um título no topo que diga "Percentage spent by category".

Esta função será testada com até quatro categorias.

Observe a saída de exemplo abaixo com atenção e certifique-se de que o espaçamento da saída corresponda exatamente ao exemplo.

~~~
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g
~~~

# Solução
---

## Criação da Classe

A parte inicial do nosso código é bem simples. Basta criar uma classe chamada de _Category_ de forma que cada elemento receba um parâmetro ao ser instanciado e esse parâmetro será o nome da classe e também seja criada uma lista vazia chamada _ledger_.

~~~Python
class Category:
    def __init__(self,category_name):
        self.name = category_name
        self.ledger = list()
    return None
~~~

## Definindo dos Métodos da Classe
---
### Método deposit
O primeiro método é feito da maneira que as instruções indicam sem nenhuma dificuldade. Como precisaremos imprimir um valor total por objeto instanciado, vou adicionar nela uma variável de classe chamada _funds_ que guardará todos os depositos feitos no objeto.

~~~Python
    def deposit(self,amount,description= ""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })
        self.funds += amount
        return self.ledger
~~~

### Método check_funds

~~~Python
    def check_funds(self,amount):
        if self.funds < amount:
            return False
        else:
            return True 
 
~~~

### Método withdraw

Usando o método _check_funds_, podemos criar nosso médoto _withdraw_ sem dificuldade. Para isso, vamos criar uma variável de classe chamada _loss_ e nela será armazenado todo o valor que for sacado do objeto.
~~~Python
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
~~~

### Método get_balance

Este método faz o display do saldo atual. Assim, basta imprimir a diferença entre as variáveis _funds_ e _loss_ que definimos anteriormente nos métodos _deposit_ e _withdraw_, respectivamente.

~~~Python
    def get_balance(self):
        total = self.funds - self.loss
        return total
~~~
### Método transfer
Este método precisa do _check_funds_ para verificar se há saldos suficientes. Caso haja, adicionamos o valor á variável _loss_ e, em seguida, com o mesmo valor fazemos um depósito à categoria passada como parâmetro.

~~~Python
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

~~~

## Impressão do Objeto
---
Para imprimir o objeto conforme as instruções, precisamos modificar o método especial __str__.

Para manter o nome centralizado por _*_ basta usar o método _center_ no nome do objeto. Em seguida, queremos imprimir uma lista de movimentações que foram feitas no objeto da classe. Para isso, criaremos uma lista vazia _nota fiscal_ e, através de um loop for, percorreremos todos os elementos da lista _ledger_ definida no método construtor pondo as formatações exigidas no projeto e adicionará cada uma dessas interações na lista 
_nota fiscal_. Em seguida, criaremos uma variável _total_ que armazenará o saldo atual naquele objeto, ou seja, armazenará o resultado o método _get_balance_. Em seguida, retornaremos o título, os elementos da lista _nota_fiscal_ em forma de string e o total. O código ficará assim:
~~~Python
    def __str__(self):
        title = self.name.center(30,'*')+'\n'
        invoice = []
        for dic in self.ledger:
            line = f"{dic['description'][:23]:<23}{dic['amount']:>7.2f}"
            invoice.append(line+'\n')    
        total = f"Total: {self.funds - self.loss:.2f}"
        return title+''.join(invoice)+total

~~~

### Código 
Organizando o código até aqui temos:

~~~Python
class Category:
    # Métodos Especiais
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

    # Métodos da classe
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


~~~

## Criando o gráfico de gastos
---
### Associando as porcentagens de gasto em cada objeto
Vamos começar pondo o titulo do gráfico em uma variável e uma lista com espaços que chamaremos de _spaces_ e sua contrução será justificada a posteriori. Em seguida, a estratégia que eu utilizei foi criar varías listas formando uma matriz e imprimir a matriz trasposta. A primeira lista é a de _rotulos_ nela irá conter as porcentagens. Em seguida, criei 4 listas todas com elementos ' '.
~~~Python
def create_spend_chart(list_of_categories = []):
    title = 'Percentage spent by category\n'
    spaces = ['' for i in range(11)]
    rotulos = [f'{(10-i)*10:>3}|' for i in range(11)]
    col1 = [' ' for i in range(11)]
    col2 = [' ' for i in range(11)]
    col3 = [' ' for i in range(11)]
    col4 = [' ' for i in range(11)]

~~~

Como é um gráfico de gastos, precisamos calcular o gasto total de cada categoria para criarmos as porcentagens. Criamos uma variável chamada _spent_total_ que será o gasto total e para cada categoria no parâmetro _list_of_categories_ vamos somar a variável de instancia _loss_. Assim, teremos
~~~Python
    spent_total = 0
    for category in list_of_categories:
        spent_total += category.loss
~~~

Vamos criar uma variável de instância chamada _spent_percent_ e associaremos a porcentagem do valor gasto em cada categoria em relação ao total nela. Para isso, basta dividir _loss_ pelo _spent_total_ em todas as categorias e multiplicar por 100. Para arrendondar ao 10 mais próximo usamos a função _round_.

~~~Python
    for category in list_of_categories:    
        category.percent = category.loss/ spent_total*100
        category.percent = round(category.percent,1)
        category.percent = int(category.percent)
~~~
É agora que entra o papel das nossas listas que foram criadas anteriormente. Faremos uma variável chamada _bar_level_ ela servirá para adicionarmos 'o' as listas que criamos anteriormente. Assim, faremos um loop por meio do atributo percent de cada elemento que associará quantas 'o' serão inseridas nas nossas listas. Conforme os elementos da lista de categorias vão mudando inserimos 'o' em listas diferentes.
~~~Python
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
~~~
Criamos apenas as listas, mas a impressão pedida não são várias listas e sim colunas. Assim, criaremos uma variável chamada _table_ nela transformaremos nossas listas em colunas por meio do método _zip_ e entra aqui a justificativa de termos criado a lista _spaces_. Ela servirá para por os espaços entre uma coluna e outra que a instrução pede como segue:

~~~Python
    table = ''
    for (a,b,c,d,e,f,g,h) in zip(rotulos,col1,space,col2,space,col3,space,col4):
        table +=' '.join((a,b,c,d,e,f,g,h))+'\n'

~~~
Para separar o gráfico da legenda, temos uma linha que deve adequar-se conforme os elementos sejam adicionados não podendo ultrapassar 4 categorias. Para isso, criaremos uma variável chamada de _num_line_. Ela terá um valor inicial de 0 e será acrescido 3 se cada uma das colunas que criamos anteriormente não estiver vazia. Para finalizar a impressão criaremos uma f-string chamada _sep_line_ que será nossa linha de divisão. O código encontra-se abaixo:

~~~Python
    num_line = 0
    if 'o' in col2:
        num_line+=3
    if 'o' in col3:
        num_line+=3
    if 'o' in col4:
        num_line+=3
    sep_line = f"{4*' '}----{num_line*'-'}"
~~~

Agora trataremos de fazer a construção da legenda. Bem, as legendas, bem como as colunas serão construídas conforme a quantidade de categorias passadas na lista de parâmetro da função. Nosso intuito é utilizar novamente a função _zip_ para construir essa parte do código que nem fizemos com a variável _table_. Anteriormente não tivemos problemas com isso, pois as listas tinham o mesmo comprimento. Aqui, os nomes da classe são de tamanhos diferentes. Dessa forma, precisamos armazenar em uma variável o comprimento do maior para que possamos criar novamente uma matriz e transpôr-la usando o _zip_. 

~~~Python
    len_big_category = 0
    for category in list_of_categories:
        if len(category.name) > len_big_category:
            len_big_category = len(category.name)

~~~


Essa preocupação ocorre aqui porque a função _zip_ para a interação quando o menor elemento é todo percorrido. Assim, por exemplo, se tivessemos duas categorias chamadas 'automóvel' e 'comida' a palavra automóvel sairia imcompleta por ser maior que comida. 

Com isso, criaremos uma nova lista com espaços vazios que terá o mesmo tamanho da maior categoria. Criaremos uma lista que servirá de matriz com o nome _subtitle_names_. Definiremos uma variável de interação _i_ e, por meio de um loop for, vamos percorrer todos os elemetnos da _list_of_categories_, criando uma lista chamada _letters_category_ com as letras do nome da categoriae adicionaremos elas na lista _subtitle_names_.
~~~Python
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
~~~
Finalmente criaremos uma string chamada _subtitle_ que será composta de todos os elementos da matriz transposta de _subtitle_names_ que chamaremos de _t_subtitles_names_
~~~Python
    subtitle = ''
    t_subtitle_names = list(map(list,zip(*subtitle_names)))

    for i in t_subtitle_names:
        if i == t_subtitle_names[len(t_subtitle_names)-1]:
            subtitle += ' '.join(i)
        else:
            subtitle += ' '.join(i)+'\n'
~~~


Por fim, retornaremos 
~~~Python 
return title+table+sep_line+'\n'+subtitle
~~~


## Código Completo
---
~~~Python
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
~~~
