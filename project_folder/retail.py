from sqlalchemy import Table, Column, Integer,DATETIME, PrimaryKeyConstraint, VARCHAR, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates="orders")

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship("Order", back_populates="items")
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", back_populates="order_items")
    quantity = Column(Integer)

Customer.orders = relationship("Order", order_by=Order.id, back_populates="customer")
Order.items = relationship("OrderItem", order_by=OrderItem.id, back_populates="order")
Product.order_items = relationship("OrderItem", order_by=OrderItem.id, back_populates="product")

engine = create_engine('sqlite:///retail.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()



