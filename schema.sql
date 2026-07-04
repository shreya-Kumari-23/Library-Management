CREATE DATABASE YOUR_LIBRARY;

USE YOUR_LIBRARY;

CREATE TABLE books (
    bname VARCHAR(100),
    author VARCHAR(100),
    bcode VARCHAR(20) PRIMARY KEY,
    category VARCHAR(50),
    availability VARCHAR(20)
);

CREATE TABLE issue (
    student_name VARCHAR(100),
    bcode VARCHAR(20),
    reg_no VARCHAR(20),
    issue_date DATE
);

CREATE TABLE rturn (
    student_name VARCHAR(100),
    bcode VARCHAR(20),
    reg_no VARCHAR(20),
    return_date DATE
);
