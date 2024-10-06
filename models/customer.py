from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Customer(Base):
    __tablename__ = "customer"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    credit_card = relationship("CreditCard", uselist=False, back_populates="customer")
    orders = relationship("Order", back_populates="customer")
    
    def __repr__(self) -> str:
        return f"<Customer(name={self.name}, email={self.email})>"