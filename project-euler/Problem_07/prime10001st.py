primes = [2]
primeCount = 1
isDivisible = False
i = 3
while primeCount < 10001:
    for prime in primes:
        if i%prime == 0:
            isDivisible = True
            break
    if not isDivisible:
        primes.append(i)
        primeCount += 1
    else:
        isDivisible = False
    i += 2
print(primes[-1])