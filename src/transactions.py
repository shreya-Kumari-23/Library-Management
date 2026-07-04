import mysql.connector
from db_connection import get_db_connection

db = get_db_connection()
cursor = db.cursor()

def issue_book():
    print("\n╔══════════════════════════════╗")
    print("║        ISSUE A BOOK          ║")
    print("╚══════════════════════════════╝\n")

    student_name = input("Enter the student's name: ")
    bcode = input("Enter the book's code: ")
    reg_no = input("Enter the registration number: ")
    issue_date = input("Enter the issue date (YYYY-MM-DD): ")

    try:
        # Insert into issue table
        cursor.execute(
            "INSERT INTO issue (student_name, bcode, reg_no, issue_date) VALUES (%s, %s, %s, %s)",
            (student_name, bcode, reg_no, issue_date)
        )

        # Update availability in books table
        cursor.execute(
            "UPDATE books SET availability = 'unavailable' WHERE bcode = %s",
            (bcode,)
        )

        db.commit()
        print(f"\nBook {bcode} issued successfully to {student_name}\n")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()


def return_book():
    print("\n╔══════════════════════════════╗")
    print("║        RETURN A BOOK         ║")
    print("╚══════════════════════════════╝\n")

    student_name = input("Enter the student's name: ")
    bcode = input("Enter the book's code: ")
    reg_no = input("Enter the registration number: ")
    return_date = input("Enter the return date (YYYY-MM-DD): ")

    try:
        # Insert into rturn table
        cursor.execute(
            "INSERT INTO rturn (student_name, bcode, reg_no, return_date) VALUES (%s, %s, %s, %s)",
            (student_name, bcode, reg_no, return_date)
        )

        # Update availability in books table
        cursor.execute(
            "UPDATE books SET availability = 'available' WHERE bcode = %s",
            (bcode,)
        )

        db.commit()
        print(f"\nBook {bcode} returned successfully by {student_name}\n")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
