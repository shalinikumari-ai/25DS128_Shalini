def fun():
    print("hello word")

fun()

def add(a, b):
     
    return a+b

x = add(5, 10)
print(x)
y = add(6, 19)
print(y)

def square(num) :
    return num*num

print(square(9))

def arithmetic(a , b):
    c1 = a + b
    c2 = a - b
    c3 = a * b
    c4 = a / b
    c5 = a //b
    c6 = a % b
    return c1, c2, c3, c4, c5, c6

a = 12
b =3
result = arithmetic(a, b)
print (result)
