from sqlalchemy import create_engine,func
from sqlalchemy.orm import sessionmaker
from model1 import Base
from dotenv import load_dotenv
import os

load_dotenv()
database_url=os.getenv("database_url")

engine=create_engine(database_url)

sessionLocal=sessionmaker(bind=engine)

Base.metadata.create_all(engine)
