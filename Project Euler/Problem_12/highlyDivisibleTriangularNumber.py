stop= False
num = 1
while not stop:
    gaussSum = int(num*(num+1)/2)
    dividers = []
    for i in range(1,int(gaussSum**0.5)+1):
        if gaussSum%i == 0:
            dividers.append(i)
            dividers.append(int(gaussSum/i))
    if len(dividers) > 500:
        stop = True
    num += 1

print(gaussSum)