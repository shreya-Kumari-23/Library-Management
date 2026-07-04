import mysql.connector as m

def get_db_connection():
    return m.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="YOUR_LIBRARY"
    )
