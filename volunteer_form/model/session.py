from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database URL
DB_URL = "mysql://root:SwethaSakthi@localhost/receiverforms_db"

# Create the engine
engine = create_engine(DB_URL)

# Create a Session class bound to the engine
Session = sessionmaker(bind=engine)