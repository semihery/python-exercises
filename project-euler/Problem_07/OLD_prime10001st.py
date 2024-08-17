primeNo = 2
number = 3
while primeNo < 10001:
    is_divisible = False
    number +=2
    for i in range(3,number):
        if number%i == 0:
            is_divisible = True
            break
    if not is_divisible: primeNo += 1

print(number)
