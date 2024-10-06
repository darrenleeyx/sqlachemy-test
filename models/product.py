from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base

class Product(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Float)
    description = Column(String, nullable=True)
    category = Column(String, nullable=True)
    orders = relationship("Order", back_populates="product")
    
    def __repr__(self) -> str:
        return f"<Product(name={self.name}, price={self.price}, description={self.description}, category={self.category})>"