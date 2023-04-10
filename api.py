from fastapi import FastAPI, Depends
from pathlib import Path # To see if the database is already in the repo
import csv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from typing import List, Optional
# from pydantic import BaseModel

# Create a Path object with the path to the database
path = Path('./titanic.db')

# Define the database and create the database engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./titanic.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for database models
Base = declarative_base()

# Define a model for the "titanic" table
class Titanic(Base):
    __tablename__ = "titanic"

    passengerid = Column(Integer, primary_key=True, index=True)
    survived = Column(Integer)
    pclass = Column(Integer)
    name = Column(String)
    sex = Column(String)
    age = Column(Integer, default=None)
    sibsp = Column(Integer)
    parch = Column(Integer)
    ticket = Column(String)
    fare = Column(Float)
    cabin = Column(String, default=None)
    embarked = Column(String)

# Create table if it does not exist already
if not path.is_file():
    print('_'*50)
    print('Creating database...')

    # Create the "titanic" table
    Base.metadata.create_all(bind=engine)

    # Open the CSV file and save each row into a list
    with open("titanic.csv") as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]

    # Create a database session
    db = SessionLocal()

    # Loop through the rows list and insert them into the database
    for row in rows:
        passenger = Titanic(
            passengerid=row["PassengerId"],
            survived=row["Survived"],
            pclass=row["Pclass"],
            name=row["Name"],
            sex=row["Sex"],
            age=row["Age"],
            sibsp=row["SibSp"],
            parch=row["Parch"],
            ticket=row["Ticket"],
            fare=row["Fare"],
            cabin=row["Cabin"],
            embarked=row["Embarked"]
        )
        db.add(passenger)

    # Commit the changes and close the database session
    db.commit()
    db.close()
# End if

# FastAPI instance
app = FastAPI()

# Define a function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define an endpoint to get all rows in the "titanic" table
@app.get("/titanic")
def get_all_titanic_rows(db: Session = Depends(get_db)):
    rows = db.query(Titanic).all()
    return rows

# Define an endpoint to get a specific row in the "titanic" table
@app.get("/titanic/{id}")
def get_titanic_row(id: int, db: Session = Depends(get_db)):
    row = db.query(Titanic).filter(Titanic.passengerid == id).first()
    return row

# Define an endpoint to get passenger based in their features
@app.get("/titanic/")
async def filter_passengers(
    passengerid: int | None = None,
    survived: int | None = None,
    pclass: int | None = None,
    name: str | None = None,
    sex: str | None = None,
    age: float | None = None,
    sibsp: int | None = None,
    parch: int | None = None,
    ticket: str | None = None,
    fare: float | None = None,
    cabin: str | None = None,
    embarked: str | None = None,
    db: Session = Depends(get_db)
):
    # Get all rows first (not efficient if dataset is large)
    passengers = db.query(Titanic)

    # Filter rows based on the query parameter
    # When text is large, I used contains function
    if passengerid is not None:
        passengers = passengers.filter(Titanic.passengerid == passengerid)
    if survived is not None:
        passengers = passengers.filter(Titanic.survived == survived)
    if pclass is not None:
        passengers = passengers.filter(Titanic.pclass == pclass)
    if name is not None:
        passengers = passengers.filter(Titanic.name.contains(name))
    if sex is not None:
        passengers = passengers.filter(Titanic.sex == sex)
    if age is not None:
        passengers = passengers.filter(Titanic.age == age)
    if sibsp is not None:
        passengers = passengers.filter(Titanic.sibsp == sibsp)
    if parch is not None:
        passengers = passengers.filter(Titanic.parch == parch)
    if ticket is not None:
        passengers = passengers.filter(Titanic.ticket.contains(ticket))
    if fare is not None:
        passengers = passengers.filter(Titanic.fare == fare)
    if cabin is not None:
        passengers = passengers.filter(Titanic.cabin.contains(cabin))
    if embarked is not None:
        passengers = passengers.filter(Titanic.embarked == embarked)

    passengers = passengers.all()
    return passengers