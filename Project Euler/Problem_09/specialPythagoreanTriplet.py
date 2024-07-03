for a in range(1,333):
    for b in range(a+1,500):
        for c in range(b+1,998):
            if a**2+b**2==c**2:
                print(a,b,c)
                if a+b+c == 1000:
                    answer = a*b*c

print("answer is",answer)