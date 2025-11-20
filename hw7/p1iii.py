import random

sample_count = 1000
samples = [0] * sample_count
n, k = 3, 100
for i in range(sample_count):
    ppl = [k] * n
    while 0 not in ppl:
        p1,p2 = random.sample(range(n), 2) 
        ppl[p1]-=1
        ppl[p2]+=1
        samples[i]+=1

print(sum(samples)/len(samples))