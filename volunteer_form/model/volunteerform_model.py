import datetime
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from volunteer_form.model.session import Session

Base = declarative_base()

class VolunteerForm(Base):
    __tablename__ = 'volunteerforms'

    id = Column(Integer, primary_key=True)
    donor_name = Column(String(50), nullable=False)
    food_name = Column(String(50), nullable=False)
    food_type = Column(String(20), nullable=False)
    quantity = Column(Integer, nullable=False)
    preparation_time = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    decision = Column(String(10)) # To store 'accept' or 'reject'

    # Ensure the import statement is aligned with other class attributes
    from volunteer_form.model.session import Session

    def __repr__(self):
        return f"<VolunteerForm(donor_name='{self.donor_name}', food_name='{self.food_name}', food_type='{self.food_type}', quantity={self.quantity}, preparation_time='{self.preparation_time}')>"
