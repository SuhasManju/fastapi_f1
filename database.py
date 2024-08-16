from sqlalchemy import create_engine,func
from sqlalchemy.orm import sessionmaker
from model1 import Base
from dotenv import load_dotenv
import os

load_dotenv()
database_url=os.getenv("database_url")

<<<<<<< HEAD

engine=create_engine("mysql+pymysql://root:root@127.0.0.1/formula1_new")
=======
engine=create_engine(database_url)
>>>>>>> ce747e1cc7fb507843c459e8296c5ae0dfd0220e

sessionLocal=sessionmaker(bind=engine)

Base.metadata.create_all(engine)
