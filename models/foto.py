from sqlalchemy import  Column, Integer, String 
from sqlalchemy.orm import  declarative_base


Base = declarative_base()



class Foto(Base):   
    __tablename__ = 'foto'
    foto_id = Column(String, primary_key=True)
    foto_url = Column(String, nullable=False)
    foto_descrizione = Column(String)
    foto_link = Column(String)
    foto_autore = Column(String)

