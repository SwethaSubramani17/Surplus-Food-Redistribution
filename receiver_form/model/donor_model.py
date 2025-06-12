import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Donor(Base):
    __tablename__ = 'donor'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    address = Column(Text)
    status = Column(Integer, default=1)
    created_time = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    updated_time = Column(TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    donor_forms = relationship("DonorForm", back_populates="donor")

    def __repr__(self):
        return f"<Donor(id={self.id}, name={self.name})>"
