library = []

def add_book():
    print("\nAdd New Book")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    
    book = {
        "title": title,
        "author": author,
        "year": year
    }
    
    library.append(book)
    print("Book added successfully!")

def show_books():
    print("\nAll Books")
    if len(library) == 0:
        print("No books in the library yet.")
    else:
        print(f"There are {len(library)} book(s) in the library:\n")
        for i in range(len(library)):
            b = library[i]
            print(f"{i+1}. Title  : {b['title']}")
            print(f"    Author : {b['author']}")
            print(f"    Year   : {b['year']}")
            print()

def search_book():
    print("\n Search Book ")
    search = input("Enter title to search: ")
    
    found = False
    for book in library:
        if book["title"].lower() == search.lower():
            print("\nBook found!")
            print(f"Title  : {book['title']}")
            print(f"Author : {book['author']}")
            print(f"Year   : {book['year']}")
            found = True
            break
    
    if found == False:
        print("Book not found.")

def delete_book():
    print("\n Delete Book ")
    title = input("Enter title to delete: ")
    
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book deleted successfully!")
            return
    
    print("Book not found. Cannot delete.")

while True:
    print("\n")
    print("=" * 35)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("=" * 35)
    print("1. Add Book")
    print("2. Show All Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")
    print("=" * 35)
    
    choice = input("Choose option (1-5): ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("\nThank you! Goodbye!")
        break
    else:
        print("Invalid choice. Please type 1, 2, 3, 4 or 5.")
    
    input("\nPress Enter to continue...")
