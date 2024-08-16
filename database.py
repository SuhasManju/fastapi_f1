from sqlalchemy import create_engine,func
from sqlalchemy.orm import sessionmaker
from model1 import Base



engine=create_engine("mysql+pymysql://root:root@127.0.0.1/formula1_new")

sessionLocal=sessionmaker(bind=engine)


Base.metadata.create_all(engine)
