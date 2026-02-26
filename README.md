📦 Inventory Management System (CLI)

A modular Command Line Inventory Management System built in Python.
This project allows users to register items, manage stock, search inventory, generate reports, and validate input data — all through a structured and maintainable architecture.

🧱 Project Architecture

The project is divided into logical modules to improve scalability and maintainability:

inventory-system/
│
├── main.py            # Application entry point
├── core.py            # Core inventory logic
├── reports.py         # Reporting and inventory summaries
├── validators.py      # Input validation logic
└── README.md
📌 Module Responsibilities
File	Responsibility
main.py	Handles user interaction and menu flow
core.py	Contains inventory operations (register, search, update, loan, etc.)
reports.py	Generates inventory summaries and reports
validators.py	Validates user inputs (numbers, conditions, duplicates, etc.)
🚀 Features

✅ Modular architecture

📦 Item registration with duplicate name prevention

📋 Full inventory listing

🔎 Search by name or category

➕ Add stock

➖ Remove stock

📤 Loan registration

📊 Reporting module

🛡 Input validation module

❌ Exception handling

🛠 Technologies Used

Python 3

Lists & Dictionaries

List Comprehensions

Exception Handling

Modular Programming

▶️ How to Run

1️⃣ Make sure Python 3 is installed

2️⃣ Run the main file:

python main.py
🧠 Data Structure

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

All items are stored in a shared inventory list managed by the core module.

📊 Reports Module

The reports.py module may include:

📈 Total inventory value

📦 Items grouped by category

📉 Low stock alerts

📄 Loan summaries

🛡 Validators Module

The validators.py module centralizes:

Numeric input validation

Condition validation (new/used)

Duplicate name checking

Data sanitization

This improves code reusability and keeps the core logic clean.

🔮 Future Improvements

💾 JSON file persistence

🗄 SQLite database integration

🖥 GUI version (Tkinter)

🌐 Web API (Flask / FastAPI)

🧪 Unit testing with pytest

📊 Advanced reporting (CSV export)

📄 License

MIT License

Se quiseres, posso agora:

🔥 Deixar isto com nível “GitHub Portfolio Ready”

📊 Criar uma secção de badges (Python version, license, etc.)

🧪 Escrever testes unitários para a estrutura modular

💼 Adaptar o README para candidatura a estágio/emprego

Qual é o objetivo do projeto? Académico ou portefólio profissional?

deixa com visual github portifolio ready 

Aqui está a versão GitHub Portfolio Ready — mais profissional, com badges, descrição estratégica e foco em arquitetura 👇

📦 Inventory Management System








A modular Command-Line Inventory Management System built with Python, designed using clean code principles and separation of concerns.

This project demonstrates:

Structured architecture

Input validation layer

Reporting module

Business logic isolation

Error handling best practices

🚀 Overview

The system allows users to:

Register new inventory items

Prevent duplicate item names

Search items by name or category

Add or remove stock

Register item loans

Generate inventory reports

Validate inputs using a dedicated validation layer

🧱 Architecture

The project follows a modular design pattern, separating responsibilities across multiple files.

inventory-system/
│
├── main.py
├── core.py
├── reports.py
├── validators.py
└── README.md
📌 Module Breakdown
Module	Responsibility
main.py	Application entry point & user interaction
core.py	Inventory business logic
reports.py	Reporting & analytics
validators.py	Input validation & data integrity

This separation improves:

Maintainability

Scalability

Readability

Testability

🧠 Core Data Structure

Each inventory item is stored as a dictionary:

{
    "id": int,
    "name": str,
    "quantity": int,
    "price": float,
    "category": str,
    "condition": str,
    "notes": str
}

All items are stored in a centralized inventory list managed by the core module.

📊 Reporting Capabilities

The reporting module supports:

📈 Total inventory value calculation

📦 Items grouped by category

⚠ Low stock detection

📄 Inventory summary views

🛡 Validation Layer

The validators.py module ensures:

Numeric validation for quantity and price

Duplicate name prevention

Condition validation (new/used)

Input sanitization

This keeps business logic clean and improves reliability.

▶️ Running the Project
1️⃣ Clone the repository
git clone https://github.com/yourusername/inventory-system.git
2️⃣ Navigate to the project folder
cd inventory-system
3️⃣ Run the application
python main.py
🧪 Possible Enhancements

Future improvements could include:

💾 Persistent storage (JSON / SQLite)

🧪 Unit testing (pytest)

📤 CSV export for reports

🖥 Graphical interface (Tkinter)

🌐 REST API version (Flask / FastAPI)

👥 Authentication system

📚 Concepts Demonstrated

Modular Programming

Separation of Concerns

Data Validation

Error Handling

List Comprehensions

Dictionary-based Data Modeling

CLI Application Design

📄 License

MIT License — feel free to use, modify, and distribute.
