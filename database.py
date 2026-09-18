from sqlalchemy import String,Integer,Column,func
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine
database_url="postgresql://postgres:YOUR_REAL_PASSWORD@localhost:5432/postgres"
engine=create_engine(database_url)
session_house=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()
