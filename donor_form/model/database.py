from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to your database
engine = create_engine('sqlite:///donors.db')  # Replace 'sqlite:///donors.db' with your database connection string

# Create a sessionmaker object
Session = sessionmaker(bind=engine)
