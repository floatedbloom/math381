import random

sample_count = 1000
samples = [0] * sample_count
ppl = [3,3,3]
n = 3
for i in range(sample_count):
    while 0 not in ppl:
        p1 = random.randrange(n)
        p2 = random.randrange(n)
        while p1==p2:
            p2 = random.randrange(n)
        ppl[p1]-=1
        ppl[p2]+=1
        samples[i]+=1
    ppl = [3,3,3]

mean = sum(samples)/len(samples)
print(mean)