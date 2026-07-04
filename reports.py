from db_connection import get_db_connection
from prettytable import PrettyTable

db = get_db_connection()

def report_issued_books():
    print("\n╔══════════════════════════════╗")
    print("║      ISSUED BOOKS' LIST      ║")
    print("╚══════════════════════════════╝\n")
    sql = "SELECT * FROM issue;"
    c = db.cursor()
    c.execute(sql)
    res = c.fetchall()
    t = PrettyTable(["Student's Name","Book Code","Registration Number","Issue Date"])
    for i in res:
        t.add_row([i[0], i[1], i[2], i[3]])
    print(t)

def report_returned_books():
    print("\n╔══════════════════════════════╗")
    print("║     RETURNED BOOKS' LIST     ║")
    print("╚══════════════════════════════╝\n")
    sql = "SELECT * FROM rturn;"
    c = db.cursor()
    c.execute(sql)
    res = c.fetchall()
    t = PrettyTable(["Student's Name","Book Code","Registration Number","Return Date"])
    for i in res:
        t.add_row([i[0], i[1], i[2], i[3]])
    print(t)
