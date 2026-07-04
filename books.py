from prettytable import PrettyTable
from db_connection import get_db_connection

def add_book():
    print("\n╔══════════════════════════════╗")
    print("║        ADD A BOOK            ║")
    print("╚══════════════════════════════╝\n")
    book_name = input("Enter the book's name: ")
    author_name = input("Enter the author's name: ")
    book_code = (input("Enter the book's code: "))
    book_category = input("Enter book's category: ")
    availability = "avaliable"
    book_details = (book_name,author_name,book_code,book_category,availability)
    sql="insert into books values(%s,%s,%s,%s,%s);"
    c=db.cursor()
    c.execute(sql,book_details)
    db.commit()
    print("\nBook added successfully..........\n")
    main()
    
# Function to search for a book by title:
def search_book():
    print("\n╔══════════════════════════════╗")
    print("║            BOOK              ║")
    print("╚══════════════════════════════╝\n")

    book_name = input("Enter the book's name to search: ")
    sql6="select *from books where bname='{}'".format(book_name,)
    c=db.cursor()
    c.execute(sql6)
    res=c.fetchall()
    l=[]
    t=PrettyTable(["Book's name","Author","Book's code","Category","Availibility"])
    for i in res:
        print("\nBook found..........\n")
        l.append([i[0],i[1],i[2],i[3],i[4]])
        break
    else:
        print("Book not found..........")
    t.add_rows(l)
    if l!=[]:
        print(t)
    main() 
    
# Function to display all available books in the library:
def display_books():
    print("\n╔══════════════════════════════╗")
    print("║         BOOKS' LIST          ║")
    print("╚══════════════════════════════╝\n")
    x=1
    sql4="select*from books;"
    c=db.cursor()
    c.execute(sql4)
    res=c.fetchall()
    l1=[]
    t=PrettyTable(["Book's name","Author","Book's code","Category","Availibility"])
    for i in res:
        l1.append([i[0],i[1],i[2],i[3],i[4]])
    t.add_rows(l1)
    if l1!=[]:
        print(t)
    else:
        print("Library is empty...............")
    main()

# Function to delete a book from the library:
def delete_book():
    print("\n╔══════════════════════════════╗")
    print("║        DELETING BOOK         ║")
    print("╚══════════════════════════════╝\n")
    book_code = (input("Enter the book code:"))
    sql5="delete from books where bcode='{}'".format(book_code,)
    sql6="select *from books where bcode='{}'".format(book_code,)
    c=db.cursor()
    c.execute(sql6)
    res=c.fetchall()
    for i in res:
        c.execute(sql5)
        print("\nBook deleted successfully..........\n")
        break
    else:
        print("Book not found............")
    main() 
