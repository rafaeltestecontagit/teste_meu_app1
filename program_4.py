
import matplotlib.pyplot as plt
import numpy as np

nl = 200
nc = 200
matriz = list(range(0,nl,1))

for i in range(0,nl,1):       
    matriz[i] = list(range(0,nc,1))  

for i in range(0,nl,1):
    for j in range(0,nc,1):
        matriz[i][j] = 10*np.exp(-((i-nl/2)/(0.2*nl))**2)+10*np.exp(-((j-nc/2)/(0.7*nc))**2)


a = 33










