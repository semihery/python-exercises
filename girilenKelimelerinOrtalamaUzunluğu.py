myStr = ""
numInput = 0

while True:
    spaceLetterFound = False
    inpt = input("Bir kelime girin. Bitirmek için 0 yaz.: ")
    if inpt == "0":
        break
    else:
        for letter in inpt:
            if letter == " ":
                spaceLetterFound = True
                print("Lütfen boşluk bırakmayınız")
                break
        if not spaceLetterFound:
            myStr += inpt
            numInput += 1

print()
print(myStr)
print("Ortalama girdi uzunluğu: "+str(len(myStr)/numInput))