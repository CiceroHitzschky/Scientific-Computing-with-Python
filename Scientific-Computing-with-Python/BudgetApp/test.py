import numpy as np
food = [i for i in 'food ']
carro = [i for i in 'carro']
matrix = np.array([food,carro])
for i in matrix.T:
    print(' '.join(i))