from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read database credentials from .env
DATABASE_URL = os.getenv("DATABASE_URL")  # Example: "mysql+pymysql://your_username:your_password@localhost:3306/your_database"

# Create the engine and session
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

# Function to initialize the database
def init_db(Base):
    Base.metadata.create_all(engine)

# Function to get a new session
def get_db_session():
    return SessionLocal()
