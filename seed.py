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
c1 = Customer(name="Alice", phone="1234567890", email="alice@example.com")
c2 = Customer(name="Bob", phone="0987654321", email="bob@example.com")
