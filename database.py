from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base


engine=create_engine("mysql+pymysql://root:root@localhost/formula1")
sessionLocal=sessionmaker(bind=engine)

Base.metadata.create_all(engine)