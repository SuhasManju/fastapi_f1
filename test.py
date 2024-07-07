from database import sessionLocal
from model import *
import os
from selenium import webdriver

driver=webdriver.Chrome()

db=sessionLocal()

result=db.query(Driver).all()
for r in result:
    print(r.driverId,r.number,r.forename,r.surname)
    driver.get(r.url)
    decesion=input("Continue")
    if decesion=="y":
        continue


