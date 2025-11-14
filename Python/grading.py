a = [62,75,83,23,45,55,35,88,92,100]
for i in a:
    if i >= 33 and i <= 35:
        print(i,"Grade = C")
    elif i >= 35 and i <= 65:
        print(i,"Grade = B")
    elif i >= 65 and i <= 89:
        print(i,"Grade = A")
    elif i >= 89 and i <= 100:
        print(i,"Grade = A++")
    else :
        print(i,"Fail")

