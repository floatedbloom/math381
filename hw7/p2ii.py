import numpy as np
import matplotlib.pyplot as plt
import random
plt.ion()

def linregression(x, y, plot=True):
    a, b = np.polyfit(x,y,1)

    if plot:
        plt.figure()
        line = [a*x0 + b for x0 in x]
        plt.scatter(x,y)
        plt.plot(x,line)
        plt.show()

    return a, b

def powregression(x, y, plot=True):
    log_x = np.log(x)
    log_y = np.log(y)
    a, b = np.polyfit(log_x,log_y,1)

    if plot:
        plt.figure()
        line = [a*x0 + b for x0 in log_x]
        plt.scatter(log_x,log_y)
        plt.plot(log_x,line)
        plt.show()

    return a, np.exp(b)

def expregression(x, y, plot=True):
    log_y = np.log(y)
    a, b = np.polyfit(x,log_y,1)

    if plot:
        plt.figure()
        line = [a*x0 + b for x0 in x]
        plt.scatter(x,log_y)
        plt.plot(x,line)
        plt.show()

    return np.exp(a), np.exp(b)

sample_count = 200000
n = 3
ks = [i for i in range(1,10)]
ps = []
for k in ks:
    losses = 0
    for i in range(sample_count):
        ppl = [k] + [1] * (n-1)
        while 0 not in ppl:
            p1,p2 = random.sample(range(n), 2) 
            ppl[p1]-=1
            ppl[p2]+=1
        if ppl[0] == 0:
            losses+=1
    ps.append(losses/sample_count)
lin_a, lin_b = linregression(ks,ps)
pow_a, pow_b = powregression(ks,ps)
exp_a, exp_b = expregression(ks,ps)
plt.show(block=True)
print(lin_a, lin_b)
print(pow_a, pow_b)
print(exp_a, exp_b)