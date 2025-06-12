# donorform_model.py

from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .donor_model import Donor  # Import the Donor class from donor_model

Base = declarative_base()

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

    # Define relationship with donor table
    donor = relationship("Donor", back_populates="donor_forms")

    def __repr__(self):
        return f"<DonorForm(id={self.id}, donor_id={self.donor_id}, donor_name={self.donor_name}, food_id={self.food_id}, food_name={self.food_name}, food_type={self.food_type}, quantity={self.quantity}, preparation_time={self.preparation_time}, available={self.available})>"

