from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Order(Base):
    __tablename__ = "order"
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="orders")
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="orders")
    quantity = Column(Integer)

    def __repr__(self) -> str:
        return f"<Order(customer_id={self.customer_id}, product_id={self.product_id}, quantity={self.quantity})>"