import numpy as np

P = np.array([[1,0,0,0,0],[0.5,0,0.5,0,0],[0,0.5,0,0.5,0],[0,0,0.5,0,0.5],[0,0,0,0,1]])

k = 10000

M = np.linalg.matrix_power(P,k)
print(M)

u,v = np.linalg.eig(np.transpose(P))
v *= 1/sum(v)

print(u)
print(v)