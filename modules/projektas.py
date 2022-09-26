
from sqlalchemy import (create_engine,
                        Column,
                        Integer,
                        String,
                        Float,
                        DateTime)
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///projektai.db')
Base = declarative_base()

class Projektas(Base):
    __tablename__ = "Projektas"
    id = Column(type_=Integer, primary_key=True)
    name = Column(name="Pavadinimas", type_=String)
    price = Column(name="Kaina", type_=Float)
    created_date = Column(name="Sukūrimo data", type_=DateTime, default=datetime.now)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"

Base.metadata.create_all(engine)