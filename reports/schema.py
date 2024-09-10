from pydantic import BaseModel
from typing import Optional

class TeamMateIn(BaseModel):
    year:int

class TeamMateOut(BaseModel):
    driver1:str
    driver2:str
    constructor:str
    driver1_races:int
    driver2_races:int
    driver1_dnf:int
    driver2_dnf:int
    sprint_driver1_races:Optional[int]=None
    sprint_driver2_races:Optional[int]=None
    sprint_driver1_dnf:Optional[int]=None
    sprint_driver2_dnf:Optional[int]=None
    quali_driver1:Optional[int]=None
    quali_driver2:Optional[int]=None