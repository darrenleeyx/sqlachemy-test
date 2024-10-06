import logging
from sqlalchemy import  create_engine, select
from sqlalchemy.orm import Session
from models import Base, Customer, CreditCard
from config import DATABASE_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_database():
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)
    return engine

def add_sample_data(session):
    try:
        customer_count = session.query(Customer).count()
        if customer_count == 0:
            logger.info("Adding sample customer data to the database.")
            for i in range(10):
                customer = Customer(name=f"Customer {i}", email=f"customer{i}@example.com")
                credit_card = CreditCard(number=f"123456789012345{i}", expiration_date="12/23")
                customer.credit_card = credit_card
                session.add(customer)
            session.commit()
        else:
            logger.info("Database already contains data. Skipping sample data insertion.")
    except Exception as e:
        logger.error(f"Error adding sample data: {e}")
        session.rollback()

def query_customers(session):
    try:
        query = select(Customer)
        result = session.execute(query).scalars().all()
        for customer in result:
            print(customer)
    except Exception as e:
        logger.error(f"Error querying customers: {e}")

def main():
    engine = setup_database()
    with Session(engine) as session:
        add_sample_data(session)
        query_customers(session)        

if __name__ == "__main__":
    main()