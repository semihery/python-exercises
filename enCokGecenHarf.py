inputText = input("Bir metin giriniz: ")

letterQuantities = {}

for i in inputText:
    if i not in letterQuantities:
        letterQuantities[i] = 0
        for j in inputText:
            if i == j:
                letterQuantities[i] += 1
                
print(letterQuantities)

for i in range(len(letterQuantities)):
    if list(letterQuantities.values())[i] == max(letterQuantities.values()):
        print("En çok bulunan harf: "+str(list(letterQuantities.items())[i]))