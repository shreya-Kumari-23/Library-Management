from db_connection import get_db_connection

db = get_db_connection()

def issue_book():
    print("\n╔══════════════════════════════╗")
    print("║        ISSUE A BOOK          ║")
    print("╚══════════════════════════════╝\n")
    student_name = input("Enter the student's name: ")
    book_code = input("Enter the book's code: ")
    reg_no = input("Enter the registration number: ")
    idate = input("Enter the issue date (YYYY-MM-DD): ")

    sql = "SELECT * FROM books WHERE bcode=%s"
    c = db.cursor()
    c.execute(sql, (book_code,))
    res = c.fetchall()

    if res:
        for i in res:
            if i[4] == "not available":
                print("\nBook already issued...........")
                return
            sql_issue = "INSERT INTO issue VALUES(%s,%s,%s,%s);"
            book_details = (student_name, book_code, reg_no, idate)
            c.execute(sql_issue, book_details)
            c.execute("UPDATE books SET availability='not available' WHERE bcode=%s", (book_code,))
            db.commit()
            print("\nBook issued successfully by ..........\n", student_name)
    else:
        print("Book not found..................")

def return_book():
    print("\n╔══════════════════════════════╗")
    print("║        RETURN A BOOK         ║")
    print("╚══════════════════════════════╝\n")
    student_name = input("Enter the student's name: ")
    book_code = input("Enter the book's code: ")
    reg_no = input("Enter the registration number: ")
    rdate = input("Enter the return date (YYYY-MM-DD): ")

    sql = "SELECT * FROM books WHERE bcode=%s"
    c = db.cursor()
    c.execute(sql, (book_code,))
    res = c.fetchall()

    if res:
        for i in res:
            if i[4] == "available":
                print("\nBook already returned...........")
                return
            sql_return = "INSERT INTO rturn VALUES(%s,%s,%s,%s);"
            book_details = (student_name, book_code, reg_no, rdate)
            c.execute(sql_return, book_details)
            c.execute("UPDATE books SET availability='available' WHERE bcode=%s", (book_code,))
            db.commit()
            print("\nBook returned successfully by", student_name, "\n")
    else:
        print("Book not found..........")
