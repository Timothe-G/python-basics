from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

app = FastAPI()
engine = create_engine('postgresql://postgres:postgres@db/northwind')
Session = sessionmaker(bind=engine)

@app.get('/')
def read_root():
	session = Session()
	result = session.execute(text('SELECT customer_id, company_name, contact_name FROM customers LIMIT 10'))
	return {'Customers info': [dict(customerid=row[0], companyname=row[1], contactname=row[2]) for row in result]}
