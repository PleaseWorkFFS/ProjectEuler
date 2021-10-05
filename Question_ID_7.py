'''The 10001st prime number'''

NonPrimes = set(j for i in range(2,9) for j in range(i*2,1000000,i))
primes = [x for x in range(2,1000000) if x not in NonPrimes]

print(len(primes))
print(primes[10000])
