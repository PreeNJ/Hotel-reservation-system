# Restaurant Table Reservation System

**Owner:** Priscillah Njai

---

## Description
A simple, menu-driven Python CLI application that allows restaurant staff to manage customers, tables, and reservations. The backend uses SQLite with SQLAlchemy ORM, and Pipenv is used for dependency management.

---

## Setup Instructions

1. **Clone or download** this repository:
   ```bash
   git clone (https://github.com/PreeNJ/Hotel-reservation-system.git) <br/>
   cd HOTEL-RESERVATION-SYSTEM

2. *Install Pipenv:*
   pip install pipenv

3. Install project dependencies:
   pipenv install

4. Activate the virtual environment:
   pipenv shell

5. Seed the database (this drops any existing tables, recreates them, and inserts sample data):
   python lib/db/seed.py
   You should see:
   Database seeded successfully.

6. Run the CLI application:
   python lib/cli.py
   This launches an interactive menu where you can manage Customers, Tables, and Reservations.

Features
Customer Management

Create new customers (name, phone, email)

View all existing customers (ID, name, contact)

Delete a customer by ID

Table Management

Add new tables (table number, capacity)

View all tables (ID, table number, capacity, availability)

Delete a table by ID

Reservation Management

Create new reservations:

Select an existing Customer ID

Select an existing Table ID

Enter reservation date/time (YYYY-MM-DD HH:MM)

Enter party size (positive integer)

Optional notes field

Prevents double-booking (no two reservations for the same table at the same time)

View all reservations (reservation ID, customer name, table number, date/time, party size)

Delete a reservation by ID

Data Seeding & Debugging

seed.py script: Drops and recreates tables, then inserts sample data (2 customers, 2 tables, 2 reservations).

debug.py script: Prints all rows from customers, tables, and reservations for quick inspection.

Technologies Used
Python 3.10

SQLAlchemy (ORM for SQLite)

SQLite (lightweight, file-based database)

Pipenv (virtual environment & dependency management)

