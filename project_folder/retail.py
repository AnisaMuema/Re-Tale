from sqlalchemy import Table, Column, Integer,DATETIME, PrimaryKeyConstraint, VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Create tables
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR)
    last_name = Column(VARCHAR)
    email = Column(VARCHAR)
    contact = Column(Integer)

    

class Product(Base):
    __table__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)
    category = Column(VARCHAR)
    sub_category = Column(VARCHAR)
    price = Column(Integer)
    Expiry_date = Column(DATETIME)

engine = create_engine('sqlite:///retail.db')

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)


