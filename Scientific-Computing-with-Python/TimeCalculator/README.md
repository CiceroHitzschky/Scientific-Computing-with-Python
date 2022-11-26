# Calculadora de tempo by Cícero Hitzschky

## Instruções 
---
Escreva uma função chamada _add_time_ que receba dois parâmetros obrigatórios e um parâmetro opcional:


- uma hora de início no formato de relógio de 12 horas (terminando em AM ou PM)
- um tempo de duração que indica o número de horas e minutos
- (opcional) um dia inicial da semana, sem distinção entre maiúsculas e minúsculas


A função deve adicionar o tempo de duração ao horário de início e retornar o resultado.

Se o resultado for no dia seguinte, deve aparecer **(next day)** após o horário. Se o resultado for mais de um dia depois, ele deve aparecer **(n days later)** depois da hora, onde "n" é o número de dias depois.

Se a função receber o parâmetro opcional do dia inicial da semana, a saída deverá exibir o dia da semana do resultado. O dia da semana na saída deve aparecer após a hora e antes do número de dias depois.

## Exemplos
---
Abaixo estão alguns exemplos de diferentes casos que a função deve tratar. Preste muita atenção ao espaçamento e pontuação dos resultados.

```Python
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

Não importe nenhuma biblioteca Python. Suponha que os horários de início sejam horários válidos. Os minutos no tempo de duração serão um número inteiro menor que 60, mas a hora pode ser qualquer número inteiro.

---


## Solução
---

O modelo já nos apresenta um modelo básico de função

```Python
def add_time(start, duration):
    return new_time
```

### Obtendo novo tempo
---
Para conseguir atender às exigências das regras optei por trabalhar em minutos. Para isso, peguei a string que vem da entrada _start_ e _duration_ e as separei usando o _split()_ com o separador _
Para conseguir atender às exigências das regras optei por trabalhar em minutos. Para isso, observei que a entrada em _start_ é uma string que possui uma parte numérica e outra parte que fala do tempo (PM ou AM). Logo, usei o método _split()_ para separa os algarismos do periodo. Isso gerou uma lista com dois elementos cujo primeiro é o horário inicial. Esse elemento é do tipo _00:00_. Assim, separer 'quebrei' a string em duas separando as horas dos minutos. Fiz o mesmo com a entrada da variável _duration_.

```Python
    starts = start.split()
    hora_start = starts[0].split(':')
    durations = duration.split(':')
```
Daí, tranformei tudo em minuto para ficar mais fácil de trabalhar uma vez que a divisão de horas e minutos na string impossibilitada isso. A transformação é feita de maneira simples. Basta notar que cada hora tem 60 minutos. Assim, se tivermos a entrada de _03:32_ é o mesmo que _3h32min_. Logo, 

$$
3h32min = 03\cdot60min + 32min = 180min + 32min = 212min
$$
Traduzindo isso em código, temos:

```Python
    hora_start_min = int(hora[0])*60 + int(hora[1])
    duration_min = int(durations[0])*60 + int(durations[1])
    total_minutos = hora_start_min + duration_min
```
Bom, temos que voltar para a formatação antiga, então vou utilizar a operação módulo para extrair a quantidade de horas que obtemos com o _total_minutos_ e o por em uma nova variável e o que sobrar dos minutos vamos atribuir a uma outra variável.

```Python
    new_hora = int(total_minutos/60)%12
    new_min = total_minutos%60
    
```
Além disso, precisamos organizar a formatação, pois com estamos trabalhando com módulo não temos o número 12 de resposta e isso prejudica e também o resultado dos minutos é um número inteiro e números inteiros menores que 10 não possuem um zero na frente. Ao organizar essa formatação ficamos com o seguinte bloco de código:
```Python
def add_time(start, duration):
    # Fazendo a adição do tempo (start + duration)
    starts = start.split()
    hora_start = starts[0].split(':')
    durations = duration.split(':')
    hora_start_min = int(hora[0])*60 + int(hora[1])
    duration_min = int(durations[0])*60 + int(durations[1])
    total_minutos = hora_start_min + duration_min
    new_hora = int(total_minutos/60)%12
    new_min = total_minutos%60
    
    # Organizando a formatação
    if new_hora == 0:
        new_hora ='12'

    if len(str(new_min)) < 2:
        new_min = '0'+str(new_min)
        
    end_hora = f"{new_hora}:{new_min}"    
        
    return new_time

```



### Ante Meridiem e Post Meridiem
---
Na parte acima o que fizemos foi apenas por o tempo indicando as horas e os minutos. Precisamos dizer se o novo tempo é de manhã(AM) ou pela tarde(PM). Para isso, utilizei novamente os minutos como uma espécie de chave seletora. O período muda a cada 12h, ou seja, a cada 720min. Assim, criei o seguinte condicional:

```Python

    if (starts[1] == 'PM' and total_minutos > 720):
        periodo = 'AM'  
    elif starts[1] == 'PM' and total_minutos <= 720:
        periodo = 'PM'
    elif (starts[1] == 'AM' and total_minutos > 720):
        periodo = 'PM'
    elif starts[1] == 'AM' and total_minutos < 720:
        periodo = 'AM'
    else:
        periodo = starts[1]
```

Basicamente o código fala: "se o periodo é PM e passaram mais que 12h, então troque para AM". O análogo ocorre caso o perído seja "AM". Isso funcionou em todos os casos dos exemplos acima. Entretanto, falhou nos testes da plataforma. O bloco falhava porque quando passavam 24h, i.e, 1440min, o período mudava, pois 1440 > 720. Só que se mudamos 24h paramos na mesma hora só que no dia seguinte. Para resolver isso, acresci mais uma condição:

```Python

    if (starts[1] == 'PM' and total_minutos > 720) and duration_min != 1440:
        periodo = 'AM'  
    elif starts[1] == 'PM' and total_minutos <= 720:
        periodo = 'PM'
    elif (starts[1] == 'AM' and total_minutos > 720)and duration_min != 1440:
        periodo = 'PM'
    elif starts[1] == 'AM' and total_minutos < 720:
        periodo = 'AM'
    else:
        periodo = starts[1]
```



### Contagem dos Dias
---
Agora vamos atender a exigência da contagem de dias. Isso é bem simples de fazer. Basta pegarmos a quantidade de minutos na entrada _duraton_ e dividir por 1440, que é 24h em minutos. Isso gerará um número do tipo float. Assim, vamos tirar a parte inteira dele por meio da função _int()_ e, em seguida, verificar se o que sobra dos minutos com os minutos da entrada _start_ formam ou não mais um dia. Traduzindo isso em código temos:

~~~Python
    n_dias = int(minutos_duracao/1440)
    decimal_n_dias = float(minutos_duracao/1440) - n_dias
~~~
Os valores acima estão em dias. Como estamos comparando em minutos vamos converter o que sobra para minutos. Claramente o que sobra não é maior que 1440min, pois é o resto da divisão. Assim, precisamos saber apenas se o período é de tarde e o que sobra ultrapassa 720min. Caso isso ocorra adicionamos mais um dia a quantidade de dias que contamos antes. Caso não ocorra, essa quantidade de dias é a quantidade final.

~~~Python
    decimal_n_dias_min = decimal_n_dias*1440
    juncao_com_resto = hora_start_min + decimal_n_dias_min
    
    if starts[1] == 'PM' and juncao_com_resto > 720:
        n_dias += 1
~~~        
Pronto, agora falta por as mensagens de formatação. Se não mudarmos de dia, nada muda. Caso, o tempo final fique no dia seguinte colocaremos _(next day)_ e se for mais que um dia daremos a quantidade dos dias juntamente com a mensagem _days later_.    

~~~Python
    if n_dias == 1:
        day_later = '(next day)'
    elif n_dias == 0 and juncao_com_resto < 720:
        day_later = ''
    elif n_dias == 0 and juncao_com_resto >= 720:
        day_later = ''    
    else:
        day_later = f'({n_dias} days later)'
~~~
Se desprezarmos o argumento opcinal da função, ela funciona perfeitamente com todas as outras exigências. Para finalizar o desafio, vamos atender as exigências do argumento opcional.


### Argumento Opcional
---
O argumento posicional é um dia. Na função associaremos, caso não seja passado, há uma string vazia _day=None_.
De cara, já podemos associar à variável _new_time_ o resultado final, caso o parêmetro _day_ não seja passado.

~~~Python
    if dia == '' and n_dias ==0:
        new_time = end_hora+' '+periodo
    elif dia == '' and n_dias !=0:
        new_time = end_hora+' '+periodo+' '+day_later       
~~~

Se o argumento for dado, não podemos deixar a função _case_sensitive_. Como as regras querem o resultado do dia com  a primeira letra maiúscula, vamos usar a função _capitalize()_. A função quer que ao indicar o número de dias percorridos, digamos também em qual dia da semana cai. Por exemplo, se o dia for terça e o tempo nos der 2 dias depois, então temos que imprimir na tela quinta. Para fazer isso, eu criei um dicionário que associa os números 0 à 6 aos dias da semana, respectivamente. Assim, vou analisar a classe residual dos restos por meio da operando o número de dias mais o índice via módulo. Isso me dará uma chave, que eu vou buscar no dicionário o valor que retornará o dia da semana desejado. Em código, teremos 


~~~Python
    week = {
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }
 
    if day == None and n_dias ==0:
        new_time = end_hora+' '+periodo

    elif day == None and n_dias !=0:
        new_time = end_hora+' '+periodo+' '+day_later

    
    elif day != None and n_dias ==0:
        day = day.capitalize()
        for k,v in week.items():
            if v == day:
                new_day_key = (k + n_dias)%7
                new_day = f', {week[new_day_key]}'        
        new_day = f', {week[new_day_key]}'  
        new_time = end_hora+' '+periodo+new_day

    else:    
        day = day.capitalize()
        for k,v in week.items():
            if v == day:
                new_day_key = (k + n_dias)%7
                new_day = f', {week[new_day_key]}'        
        new_day = f', {week[new_day_key]}'  
        new_time = end_hora+' '+periodo+new_day+' '+day_later
~~~
E assim, concluímos o desafio.

## Código Completo
---
~~~Python
## Código Completo

def add_time(start, duration,day=None):
    # Fazendo a adição do tempo (start + duration)
    
    starts = start.split()
    hora_start = starts[0].split(':')
    durations = duration.split(':')
    hora_start_min = int(hora_start[0])*60 + int(hora_start[1])
    duration_min = int(durations[0])*60 + int(durations[1])
    total_minutos = hora_start_min + duration_min
    new_hora = int(total_minutos/60)%12
    new_min = total_minutos%60

    # Organizando a formatação
    
    if new_hora == 0:
        new_hora ='12'

    if len(str(new_min)) < 2:
        new_min = '0'+str(new_min)

    end_hora = f"{new_hora}:{new_min}" 
    
    # Associando o périodo
    
    if (starts[1] == 'PM' and total_minutos > 720) and duration_min != 1440:
        periodo = 'AM'  
    elif starts[1] == 'PM' and total_minutos <= 720:
        periodo = 'PM'
    elif (starts[1] == 'AM' and total_minutos > 720)and duration_min != 1440:
        periodo = 'PM'
    elif starts[1] == 'AM' and total_minutos < 720:
        periodo = 'AM'
    else:
        periodo = starts[1]
  
    # Contagem dos dias

    n_dias = int(duration_min/1440)
    decimal_n_dias = float(duration_min/1440) - n_dias
    decimal_n_dias_min = decimal_n_dias*1440
    juncao_com_resto = hora_start_min + decimal_n_dias_min
    
    if starts[1] == 'PM' and juncao_com_resto > 720:
        n_dias += 1

    # Impressão da contagem dos dias
    
    if n_dias == 1:
        day_later = '(next day)'
    elif n_dias == 0 and juncao_com_resto < 720:
        day_later = ''
    elif n_dias == 0 and juncao_com_resto >= 720:
        day_later = ''    
    else:
        day_later = f'({n_dias} days later)'
    
    # Retorno se não há argumentos opcionais
    week = {
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }
 
    if day == None and n_dias ==0:
        new_time = end_hora+' '+periodo

    elif day == None and n_dias !=0:
        new_time = end_hora+' '+periodo+' '+day_later

    # Retorno com argumento opcional
    
    elif day != None and n_dias ==0:
        day = day.capitalize()
        for k,v in week.items():
            if v == day:
                new_day_key = (k + n_dias)%7
                new_day = f', {week[new_day_key]}'        
        new_day = f', {week[new_day_key]}'  
        new_time = end_hora+' '+periodo+new_day

    else:    
        day = day.capitalize()
        for k,v in week.items():
            if v == day:
                new_day_key = (k + n_dias)%7
                new_day = f', {week[new_day_key]}'        
        new_day = f', {week[new_day_key]}'  
        new_time = end_hora+' '+periodo+new_day+' '+day_later

    return new_time

~~~
