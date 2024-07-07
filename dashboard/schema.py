from pydantic import BaseModel
from typing import Optional

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
    circuit_image:str