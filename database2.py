from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model2 import Base
from dotenv import load_dotenv
import os

load_dotenv()

database_url=os.getenv("database_url2")

<<<<<<< HEAD
engine=create_engine("mysql+pymysql://root:root@127.0.0.1/formula1")

sessionLocal=sessionmaker(bind=engine)


Base.metadata.create_all(engine)
=======
engine=create_engine(database_url)

sessionLocal=sessionmaker(bind=engine)

Base.metadata.create_all(engine)
>>>>>>> ce747e1cc7fb507843c459e8296c5ae0dfd0220e
