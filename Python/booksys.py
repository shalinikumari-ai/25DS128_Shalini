def books():
    d = {1 : "Harry Potter", 2 : "Panchtantra", 3 : "Flamingo", 4 : "Vistas", 5 : "Honeycomb"}
    num = int(input("Enter the book number (1 - 5) : "))
    book_name = d.get(num)
    if book_name :
        print("book name : " ,book_name)
    else :
        print("Invalid book number!")
books()
    