# 📚 Library Management System (Python + MySQL)

A simple command-line Library Management System built in Python with MySQL integration.  
It supports book management, issuing/returning transactions, and reporting — perfect for learning database + Python integration.

## 🚀 Features
- Add new books
- Display all books
- Issue books
- Return books
- Search books by title
- Delete books
- Reports for issued and returned books

## ⚙️ Requirements
- Python 3.x
- MySQL Server
- Dependencies: `mysql-connector-python`, `prettytable`

---
## 📂 Project Structure
Library-Management/

├── src/                  # All Python source files
│       ├── main.py
│       ├── db_connection.py
│       ├── books.py
│       ├── transactions.py
│       └── reports.py
├── requirements.txt       # Dependencies
├── schema.sql             # Database schema
└── README.md              # Documentation

---

## ▶️ How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system

2. Install dependencies:
   pip install -r requirements.txt
   
3. Set up the database:
   mysql -u root -p < schema.sql

4. Run the program:
  python main.py
