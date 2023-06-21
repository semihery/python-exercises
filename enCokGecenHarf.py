inputText = input("Bir metin giriniz: ")

letterQuantities = {}

for i in inputText:
    if i not in letterQuantities and i != " ":
        letterQuantities[i] = 0
        for j in inputText:
            if i == j:
                letterQuantities[i] += 1
                
print(letterQuantities)

for i in range(len(letterQuantities)):
    if list(letterQuantities.values())[i] == max(letterQuantities.values()):
        print(list(letterQuantities.keys())[i] + " harfi " + str(list(letterQuantities.values())[i]) + " defa kullanıldı.")