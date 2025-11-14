def book_system():
    book_d = {1 : "book1", 2 : "book2", 3 : "book3" , 4 : "book4", 5 : "book5"}
    num = int(input("Enter book number (1 - 5) : "))
    if num in book_d:
        print ("Book name : ",book_d[num])
    else :
        print("invalid book number!")
book_system()