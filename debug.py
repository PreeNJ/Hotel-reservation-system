# ─── Chunk 3 (Add printing for reservations and finalize script) ────────────────

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Customer, Table, Reservation

engine = create_engine('sqlite:///restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()

def print_all_data():
    print("=== CUSTOMERS ===")
    for c in session.query(Customer).all():
        print(f"{c.id}: {c.name}  ({c.phone}, {c.email})")

    print("\n=== TABLES ===")
    for t in session.query(Table).all():
        status = "Available" if t.is_available else "Occupied"
        print(f"{t.id}: Table #{t.table_number}  (Capacity: {t.capacity})  [{status}]")

    print("\n=== RESERVATIONS ===")
    for r in session.query(Reservation).all():
        cust_name = r.customer.name if r.customer else "(no customer)"
        tbl_num = r.table.table_number if r.table else "(no table)"
        print(f"{r.id}: {cust_name} → Table #{tbl_num} @ {r.reservation_time}  (Party: {r.party_size})")

if __name__ == "__main__":
    print_all_data()
