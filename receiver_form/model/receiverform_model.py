
import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .donor_model import Donor
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Donor(Base):
    __tablename__ = 'donor'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(Integer)
    email = Column(String, unique=True)
    password = Column(String)
    address = Column(Text)
    status = Column(Integer, default=1)
    created_time = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    updated_time = Column(TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    forms = relationship("DonorForm", back_populates="donor")

class DonorForm(Base):
    __tablename__ = 'donorform'

    id = Column(Integer, primary_key=True)
    donor_id = Column(Integer, ForeignKey('donor.id'))
    donor_name = Column(String(50))
    food_id = Column(Integer)
    food_name = Column(String(50))
    food_type = Column(String(20))
    quantity = Column(Integer)
    preparation_time = Column(TIMESTAMP)
    available = Column(Boolean)

    donor = relationship("Donor", back_populates="forms")

    def __repr__(self):
        return f"<DonorForm(donor_name='{self.donor_name}', food_name='{self.food_name}', food_type='{self.food_type}', quantity={self.quantity}, preparation_time='{self.preparation_time}')>"
