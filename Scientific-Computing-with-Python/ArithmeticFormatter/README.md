# Formatador Aritmético

Os alunos da escola primária geralmente organizam problemas de aritmética verticalmente para torná-los mais fáceis de resolver. Por exemplo, "235 + 52" se torna:

```Python
  235
+  52
-----
```


Crie uma função que receba uma lista de strings que são problemas aritméticos e retorne os problemas dispostos verticalmente e lado a lado. A função deve opcionalmente receber um segundo argumento. Quando o segundo argumento é definido como **True**, as respostas devem ser exibidas.

### Exemplo
---
Chamada de função:

```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

```

Resultado:

```python
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Chamada de função:

```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```


Resultado:

```python
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

### Regras
---
A função retornará a conversão correta se os problemas fornecidos estiverem formatados corretamente, caso contrário, retornará uma string que descreve um erro significativo para o usuário.

1. Situações que retornarão um erro:
  1. Se houver muitos problemas fornecidos à função. O limite é cinco , qualquer coisa mais retornará: **Error: Too many problems**.
  2. Os operadores apropriados que a função aceitará são **adição** e **subtração** . A multiplicação e a divisão retornarão um erro. Outros operadores não mencionados neste ponto não precisarão ser testados. O erro retornado será: **Error: Operator must be '+' or '-'**.
  3. Cada número (operando) deve conter apenas dígitos. Caso contrário, a função retornará: **Error: Numbers must only contain digits.**
  4. Cada operando (também conhecido como número em cada lado do operador) tem no máximo quatro dígitos de largura. Caso contrário, a string de erro retornada será: **Error: Numbers cannot be more than four digits.**


2. Se o usuário forneceu o formato correto dos problemas, a conversão que você retornar seguirá estas regras:
  1. Deve haver um único espaço entre o operador e o maior dos dois operandos, o operador estará na mesma linha do segundo operando, ambos os operandos estarão na mesma ordem fornecida (o primeiro será o de cima e o segundo será o fundo).
  2. Os números devem ser alinhados à direita.
  3. Deve haver quatro espaços entre cada problema.
  4. Deve haver traços na parte inferior de cada problema. Os traços devem percorrer toda a extensão de cada problema individualmente. (O exemplo acima mostra como isso deve ser.)

# Solução
---
Para construir esse formatador aritmético, criaremos uma função com dois argumentos:
- problemas : _deve ser uma lista_
- resp: _deve ser dado um valor booleano que por padrão é falso_

Ela retornará os problemas formatados. Assim, nossa função terá o seguinte modelo:
```Python
def arithmetic_arranger(problemas, respo=False):
    return arranged_problems
```

### Tratando os Erros
---
Iniciaremos a função tratando das restrições. Para a situação **1.A**., basta limitar o funcionamento da função quando a lista conter mais que cinco problemas. Isso é feito de maneira muito simples pelo código abaixo:


```python
if len(problemas) > 5:
    return "Error: Too many problems."
```

Para resolver a situação **1.B**, precisamos identificar os simbolos em cada problema da lista. Sabemos do ensino fundamental que na adição cada número é chamado de parcela. Assim, para cada problema da nossa lista, vamos criar três novas listas que separarão as parcelas dos simbolos. Como estamos trabalhando com subtração também a ordem vai importar, pois a operação de substração não satisfaz [comutatividade](https://pt.wikipedia.org/wiki/Comutatividade).

```python
parcela1, operador, parcela2  = [],[],[]
```

A parcela 1 será a primeira em ordem de leitura e o operador será '+' ou '-'. Para separá-los, usaremos um loop que percorrerá toda a lista de problemas, transformará cada problema em uma lista por meio do método _split()_ e adicionará os elementos em suas devidas listas que foram definidas acima pelo método _append()_.

```python
for problema in problemas:
    partes = problema.split()
    parcela1.append(partes[0])
    operador.append(partes[1])
    parcela2.append(partes[2])

```
Feito isso podemos tratar da situação **1.B**. O problema exige que tratemos apenas os casos das operações de multiplicação e divisão. Entretanto, da pra resolver um problema geral de maneira simples. Basta analisar a lista com os operadores e verificar se cada operador contêm '+' ou '-'. Caso não contenha nenhum dos dois, emitimos o erro.

```python
for i in operador:    
    if i not in '+' and i not in '-':
        return "Error: Operator must be '+' or '-'."

```
Para tratar o **1.C** usaremos o método _isdigit()_ que verifica se a string possui apenas dígitos e associando a um valor booleano. Logo, para cada algarismo de cada número na lista de parcela faremos essa verificação. Caso encontremos algo que não seja número retornará o erro.

```python

for i in range(len(parcela1)):
    if not (parcela1[i].isdigit() and parcela2[i].isdigit()):
        return "Error: Numbers must only contain digits."
```

Por fim, para **1.D**, percorreremos cada elemento nas listas de parcelas verificando se um ou outro possui mais que quatro digitos e retornará o erro.

```python
for i in range(len(parcela1)):
    if len(parcela1[i]) > 4 or len(parcela2[i]) > 4:
        return "Error: Numbers cannot be more than four digits."
```

### Formatação dos Problemas
---

A formatação para um único problema é muito simples de fazer utilizando as [f-strings](https://pythonacademy.com.br/blog/f-strings-no-python), entretanto não conseguimos por uma string ao lado da outra conforme a exigência **2.C**. Para solucionar isso, resolvi usar o método [_.join()_](https://www.programiz.com/python-programming/methods/string/join) e por isso tive que criar 4 linhas:

```Python
linha1, linha2, linha3, linha4 = [], [], [], []
```
Assim,
- linha 1 irá conter os números da parcela 1;
- linha 2 irá conter os operadores junto aos números da parcela 2;
- linha 3 irá conter os traços;
- linha 4 irá conter as soluções quando socilitada.

Para as exigências **2.A** e **2.B**, vamos precisar de alguns condicionais. Se o maior número for o primeiro, então devemos ter um espaço de distância dele para o sinal. Só que o sinal fica em baixo, então precisaremos de mais um espaço para manter os número alinhados à direita. Em código:

```Python
if len(parcela1[i]) > len(parcela2[i]):
    linha1.append(" "*2 + parcela1[i])
```

Por outro lado, caso o primeiro não seja maior, então ele deve ser menor ou igual. Assim, por meio de alguns destes, consegui deduzir que a quantidade de espaços necessária será o número de digitos do segundo(que será maior ou igual) menos o número de dígitos do primeiro mais 2. O que nos dá o seguinte código:

```Python
else:
    linha1.append(" "*(len(parcela2[i]) - len(parcela1[i]) + 2) + parcela1[i])

```
Como faremos isso para todos os problemas nosso bloco de códico fica assim:


```Python
for i in range(len(parcela1)):
    if len(parcela1[i]) > len(parcela2[i]):
        linha1.append(" "*2 + parcela1[i])
    else:
        linha1.append(" "*(len(parcela2[i]) - len(parcela1[i]) + 2) + parcela1[i])
```
Faremos algo totalmente análogo para formatar a linha, lembrando apenas de incluir o operador:


```Python
for i in range(len(parcela2)):
    if len(parcela2[i]) > len(parcela1[i]):
        linha2.append(operador[i] + " " + parcela2[i])
    else:
        linha2.append(operador[i] + " "*(len(parcela1[i]) - len(parcela2[i]) + 1) + parcela2[i])
```

Para a exigência **2.D** adicionar à terceira linha o número de traços corresponte ao maior número de digitos dos números analisados mais 2:

```Python
for i in range(len(parcela1)):
    linha3.append("-"*(max(len(parcela1[i]), len(parcela2[i])) + 2))

```

Assim, podemos definir o _arranged_problemas_ da seguinte forma:

```Python
arranged_problems = (4*" ").join(linha1) + "\n" + (4*" ").join(linha2) + "\n" + (4*" ").join(linha3)

```
Isso acabaria com nosso desafio se não tivéssemos o argumento opcional que por padrão é _False_. Para nossa sorte, resolver isso é fácil e auto explicativo como segue:

```Python
if resp == True:
    for i in range(len(parcela1)):
        if operador[i] == "+":
            ans = str(int(parcela1[i]) + int(parcela2[i]))
        else:
            ans = str(int(parcela1[i]) - int(parcela2[i]))

        if len(ans) > max(len(parcela1[i]), len(parcela2[i])):
            linha4.append(" " + ans)
        else:
            linha4.append(" "*(max(len(parcela1[i]), len(parcela2[i])) - len(ans) + 2) + ans)
    arranged_problems = (4*" ").join(linha1) + "\n" + (4*" ").join(linha2) + "\n" + (4*" ").join(linha3) + "\n" + (4*" ").join(linha4)
else:
    arranged_problems = (4*" ").join(linha1) + "\n" + (4*" ").join(linha2) + "\n" + (4*" ").join(linha3)

```
Isso termina nosso desafio!

## Código Completo


```python
def arithmetic_arranger(problemas, resp=False):
    if len(problemas) > 5:
        return "Error: Too many problems."
    
    parcela1, operador, parcela2  = [],[],[]

    for problema in problemas:
        partes = problema.split()
        parcela1.append(partes[0])
        operador.append(partes[1])
        parcela2.append(partes[2])

    # Verificando os erros
    # Exigencia dos operadores
    for i in operador:    
        if i not in '+' and i not in '-':
            return "Error: Operator must be '+' or '-'."

    # Exigência dos dígitos
    for i in range(len(parcela1)):
        if not (parcela1[i].isdigit() and parcela2[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Números com 4 dígitos 
    for i in range(len(parcela1)):
        if len(parcela1[i]) > 4 or len(parcela2[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    linha1, linha2, linha3, linha4 = [], [], [], []
    
    # Formatação das linhas
    for i in range(len(parcela1)):
        if len(parcela1[i]) > len(parcela2[i]):
            linha1.append(" "*2 + parcela1[i])
        else:
            linha1.append(" "*(len(parcela2[i]) - len(parcela1[i]) + 2) + parcela1[i])

    for i in range(len(parcela2)):
        if len(parcela2[i]) > len(parcela1[i]):
            linha2.append(operador[i] + " " + parcela2[i])
        else:
            linha2.append(operador[i] + " "*(len(parcela1[i]) - len(parcela2[i]) + 1) + parcela2[i])

    for i in range(len(parcela1)):
        linha3.append("-"*(max(len(parcela1[i]), len(parcela2[i])) + 2))
    
    # Pondo as soluções dos problemas
    if resp == True:
        for i in range(len(parcela1)):
            if operador[i] == "+":
                ans = str(int(parcela1[i]) + int(parcela2[i]))
            else:
                ans = str(int(parcela1[i]) - int(parcela2[i]))

            if len(ans) > max(len(parcela1[i]), len(parcela2[i])):
                linha4.append(" " + ans)
            else:
                linha4.append(" "*(max(len(parcela1[i]), len(parcela2[i])) - len(ans) + 2) + ans)
        arranged_problems = (4*" ").join(linha1) + "\n" + (4*" ").join(linha2) + "\n" + (4*" ").join(linha3) + "\n" + (4*" ").join(linha4)
    else:
        arranged_problems = (4*" ").join(linha1) + "\n" + (4*" ").join(linha2) + "\n" + (4*" ").join(linha3)
    return arranged_problems

```
