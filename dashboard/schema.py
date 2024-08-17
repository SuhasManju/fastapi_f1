from pydantic import BaseModel
from typing import Optional,List

class RaceOut(BaseModel):
    round:int
    name:str
    start_date:Optional[str]=None
    end_date:str
    location:str
    co_ordinates:Optional[List[float]]=None

class DriverStandingOut(BaseModel):
    driver_name:str
    number:Optional[int]=None
    driver_id:str
    constructor_name:str
    points:Optional[float]=0
    position:Optional[int]=0

class ConstructorStandingOut(BaseModel):
    year:int
    constructor_name:str
    constructor_id:str
    points:float
    position:int

class RaceDetailsOut(BaseModel):
    name:str
    fp1_timings:Optional[str]=None
    fp2_timings:Optional[str]=None
    fp3_timings:Optional[str]=None
    quali_timings:Optional[str]=None
    race_timings:str
    sprint:bool
    sprint_quali_timings:Optional[str]=None
    sprint_race_timings:Optional[str]=None
    circuit_image:Optional[str]=None

class RaceResultIn(BaseModel):
    year:int
    round:int

class DriverStandingDetailed(BaseModel):
    driver_id:str
    driver_number:int
    round:List[int]
    points:List[float]

class ConstructorStandingDetailed(BaseModel):
    constructor_name:str
    round:List[int]
    points:List[float]

class RaceResultOut(BaseModel):
    driver_name:str
    driver_id:str
    constructor_name:str
    constructor_id:str
    driver_number:int
    points:Optional[float]=None
    position_number:Optional[int]=None
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
    position_number:Optional[int]=None

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
    position_number:Optional[int]=None
