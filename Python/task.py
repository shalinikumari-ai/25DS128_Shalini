import random
def task():
    num = random.randint(-10, 40)
    if num > 0:
        print(f"{num} is a positive integer")
    else:
        print(f"{num} is a negative integer")

    num1 = random.randint(1, 30)
    if num1 % 5 == 0:
         print(f"{num1} is divisible by 5")
    else:
        print(f"{num1} is not divisible by 5")

    num2 = random.randint(1, 50)
    if num2 % 2 == 0:
        print(f"{num2} is even")
    else:
        print(f"{num2} is odd")

task()