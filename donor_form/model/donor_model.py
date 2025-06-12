import datetime
from sqlalchemy import create_engine, Column, Integer, Text, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('mysql://root:SwethaSakthi@localhost/donors_db') # Updated databse namename to donors_db
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class Donor(Base):
    __tablename__ = 'donor'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(Integer)
    email = Column(String, unique=True)
    password = Column(String)
    address = Column(Text)
    status = Column(Integer, default=1)
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    updated_time = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

def __repr__(self):
   return f"<Donor(id={self.id}, donor_name={self.donor_name}, phone_number={self.phone_number}, email={self.email}, password={self.password}, confirm_password={self.confirm_password})>"