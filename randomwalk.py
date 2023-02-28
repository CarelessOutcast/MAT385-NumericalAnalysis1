# Random Walk Simulations
# The procedure below estimates the mean escape time for a random walk to escape the interval [-b,a]

import random


def randwalk():
    count = 0
    pos = 0
    while pos < a and b < pos:
        if random.randint(0,1)==1:
            pos = pos + 1 
        else:
            pos = pos - 1
        count = count + 1
    return (count)
    


# Estimate the escape time for one simulation
 
a = 6
b = -3

print('Exit time (one trial):', randwalk())

# Estimate the escape time for N simulations

N = 10000
steps = 0
for n in range(N):
    steps = steps + randwalk()
print('\nExpected Exit time after',N,'trials:',steps/N)
    
                               

