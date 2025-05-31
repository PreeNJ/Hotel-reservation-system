from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Customer, Table, Reservation
from datetime import datetime, timedelta

engine = create_engine('sqlite:///restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()

# Drop and recreate tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create customers
c1 = Customer(name="Alice", phone="0134567890", email="alice@gmail.com")
c2 = Customer(name="Bob", phone="0987654321", email="bob@gmail.com")

t1 = Table(table_number=1, capacity=4)
t2 = Table(table_number=2, capacity=2)

# Create reservations
r1 = Reservation(
    customer=c1,
    table=t1,
    reservation_time=datetime.now() + timedelta(days=1),
    party_size=2,
    notes="Birthday"
)
r2 = Reservation(
    customer=c2,
    table=t2,
    reservation_time=datetime.now() + timedelta(days=2),
    party_size=2,
    notes="Anniversary"
)

# Add to session
session.add_all([c1, c2, t1, t2, r1, r2])
session.commit()

print("Database seeded successfully.")

