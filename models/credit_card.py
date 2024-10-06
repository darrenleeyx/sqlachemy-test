from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class CreditCard(Base):
    __tablename__ = "credit_card"
    
    id = Column(Integer, primary_key=True)
    number = Column(String(19))
    expiration_date = Column(String(10))
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="credit_card")
    
    def __repr__(self) -> str:
        return f"<CreditCard(number={self.number}, expiration_date={self.expiration_date}, customer_id={self.customer_id})>"