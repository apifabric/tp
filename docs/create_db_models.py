# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

# Define a base class using SQLAlchemy Declarative system
Base = declarative_base()

# Table Descriptions:
# 1. Customer: Stores information about customers, including their credit limits and balances
# 2. Order: Holds data about customer orders, including dates and notes
# 3. Item: Represents individual items within an order, including quantity and unit price
# 4. Product: Contains product details such as the unit price
# 5. Address: Manages customer addresses, storing multiple addresses for a customer
# 6. OrderNote: Captures additional notes related to an order
# 7. Payment: Logs payment information against customer orders
# 8. Contact: Manages contact information for customers
# 9. Supplier: Contains supplier details who provide products
# 10. Inventory: Keeps track of product inventory status
# 11. Shipment: Logs shipment information for orders
# 12. Return: Manages records of returned items

class Customer(Base):
    """description: Stores information about customers, including their credit limits and balances."""
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    credit_limit = Column(Float, nullable=False)
    balance = Column(Float, default=0.0)

class Order(Base):
    """description: Holds data about customer orders, including dates and notes."""
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    date_shipped = Column(DateTime, nullable=True)
    amount_total = Column(Float, default=0.0)
    note = Column(String, nullable=True)
    customer = relationship("Customer", back_populates="orders")

Customer.orders = relationship("Order", order_by=Order.id, back_populates="customer")

class Item(Base):
    """description: Represents individual items within an order, including quantity and unit price."""
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    amount = Column(Float, default=0.0)
    order = relationship("Order", back_populates="items")

Order.items = relationship("Item", order_by=Item.id, back_populates="order")

class Product(Base):
    """description: Contains product details such as the unit price."""
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    unit_price = Column(Float, nullable=False)

class Address(Base):
    """description: Manages customer addresses, storing multiple addresses for a customer."""
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    address = Column(String, nullable=False)

class OrderNote(Base):
    """description: Captures additional notes related to an order."""
    __tablename__ = 'order_notes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    note = Column(String, nullable=False)

class Payment(Base):
    """description: Logs payment information against customer orders."""
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    amount = Column(Float, nullable=False)
    date_received = Column(DateTime, default=datetime.datetime.utcnow)

class Contact(Base):
    """description: Manages contact information for customers."""
    __tablename__ = 'contacts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    contact_number = Column(String, nullable=False)

class Supplier(Base):
    """description: Contains supplier details who provide products."""
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)

class Inventory(Base):
    """description: Keeps track of product inventory status."""
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity_available = Column(Integer, nullable=False)

class Shipment(Base):
    """description: Logs shipment information for orders."""
    __tablename__ = 'shipments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    shipment_date = Column(DateTime, nullable=True)
    carrier = Column(String, nullable=False)

class Return(Base):
    """description: Manages records of returned items."""
    __tablename__ = 'returns'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    reason = Column(String, nullable=False)

# Create a new SQLite database (or connect to an existing one)
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Seed data for the database
customer1 = Customer(name="John Doe", credit_limit=5000.0, balance=1500.0)
customer2 = Customer(name="Jane Smith", credit_limit=10000.0, balance=800.0)

order1 = Order(customer_id=1, date_shipped=None, note="Urgent delivery")
order2 = Order(customer_id=2, date_shipped=datetime.datetime.utcnow(), note="Handle with care")

product1 = Product(name="Widget A", unit_price=25.0)
product2 = Product(name="Gadget B", unit_price=15.0)

item1 = Item(order_id=1, product_id=1, quantity=10, unit_price=25.0, amount=250.0)
item2 = Item(order_id=2, product_id=2, quantity=20, unit_price=15.0, amount=300.0)

inventory1 = Inventory(product_id=1, quantity_available=100)
inventory2 = Inventory(product_id=2, quantity_available=150)

address1 = Address(customer_id=1, address="123 Elm St")
address2 = Address(customer_id=2, address="456 Oak St")

order_note1 = OrderNote(order_id=1, note="Remember to call before delivery")
order_note2 = OrderNote(order_id=2, note="Leave at the front door if not home")

payment1 = Payment(order_id=1, amount=500.0)
payment2 = Payment(order_id=2, amount=400.0)

contact1 = Contact(customer_id=1, contact_number="555-1234")
contact2 = Contact(customer_id=2, contact_number="555-5678")

supplier1 = Supplier(name="Supplier A", contact_number="555-0099")
supplier2 = Supplier(name="Supplier B", contact_number="555-0088")

shipment1 = Shipment(order_id=1, shipment_date=datetime.datetime.utcnow(), carrier="Carrier X")
shipment2 = Shipment(order_id=2, shipment_date=None, carrier="Carrier Y")

return1 = Return(item_id=1, reason="Defective")
return2 = Return(item_id=2, reason="Not required")

# Add objects to the session
session.add_all([customer1, customer2, order1, order2, product1, product2, item1, item2,
                 inventory1, inventory2, address1, address2, order_note1, order_note2,
                 payment1, payment2, contact1, contact2, supplier1, supplier2, shipment1, shipment2,
                 return1, return2])

# Commit the session to the database
session.commit()

# Define LogicBank rules
def declare_logic():
    Rule.constraint(
        validate=Customer,
        as_condition=lambda row: row.balance <= row.credit_limit,
        error_msg="Customer balance ({row.balance}) exceeds credit limit ({row.credit_limit})"
    )
    Rule.sum(
        derive=Customer.balance, 
        as_sum_of=Order.amount_total, 
        where=lambda row: row.date_shipped is None
    )
    Rule.sum(
        derive=Order.amount_total, 
        as_sum_of=Item.amount
    )
    Rule.formula(
        derive=Item.amount, 
        as_expression=lambda row: row.quantity * row.unit_price
    )
    Rule.copy(
        derive=Item.unit_price, 
        from_parent=Product.unit_price
    )
