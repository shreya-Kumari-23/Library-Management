from books import add_book, display_books, delete_book, search_book
from transactions import issue_book, return_book
from reports import report_issued_books, report_returned_books
from db_connection import get_db_connection

db = get_db_connection()

# Main menu:
def main():
    while True:
        print("_")
        print("+                                                                           +")
        print("+ *******               Library Management System                 ********* +")
        print("+_+")
        print("+                                                                           +")
        print("+                       1. Add a book                                       +")
        print("+                       2. Display available books                          +")
        print("+                       3. Issue a book                                     +")
        print("+                       4. Return a book                                    +")
        print("+                       5. Search for a book                                +")
        print("+                       6. Delete a book                                    +")
        print("+                       7. Report menu                                      +")
        print("+                       8. Exit                                             +")
        print("+                                                                           +")
        print("+_+")

        choice = input("           Enter your choice (1-8): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            search_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("\n╔══════════════════════════╗")
            print("║        REPORT MENU       ║")
            print("╠══════════════════════════╣")
            print("║ 1. Issued Books          ║")
            print("║ 2. Returned Books        ║")
            print("║ 3. Go back to Main Menu  ║")
            print("╚══════════════════════════╝\n")
            choice = input("  Enter your choice (1-3): ")

            if choice == "1":
                report_issued_books()
            elif choice == "2":
                report_returned_books()
            elif choice == "3":
                main()
            else:
                print("\nPlease try again..........\n")
                main()
        elif choice == "8":
            print("\nThankyou and have a great day ahead..........\n")
            db.close()
            quit()
        else:
            print("\nInvalid choice. Please try again.\n")
            main()
            db.close()

# Run the main function
main()
