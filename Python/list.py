#List : are used to store the multiple values in the single variable
a = ["Rachit", "Vaishnavi", "Shalini"]
print(a)
print(type(a))
print(len(a))

#Tuples : are used to store the multiple values in the single variable but tuples are immutable
a = (1, "Rachit",True)
print(a)
print(type(a))
print(a[1])
print(a[:3])

#Sets : are used to store multiple values in the single variable but sets are uordered and unindexed
#can't store a single value multiple times
a = {1,2,3,4,"Rachit","Vaishnavi"}
print(a)
print(type(a))

#Dictionary : are used to store multiple values in the single variable in key : value pair
a = {"Name" : "Rachit", "Age" : 21, "College" : "ABC"}
print(a)
print(a["College"])

#LOOPS
#while loop
i = 7
while i < 8:
    print(i)
    i+=1

count = 5
while count > 0:
    if count % 2 == 0:
        print(f"{count} is even")
    else:
        print(f"{count} is odd")
    count-=1

#For loop
nums = [1,2,3,4,5,6,7,8,9]
for num in nums:
    if num % 2 == 0:
        print(f"{num} is even")
    else :
        print(f"{num} is odd")

for i in range(1,11,2):
    print (i) 