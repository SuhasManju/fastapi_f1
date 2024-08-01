from pydantic import BaseModel
from typing import Optional,List

class RaceResultIn(BaseModel):
    year:int
    round:int

class PitStopOut(BaseModel):
    driver_name:str
    driver_number:str | int
    constructor:str
    lap:int
    time:str
    
class LapTimesOut(BaseModel):
    driver_name:str
    driver_number:int|str
    laptime:List[str]
    laps:List[int]
    compound:List[str]
    pitstop:List[bool]
