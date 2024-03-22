from sqlalchemy import Column, Integer, Float, String
from Database import Base

class Atom(Base):
    __tablename__ = 'atom'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Float)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    charge = Column(Float)
    charge_type = Column(String)
