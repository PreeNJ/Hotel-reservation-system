# ─── Chunk 3 ────────────────────────────────────────────────────────────────────
def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. Create Customer")
        print("2. View All Customers")
        print("3. Delete Customer")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            session.add(Customer(name=name, phone=phone, email=email))
            session.commit()
            print("Customer created.")
        elif choice == "2":
            all_customers = session.query(Customer).all()
            if not all_customers:
                print("No customers found.")
            for c in all_customers:
                print(f"{c.id}: {c.name} (Email: {c.email}, Phone: {c.phone})")
        # (options 3 and 4 still to be implemented)
        else:
            print("Invalid choice. Try again.")

# ─── Chunk 4 ────────────────────────────────────────────────────────────────────
        elif choice == "3":
            cid = validate_input("Customer ID to delete: ", int, lambda x: x > 0, "Enter a positive integer.")
            cust = session.query(Customer).get(cid)
            if cust:
                session.delete(cust)
                session.commit()
                print("Customer deleted.")
            else:
                print("Customer not found.")
        elif choice == "4":
            return
    
     else:
            print("Invalid choice. Try again.")
# ─── Chunk 6 ────────────────────────────────────────────────────────────────────
        if choice == "1":
            number = validate_input("Table Number: ", int, lambda x: x > 0, "Enter a positive integer.")
            capacity = validate_input("Capacity: ", int, lambda x: x > 0, "Enter a positive integer.")
            session.add(Table(table_number=number, capacity=capacity))
            session.commit()
            print("Table added.")
        elif choice == "2":
            all_tables = session.query(Table).all()
            if not all_tables:
                print("No tables found.")
            for t in all_tables:
                status = "Available" if t.is_available else "Occupied"
                print(f"{t.id}: Table #{t.table_number} (Capacity: {t.capacity}) [{status}]")
        # (options 3 and 4 still to be implemented)
# ─── Chunk 7 ────────────────────────────────────────────────────────────────────
        elif choice == "3":
            tid = validate_input("Table ID to delete: ", int, lambda x: x > 0, "Enter a positive integer.")
            tbl = session.query(Table).get(tid)
            if tbl:
                session.delete(tbl)
                session.commit()
                print("Table deleted.")
            else:
                print("Table not found.")
        elif choice == "4":
            return
