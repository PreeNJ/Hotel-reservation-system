from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    reservations = relationship("Reservation", back_populates="customer")


class Table(Base):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True)
    table_number = Column(Integer, unique=True)
    capacity = Column(Integer)
    is_available = Column(Boolean, default=True)

    reservations = relationship("Reservation", back_populates="table")


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    table_id = Column(Integer, ForeignKey('tables.id'))
    reservation_time = Column(DateTime)
    party_size = Column(Integer)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="reservations")
    table = relationship("Table", back_populates="reservations")
