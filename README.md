📦 Inventory Management System


A modular Command-Line Inventory Management System built with Python.
This project demonstrates clean code organization, separation of concerns, and structured application design.

🚀 Overview

This system allows users to:

Register new inventory items

Prevent duplicate item names

Search items by name or category

Add stock to existing items

Remove stock safely

Register item loans

Generate inventory reports

Validate user input using a dedicated validation module

🧱 Project Structure
inventory-system/
│
├── main.py            # Application entry point
├── core.py            # Inventory business logic
├── reports.py         # Reporting and summaries
├── validators.py      # Input validation
└── README.md
📌 Module Responsibilities
Module	Description
main.py	Handles menu and user interaction
core.py	Core inventory operations
reports.py	Inventory reporting and analytics
validators.py	Input validation and data integrity

This modular structure improves:

Maintainability

Scalability

Code readability

Separation of concerns

🧠 Data Model

Each item is stored as a dictionary:

{
    "id": int,
    "name": str,
    "quantity": int,
    "price": float,
    "category": str,
    "condition": str,
    "notes": str
}

All items are managed in a centralized inventory list.

▶️ How to Run

Make sure you have Python 3 installed

Open the project folder in terminal

Run:

python main.py
📊 Reporting Features

The reporting module can include:

Total inventory value calculation

Items grouped by category

Low stock alerts

Inventory summaries

🛡 Validation Layer

The validators.py module ensures:

Numeric input validation

Duplicate name prevention

Condition validation (new/used)

Clean and consistent data handling

📚 Concepts Demonstrated

Modular Programming

Separation of Concerns

CLI Application Design

Data Validation

Error Handling

List Comprehensions

Dictionary-Based Data Modeling

🔮 Future Improvements

Persistent storage (JSON or SQLite)

Unit testing with pytest

CSV export for reports

Graphical interface (Tkinter)

REST API version (Flask / FastAPI)

Authentication system

📄 License

MIT License — free to use and modify.
