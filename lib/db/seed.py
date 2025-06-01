import sys
import os

# Add both the project root and lib directory to Python path
current_dir = os.path.dirname(__file__)
db_dir = current_dir
lib_dir = os.path.dirname(db_dir)
project_root = os.path.dirname(lib_dir)

sys.path.insert(0, project_root)
sys.path.insert(0, lib_dir)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Customer, Table, Reservation
from datetime import datetime, timedelta

engine = create_engine('sqlite:///restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

c1 = Customer(
    name="Alice Johnson",
    phone="555-123-4567",
    email="alice.johnson@example.com"
)
c2 = Customer(
    name="Bob Smith",
    phone="555-987-6543",
    email="bob.smith@example.com"
)

t1 = Table(
    table_number=1,
    capacity=4,
    is_available=True
)
t2 = Table(
    table_number=2,
    capacity=2,
    is_available=True
)

r1 = Reservation(
    customer=c1,
    table=t1,
    reservation_time=datetime.now() + timedelta(days=1, hours=19),  # tomorrow at ~7pm
    party_size=2,
    notes="Birthday dinner"
)
r2 = Reservation(
    customer=c2,
    table=t2,
    reservation_time=datetime.now() + timedelta(days=2, hours=18),  # day after tomorrow at ~6pm
    party_size=2,
    notes="Anniversary"
)

session.add_all([c1, c2, t1, t2, r1, r2])
session.commit()

print("Database seeded successfully.")