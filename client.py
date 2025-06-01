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
