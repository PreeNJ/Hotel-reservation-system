from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Customer, Table, Reservation
from lib.helpers import validate_input
from datetime import datetime

engine = create_engine("sqlite:///restaurant.db")
Session = sessionmaker(bind=engine)
session = Session()

def menu():
    while True:
        print("\n--- Restaurant Reservation CLI ---")
        print("1. Manage Customers")
        print("2. Manage Tables")
        print("3. Manage Reservations")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            customer_menu()
        elif choice == "2":
            table_menu()
        elif choice == "3":
            reservation_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def customer_menu():
    pass

def table_menu():
    pass

def reservation_menu():
    pass