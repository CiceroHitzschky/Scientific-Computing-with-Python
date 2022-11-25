def add_time(hora_inicio, duracao, dia=None):
    dias_depois = ''
    semana = {
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }
    pm_am = {
        0:'AM',
        1:'PM'
    }

    hora_inicio = hora_inicio.split()

    hora = hora_inicio[0].split(':')
    duracao = duracao.split(':')
    
    minutos_hora = int(hora[0])*60 + int(hora[1])
    minutos_duracao = int(duracao[0])*60 + int(duracao[1])
    total_minutos = minutos_hora + minutos_duracao

    hora_resultado = int(total_minutos/60)%12

    
    # Condicional do periodo
    if hora_inicio[1] == 'AM' and total_minutos < 720:
        periodo = 'AM'
    elif hora_inicio[1] == 'AM' and total_minutos >= 720:
        periodo = 'PM'
    
    elif hora_inicio[1] == 'PM' and total_minutos < 720:
        periodo = 'PM'
    else:
        periodo = 'AM'

    # Contagem dos dias


    # if hora_inicio[1] == 'PM':
    #     completar_dia = 12*60-minutos_hora
    #     print(completar_dia)
    #     intervalo_completo = minutos_duracao - completar_dia
    #     parte_inteira_dias = int(intervalo_completo/(24*60)) 
    #     n_dias = int(parte_inteira_dias +1 )
    #     print(n_dias)
    # else:
    #     n_dias = 0
    # if n_dias == 0:
    #     days_later = ' '
    # elif n_dias == 1:
    #     days_later = '(next day)'
    # else:
    #     days_later = f'({n_dias} days later)'

    if hora_resultado == 0:
        hora_resultado ='12'
    minutos_resultado = total_minutos%60
    
    if len(str(minutos_resultado)) < 2:
        minutos_resultado = '0'+str(minutos_resultado)
    resultado = str(hora_resultado) +':'+ str(minutos_resultado)+' '+periodo+' '
    return print(resultado)

add_time('3:00 PM','3:10')
add_time('11:30 AM','2:32')
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")