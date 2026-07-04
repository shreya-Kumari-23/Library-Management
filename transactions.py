from db_connection import get_db_connection

db = get_db_connection()

# Function to issue a book from the library:
def issue_book():
    print("\n╔══════════════════════════════╗")
    print("║        ISSUE A BOOK          ║")
    print("╚══════════════════════════════╝\n")
    student_name = input("Enter the student's name: ")
    book_code = (input("Enter the book's code: "))
    reg_no = input("Enter the regisration number: ")
    idate = input("Enter the issue date (YYYY-MM-DD): ")
    sql6="select *from books where bcode='{}'".format(book_code,)
    c=db.cursor()
    c.execute(sql6)
    res=c.fetchall()
    for i in res:
        if book_code==i[2]:  
            print("Book found.................")
            if i[4]=="not available":
                print("\nBook already issued...........")
                break
            sql1="insert into issue values(%s,%s,%s,%s);"
            book_details1=(student_name,book_code,reg_no,idate)
            c=db.cursor()
            c.execute(sql1,book_details1)
            c.execute("UPDATE books SET availability='not available' WHERE bcode = %s", (book_code,))
            db.commit()
            print("\nBook issued successfully by ..........\n",student_name)
            break
    else:
        print("Book not found..................")           
    main() 

# Function to return an issued book to the library:
def return_book():
    print("\n╔══════════════════════════════╗")
    print("║        RETURN A BOOK         ║")
    print("╚══════════════════════════════╝\n")
    student_name = input("Enter the student's name: ")
    book_code= (input("Enter the book's code: "))
    reg_no = input("Enter the regisration number: ")
    rdate = input("Enter the issue date (YYYY-MM-DD): ")
    sql6="select *from books where bcode='{}'".format(book_code,)
    c=db.cursor()
    c.execute(sql6)
    res=c.fetchall()
    for i in res:
        if book_code == i[2]:
            print("book found.................")
            if i[4]=="available":
                print("\nBook already returned...........")
                break
            sql2="insert into rturn values(%s,%s,%s,%s);"
            book_details2=(student_name,book_code,reg_no,rdate)
            c=db.cursor()
            c.execute(sql2,book_details2)
            c.execute("UPDATE books SET availability='available' WHERE bcode = %s", (book_code,))
            db.commit()
            print("\nBook returned successfully by",student_name,"\n")   
            break         
    else:
        print("Book not found..........")
    main() 
