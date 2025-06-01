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
# ─── Chunk 8 ────────────────────────────────────────────────────────────────────
def reservation_menu():
    while True:
        print("\n--- Reservation Menu ---")
        print("1. Create Reservation")
        print("2. View All Reservations")
        print("3. Delete Reservation")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            cid = validate_input("Customer ID: ", int, lambda x: x > 0, "Enter a positive integer.")
            tid = validate_input("Table ID: ", int, lambda x: x > 0, "Enter a positive integer.")

            # Retrieve the objects so we can show errors if invalid
            customer = session.query(Customer).get(cid)
            table = session.query(Table).get(tid)

            if not customer:
                print("Customer ID not found.")
                continue
            if not table:
                print("Table ID not found.")
                continue

            # Prompt for a reservation datetime string
            time_str = input("Reservation Time (YYYY-MM-DD HH:MM, 24h): ").strip()
            try:
                time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Invalid datetime format. Use YYYY-MM-DD HH:MM.")
                continue

            party_size = validate_input("Party Size: ", int, lambda x: x > 0, "Enter a positive integer.")
            notes = input("Notes (optional): ").strip()

            # Prevent double booking: check if a reservation already exists for that table at that time
            conflict = session.query(Reservation).filter_by(table_id=table.id, reservation_time=time_obj).first()
            if conflict:
                print("That table is already booked at that time.")
                continue

            # Insert reservation
            new_res = Reservation(
                customer_id=customer.id,
                table_id=table.id,
                reservation_time=time_obj,
                party_size=party_size,
                notes=notes
            )
            session.add(new_res)
            session.commit()
            print("Reservation created.")
        elif choice == "2":
            all_res = session.query(Reservation).all()
            if not all_res:
                print("No reservations found.")
            for r in all_res:
                cust_name = r.customer.name
                tbl_num = r.table.table_number
                when = r.reservation_time.strftime("%Y-%m-%d %H:%M")
                print(f"{r.id}: {cust_name} → Table #{tbl_num} @ {when} (Party: {r.party_size})")
        elif choice == "3":
            rid = validate_input("Reservation ID to delete: ", int, lambda x: x > 0, "Enter a positive integer.")
            res = session.query(Reservation).get(rid)
            if res:
                session.delete(res)
                session.commit()
                print("Reservation deleted.")
            else:
                print("Reservation not found.")
        elif choice == "4":
            return
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
