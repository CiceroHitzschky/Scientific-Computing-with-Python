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

