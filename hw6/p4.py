import numpy as np

P = np.array([[0.1, 0.9, 0, 0],[0, 0, 0.03, 0.97],[0.1, 0.9, 0, 0],[0, 0, 0.03, 0.97]])

u,v = np.linalg.eig(np.transpose(P))
v *= 1/sum(v)

print(u)
print(v)