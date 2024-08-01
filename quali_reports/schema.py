from pydantic import BaseModel
from typing import Optional,List,Any

class RaceResultIn(BaseModel):
    year:int
    round:int

class QualiAnalysisOut(BaseModel):
    driver_name:str
    driver_number:int|str
    lap_time:List[str]
    speed:List[int]
    throttle:List[int]
    rpm:List[int]
    brake:List[int]
    gear:List[int]
