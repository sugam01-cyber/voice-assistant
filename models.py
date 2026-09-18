from database import Base, engine
from sqlalchemy import String,Integer,Column,func,DateTime

class App(Base):
    __tablename__="PasteApp"
    pastes= Column(String)
    id=Column(Integer,primary_key=True)
    date_created=Column(DateTime,server_default=func.now())


Base.metadata.create_all(bind=engine)
