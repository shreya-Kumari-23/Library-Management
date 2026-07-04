-- Create the database
CREATE DATABASE YOUR_LIBRARY;

-- Switch to the database
USE YOUR_LIBRARY;

-- Table for storing books
CREATE TABLE books (
    bname VARCHAR(100),
    author VARCHAR(100),
    bcode VARCHAR(20) PRIMARY KEY,
    category VARCHAR(50),
    availability VARCHAR(20)
);

-- Table for issued books
CREATE TABLE issue (
    student_name VARCHAR(100),
    bcode VARCHAR(20),
    reg_no VARCHAR(20),
    issue_date DATE
);

-- Table for returned books
CREATE TABLE rturn (
    student_name VARCHAR(100),
    bcode VARCHAR(20),
    reg_no VARCHAR(20),
    return_date DATE
);