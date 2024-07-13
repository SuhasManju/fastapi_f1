from pydantic import BaseModel
from typing import Optional,List

class RaceOut(BaseModel):
    round:int
    name:str
    start_date:str
    end_date:str
    location:str

class RaceDetailsOut(BaseModel):
    name:str
    fp1_timings:str
    fp2_timings:Optional[str]=None
    fp3_timings:Optional[str]=None
    quali_timings:Optional[str]=None
    race_timings:str
    sprint:bool
    sprint_quali_timings:Optional[str]=None
    sprint_race_timings:Optional[str]=None
#    circuit_image:str

class RaceResultIn(BaseModel):
    year:int
    round:int

class RaceResultOut(BaseModel):
    driver_name:str
    driver_id:str
    constructor_name:str
    constructor_id:str
    driver_number:int
    points:Optional[int]=None
    gap:Optional[str]=None
    interval:Optional[str]=None
    retired:Optional[str]=None

class QualiResultOut(BaseModel):
    driver_name:str
    driver_id:str
    constructor_name:str
    constructor_id:str
    driver_number:int
    q1:Optional[str]=None
    q2:Optional[str]=None
    q3:Optional[str]=None

class PracticeResultOut(BaseModel):
    driver_name:str
    driver_id:str
    constructor_name:str
    constructor_id:str
    driver_number:int
    time:Optional[str]=None
    gap:Optional[str]=None
    interval:Optional[str]=None
    retired:Optional[str]=None
    laps:int
