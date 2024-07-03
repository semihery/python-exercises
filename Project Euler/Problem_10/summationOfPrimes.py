primes = [2]

for num in range(3,2000000,2):
    for i in primes:
        if num%i == 0:
            break
        if i*i > num:
            primes.append(num)
            print(num)
            break

suma = 0
for prime in primes:
    suma += prime

print(suma)
print(sum(primes))