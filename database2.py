from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model2 import Base



engine=create_engine("mysql+pymysql://root:root@127.0.0.1/formula1")

sessionLocal=sessionmaker(bind=engine)


Base.metadata.create_all(engine)
