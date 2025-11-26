import random

sample_count = 100000
losses = 0
n, k = 2, 29
for i in range(sample_count):
    ppl = [k] + [1] * (n-1)
    while 0 not in ppl:
        p1,p2 = random.sample(range(n), 2) 
        ppl[p1]-=1
        ppl[p2]+=1
    if ppl[0] == 0:
        losses+=1
print(f"k={k}", losses/sample_count)