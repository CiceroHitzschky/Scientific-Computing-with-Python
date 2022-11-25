def add_time(hora_inicio, duracao, dia=None):
    semana = {
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }
    # Separando e tranformando em minutos
    hora_inicio = hora_inicio.split()
    hora = hora_inicio[0].split(':')
    duracao = duracao.split(':')
    minutos_hora = int(hora[0])*60 + int(hora[1])
    minutos_duracao = int(duracao[0])*60 + int(duracao[1])
    total_minutos = minutos_hora + minutos_duracao
    hora_resultado = int(total_minutos/60)%12

    # Tranformando em dias
    n_dias_inteiros = int(minutos_duracao/1440)
    parte_decimal = float(minutos_duracao/1440) - n_dias_inteiros
    minutos_restantes_duracao = parte_decimal*1440
    COMPLETA_DIA = minutos_hora + minutos_restantes_duracao
    
    if hora_inicio[1] == 'PM' and COMPLETA_DIA > 720:
        n_dias = n_dias_inteiros + 1

    else:
        n_dias = n_dias_inteiros
    # print(n_dias_inteiros,minutos_restantes_duracao)

    
    # Condicional do periodo
    if (hora_inicio[1] == 'PM' and total_minutos > 720) and minutos_duracao != 1440:
        periodo = 'AM'  
    elif hora_inicio[1] == 'PM' and total_minutos < 720:
        periodo = 'PM'
    elif (hora_inicio[1] == 'AM' and total_minutos > 720) and minutos_duracao != 1440:
        periodo = 'PM'
    elif hora_inicio[1] == 'AM' and total_minutos < 720:
        periodo = 'AM'
    else:
        periodo = hora_inicio[1]



    # Contagem dos dias
    if n_dias == 1:
        day_later = '(next day)'
    elif n_dias == 0 and COMPLETA_DIA < 720:
        day_later = ''
    elif n_dias == 0 and COMPLETA_DIA >= 720:
        day_later = ''    
    else:
        day_later = f'({n_dias} days later)'

    # Adaptação do dia
    

    # dia = dia.capitalize()
    # for k,v in semana.items():
    #     if v == dia:
    #         # print(k)
    #         index_dia_retorno = (k + n_dias)%7
    #         # print(index_dia_retorno)
    # novo_dia = f', {semana[index_dia_retorno]}'

    # Formatação de trocar 12 por 00
    if hora_resultado == 0:
        hora_resultado ='12'
    minutos_resultado = total_minutos%60
    
    if len(str(minutos_resultado)) < 2:
        minutos_resultado = '0'+str(minutos_resultado)

    if dia == None and n_dias ==0:
        resultado = str(hora_resultado) +':'+ str(minutos_resultado)+' '+periodo
    elif dia == None and n_dias !=0:
        resultado = str(hora_resultado) +':'+ str(minutos_resultado)+' '+periodo+' '+day_later        
    
    elif dia != None and n_dias ==0:
        dia = dia.capitalize()
        for k,v in semana.items():
            if v == dia:
                # print(k)
                index_dia_retorno = (k + n_dias)%7
                # print(index_dia_retorno)
        novo_dia = f', {semana[index_dia_retorno]}'        
        resultado = str(hora_resultado) +':'+ str(minutos_resultado)+' '+periodo+novo_dia
    else:    
        dia = dia.capitalize()
        for k,v in semana.items():
            if v == dia:
                # print(k)
                index_dia_retorno = (k + n_dias)%7
                # print(index_dia_retorno)
        novo_dia = f', {semana[index_dia_retorno]}'
        
        resultado = str(hora_resultado) +':'+ str(minutos_resultado)+' '+periodo+novo_dia+' '+day_later
    
    
    return resultado

# add_time('3:00 PM','3:10')
# add_time("11:30 AM", "2:32", "Monday")
# add_time("11:43 AM", "00:20")
# add_time("10:10 PM", "3:30")
# add_time("11:43 PM", "24:20", "tueSday")
# add_time("11:43 PM", "24:00", "tueSday")
# add_time("6:30 PM", "205:12")
# # testes
# add_time("3:30 PM", "2:12")
# add_time("11:55 AM", "3:12")
# add_time("8:16 PM", "466:02")
# add_time("3:30 PM", "2:12", "Monday")
# add_time("2:59 AM", "24:00", "saturDay")

# print(add_time("2:59 AM", "24:00"))