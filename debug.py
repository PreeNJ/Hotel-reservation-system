from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Customer, Table, Reservation

engine = create_engine('sqlite:///restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()

def print_all_data():
    pass

if __name__ == "__main__":
    print_all_data()
