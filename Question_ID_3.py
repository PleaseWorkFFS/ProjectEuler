'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''
'''NonPrimes = set(j for i in range(2,9) for j in range(i*2,13195,i))
primes = [x for x in range(2,13195) if x not in NonPrimes]
'''
NonPrimes = []
Primes = []
for i in range(1,10):
    for j in range(2,51):
        if j%i==0:
            NonPrimes.append(i)

for p in range(2,50):
    for e in NonPrimes:
        if p!=e:
            Primes.append(p)
BiggestPrime = 0
for f in Primes:
    if 13195%f==0:
        if f>BiggestPrime:
            BiggestPrime=f

print(BiggestPrime)

print(NonPrimes)
print(Primes)
