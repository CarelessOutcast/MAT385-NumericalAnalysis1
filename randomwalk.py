# Random Walk Simulations
# The procedure below estimates the mean escape time for a random walk to escape the interval [-b,a]

import random

def randwalk(b,a):
    avar = 0
    count = 0
    pos = 0
    while pos < a and b < pos:
        if random.randint(0,1)==1:
            pos = pos + 1 
        else:
            pos = pos - 1
        count = count + 1
    if pos==a:
        avar = 1
    return [count,avar]
    


# Estimate the escape time for one simulation
#  #(a)
b = -2
a = 5

#  #(b)
# a = 3
# b = -5
#
 #(c)
# b = -8
# a = 3

print(f'Exit time (one trial): {randwalk(b,a)[0]}')
values = []
# Estimate the escape time for N simulations

N = 10000
probs = 0
steps = 0
for n in range(N):
    values.append(0)
    values[n], avar = randwalk(b,a)
    probs += avar;
    steps += values[n]

variance = 0
for n in range(N):
    variance += (values[n]-(steps/N))**2

print(f"\n  For {N} trials")
print('Sample Mean:&\t',steps/N)
print('Variance:&\t',variance/(N-1))
print('Standard Err:&\t',(variance/(N-1))**(1/2))
print(f'Actual prob:&\t {b/(b-a)}')
print(f'Cal. prob:&\t {probs/N}')
print(f'prob\\,\\,Error:&\t {b/(b-a)-probs/N}')





