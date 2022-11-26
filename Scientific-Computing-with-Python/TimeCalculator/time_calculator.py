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
