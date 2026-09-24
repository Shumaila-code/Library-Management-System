books = []

while True:
    print("\n==== Library Management System ====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")
    print("4. Search Book")
    print("5. Delete Book")
    print("6. Update Book")
    print("7. Issue Book")
    print("8. Return Book")

    choice = input("Enter your Choice: ")

    if choice == "1":
        book_name = input("Enter Book Name: ").strip()
        author = input("Enter Author Name: ")

        book = {
            "Book": book_name,
            "Author": author,
            "Status": "Available"
        }

        books.append(book)
        print("Book Added Successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No Books Available!")
        else:
            print("\nBooks List:")
            for book in books:
                print("Book: ",book["Book"]),
                print("Author: ",book["Author"]),
                print("Status: ",book["Status"]),
                print(".........................")

    elif choice == "3":
        print("Program Closed.")
        break

    elif choice == "4":
        search_book=input("Enter Book Name: ").strip().lower()
        for book in books:
          if book ["Book"].lower() == search_book:
            print("Book Found!")
            print("Book: ",book["Book"]),
            print("Author: ",book["Author"]),
            print("Status: ",book["Status"]),
            print(".........................")
                                     
            break
        else:
            print("Book Not Found")
    elif choice == "5":
        delete_book=input("Enter Book Name: ").lower()
        for book in books:
            if book ["Book"].lower() == delete_book:
                books.remove(book)
                print("Book Deleted Successfully!")
                break
        else:
             print("Such Book Not Found...")

    elif choice == "6":
        old_book=input("Enter Old Book Name: ").lower()
        for book in books:
            if book["Book"].lower() == old_book:
                new_book=input("Enter New Book Name: ")
                book["Book"]=new_book
                print("Book Updated Successfully!")
                break
        else:
            print("No Updation Occur..")

    elif choice == "7":
        issue_book=input("Enter Book Name: ").lower()
        for book in books:
            if book["Book"].lower() == issue_book:
               if book["Status"] == "Available":
                book["Status"] = "Issued"
                print("Book Issued Successfully!")
               else:
                     print("Book Is Already Issued!")
               break

        else:
            print("Book Not Found!") 

    elif choice == "8":
        return_book=input("Enter Book Name: ").lower()
        for book in books:
            if book["Book"].lower() == return_book:
             if book["Status"] == "Issued":
                 book["Status"] = "Available"
                 print("Book Returned Successfully!")
             else:
                 print("Book Is Already Available!")
             break
        else:
            print("Book Not Found!")
    else:
        print("Invalid Choice.")