num = int(input("Bir sayı girin: "))

for i in range(2,num):
    if num%i == 0:
        print("Sayı asal değil")
        break
    if i == num-1:
        print("Sayı asal")