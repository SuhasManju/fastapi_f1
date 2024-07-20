from pydantic import BaseModel
from typing import Optional,List

class RaceResultIn(BaseModel):
    year:int
    round:int

class LapTimesOut(BaseModel):
    driver_name:str
    driver_number:int|str
    laps:List[int]
    laptimes:List[str]
    position:List[int]

class DriverPitStop(BaseModel):
    driver_name:str
    driver_number:int|str
    laps:List[int]
    compound:List[str]
