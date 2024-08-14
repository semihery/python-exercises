primeNums = {2:0,3:0,5:0,7:0,11:0,13:0,17:0,19:0}
numsUndivided = list(range(2,21))


for i in primeNums.keys():
    divisible = True
    while divisible:
        divisible = False        
        for j in range(len(numsUndivided)):
            if numsUndivided[j]%i == 0:
                divisible = True
                numsUndivided[j] //= i
        if divisible:
            primeNums[i] += 1

answer = 1

for i in list(primeNums.keys()):
    answer *= i**primeNums[i]

print(answer)