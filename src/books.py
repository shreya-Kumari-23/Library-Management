from db_connection import get_db_connection
from prettytable import PrettyTable

db = get_db_connection()

def add_book():
    print("\n╔══════════════════════════════╗")
    print("║        ADD A BOOK            ║")
    print("╚══════════════════════════════╝\n")
    book_name = input("Enter the book's name: ")
    author_name = input("Enter the author's name: ")
    book_code = input("Enter the book's code: ")
    book_category = input("Enter book's category: ")
    availability = "available"
    book_details = (book_name, author_name, book_code, book_category, availability)
    sql = "INSERT INTO books VALUES(%s,%s,%s,%s,%s);"
    c = db.cursor()
    c.execute(sql, book_details)
    db.commit()
    print("\nBook added successfully..........\n")

def display_books():
    print("\n╔══════════════════════════════╗")
    print("║         BOOKS' LIST          ║")
    print("╚══════════════════════════════╝\n")
    sql = "SELECT * FROM books;"
    c = db.cursor()
    c.execute(sql)
    res = c.fetchall()
    t = PrettyTable(["Book Name","Author","Book Code","Category","Availability"])
    if res:
        for i in res:
            t.add_row([i[0], i[1], i[2], i[3], i[4]])
        print(t)
    else:
        print("Library is empty...............")

def search_book():
    print("\n╔══════════════════════════════╗")
    print("║            SEARCH BOOK       ║")
    print("╚══════════════════════════════╝\n")
    book_name = input("Enter the book's name to search: ")
    sql = "SELECT * FROM books WHERE bname=%s"
    c = db.cursor()
    c.execute(sql, (book_name,))
    res = c.fetchall()
    t = PrettyTable(["Book Name","Author","Book Code","Category","Availability"])
    if res:
        for i in res:
            t.add_row([i[0], i[1], i[2], i[3], i[4]])
        print("\nBook found..........\n")
        print(t)
    else:
        print("Book not found..........")

def delete_book():
    print("\n╔══════════════════════════════╗")
    print("║        DELETE BOOK           ║")
    print("╚══════════════════════════════╝\n")
    book_code = input("Enter the book code: ")
    sql_check = "SELECT * FROM books WHERE bcode=%s"
    sql_delete = "DELETE FROM books WHERE bcode=%s"
    c = db.cursor()
    c.execute(sql_check, (book_code,))
    res = c.fetchall()
    if res:
        c.execute(sql_delete, (book_code,))
        db.commit()
        print("\nBook deleted successfully..........\n")
    else:
        print("Book not found............")
