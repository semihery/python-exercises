textFile = open("Kelime Cümle Arama\Sample Text.txt", "r")
mainText = textFile.read()
textFile.close()
# mainText = "abc def klmn kodar dedil."
# print(mainText)
searchedWord = str(input("Aranan kelime: "))


i = 0
result = ""
while i < len(mainText):
    if mainText[i] == searchedWord[0]:
        if searchedWord == mainText[i:i+len(searchedWord)]:
            while mainText[i] != " ":
                result += mainText[i]
                i += 1
            else: result += " "
    i += 1
print()
print("Kelimeler: "+result)
print()

i = 0
result = ""
while i < len(mainText):
    if mainText[i] == searchedWord[0]:
        if searchedWord == mainText[i:i+len(searchedWord)]:
            while mainText[i] != ".":
                result += mainText[i]
                i += 1
            else: result += "."    
    i += 1
print("Cümleler: "+result)
print()