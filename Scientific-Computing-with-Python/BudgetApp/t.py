def criador_colunas(numero):
    lista = [' ' for i in range(10)]
    
    for i in range(numero):
        lista[i] = lista[i].replace(' ', 'o')
    
    return lista
        
    
def create_spend_chart():
    title = 'Percentage spent by category\n'
    num1 = 8
    num2 = 3
    num3 = 1
    num4 = 0
    
    eixo_y = [
        f"{100:>3}|",
        f"{90:>3}|",
        f"{80:>3}|",
        f"{70:>3}|",
        f"{60:>3}|",
        f"{50:>3}|",
        f"{40:>3}|",
        f"{30:>3}|",
        f"{20:>3}|",
        f"{10:>3}|",
        f"{0:>3}|"
    ] 
    coluna1 = ''.join(criador_colunas(num1))+'\n'
    coluna2 = ''.join(criador_colunas(num2))+'\n'
    coluna3 = ''.join(criador_colunas(num3))+'\n'
    coluna4 = ''.join(criador_colunas(num4))+'\n'
    
#     return coluna1+coluna2+coluna3+coluna4
    lista_colunas = ''
    for i in zip(eixo_y,coluna1,coluna2,coluna3,coluna4):
        lista_colunas += ' '.join(i)
    return title+lista_colunas

print(create_spend_chart())