from sqlalchemy.orm import sessionmaker
from modules.projektas import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()