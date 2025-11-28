import numpy as np

steps = 10000000
n, k = 4, 5
x = np.array([k]*n, dtype=float)
burn_in = 1000000
samples = np.array([0]*(steps-burn_in), dtype=float)
for t in range(steps):
    p1,p2 = np.random.choice(n, 2, replace=False)
    alpha = ((x[p1]-1)*(x[p2]+1))/(x[p1]*x[p2])
    if np.random.random() < alpha:
        x[p1]-=1
        x[p2]+=1
    if t > burn_in:
        samples[t-burn_in] = np.prod(x)

print(np.mean(samples))