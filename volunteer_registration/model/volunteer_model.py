import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
Base = declarative_base()

engine = create_engine('mysql://root:SwethaSakthi@localhost/volunteers_db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class Volunteer(Base):
    __tablename__ = 'volunteers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    phone_number = Column(String(10))
    email = Column(String(255), unique=True)
    password = Column(String(10))
    address = Column(Text)
    status = Column(Integer, default=1)
    created_time = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    updated_time = Column(TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
