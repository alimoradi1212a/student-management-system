# Student Management System

A simple Python-based student management system for storing, searching, and managing student records using file handling.

---

## Features

- Add new students (name, age, major)
- View all students
- Search students by name
- Delete student records
- Save and load data from a file (`students.txt`)
- Handles invalid file data safely

---

## Project Structure



student management system/
│
├── main.py
├── README.md
└── students.txt

---

## Strengths

- Safe file handling using try-except to avoid crashes
- Input validation for empty names
- UTF-8 encoding supports Persian/Unicode text
- Clean and simple function-based structure
- Automatic data loading on startup

---

## Possible Improvements

- Add age validation (ensure numeric input)
- Improve output formatting for better alignment
- Add confirmation before deleting records
- Handle duplicate names during deletion more carefully
- Show number of search results
- Add edit/update student feature

---

Author

Ali Moradi