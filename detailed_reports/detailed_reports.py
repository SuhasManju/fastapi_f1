from fastapi import APIRouter,Depends,HTTPException
import fastf1._api
import fastf1.plotting
from .schema import *
from database import sessionLocal
from model1 import *
import pandas as pd
import fastf1
import os
import json
import numpy as np

detailed_api=APIRouter(tags=['Detailed report'])

@detailed_api.post("/round/race_result/pitsop")
def retrive_laptimes(data:RaceResultIn):
    """
    Input: \n
        year: Integer [2023,2024] \n
        round: Integer [1,2,3,....] \n
    Output: \n
    Returns list of all the pitstop done during the race with time \n
        [ {
            "driver_name": "Sergio Pérez",  \n
            "driver_number": "11",  \n
            "constructor": "Red Bull",  \n
            "lap": 31,  \n
            "time": "21.464"  \n
        }]
    """
    db=sessionLocal()
    output=[]
    race_result=db.query(Race).filter(Race.round==data.round,Race.year==data.year).first()
    result=db.query(Driver.name,t_pit_stop.c.driver_number,t_pit_stop.c.lap,t_pit_stop.c.time,Constructor.name).filter(t_pit_stop.c.race_id==race_result.id,t_pit_stop.c.driver_id==Driver.id,t_pit_stop.c.constructor_id==Constructor.id).order_by(t_pit_stop.c.time_millis).all()
    for r in result:
        output.append(PitStopOut(
            driver_name=r[0],
            driver_number=r[1],
            constructor=r[-1],
            lap=r[2],
            time=r[3]
        ))
    return output

@detailed_api.post("/round/race_result/driver_info")
def retrive_driver_info(data:RaceResultIn):
    """
    Input: \n
        year: Integer [2023,2024] \n
        round: Integer [1,2,3,....] \n
    Output: \n
    Returns list of all the drivers that drove during the weekend. \n
        [{"RacingNumber": "4", \n
        "BroadcastName": "L NORRIS", \n
        "FullName": "Lando NORRIS", \n
        "Tla": "NOR", \n
        "Line": 2, \n
        "TeamName": "McLaren", \n
        "TeamColour": "FF8000", \n
        "FirstName": "Lando", \n
        "LastName": "Norris", \n
        "Reference": "LANNOR01", \n
        "HeadshotUrl": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/L/LANNOR01_Lando_Norris/lannor01.png.transform/1col/image.png", \n
        "CountryCode": "GBR"}] \n
    """
    directory=f"race/laps/{data.year}/{data.round}"
    if os.path.exists(f"{directory}/driver_data.json"):
        with open(f"{directory}/driver_data.json","r") as json_file:
            driver_data=json.load(json_file)
        driver_data={int(k):v for k,v in driver_data.items()}
        return list(driver_data.values())
    else:
        race=fastf1.get_session(year=data.year,gp=data.round,identifier="Race")
        driver_data=fastf1._api.driver_info(race.api_path)
        return list(driver_data.values())
    
@detailed_api.get("/colours")
def retrive_driver_colour():
    return {"driver_colour":fastf1.plotting.DRIVER_COLORS,"team_colours":fastf1.plotting.TEAM_COLORS,"compound_colours":fastf1.plotting.COMPOUND_COLORS}

@detailed_api.post("/round/race_result/laptimes")
def retrive_pipstops(data:RaceResultIn):
    """
    Input: \n
        year: Integer [2023,2024] \n
        round: Integer [1,2,3,....] \n
    Output: \n
        Returns list of laptimes, tyre, pit in lap for all the lap done by driver during the race \n
        [
        {
        "driver_name": "Max VERSTAPPEN", \n
        "driver_number": 1, \n
        "laps":[1,...,58], \n
        "laptime:["00:01:23.186000",....,"00:01:16.186000"], \n
        "pitstop":[false,...,true,...,false], \n
        "compound:["soft",....,"medium",...,"soft"] \n
        }
        ]
    """
    directory=f"race/laps/{data.year}/{data.round}"
    if os.path.exists(f"{directory}/laps.csv"):
        race_laps=pd.read_csv(f"{directory}/laps.csv")
        with open(f"{directory}/driver_data.json","r") as json_file:
            driver_data=json.load(json_file)
        driver_data={int(k):v for k,v in driver_data.items()}
    else:
        race=fastf1.get_session(year=data.year,gp=data.round,identifier="Race")  
        race.load(laps=True)
        race_laps=race.laps
        os.makedirs(directory)
        race_laps.to_csv(f"{directory}/laps.csv")
        driver_data=fastf1._api.driver_info(race.api_path)
        with open(f"{directory}/driver_data.json","w") as json_file:
            json.dump(driver_data,json_file,indent=4)
    output=[]
    race_laps['PitInTime']=pd.to_timedelta(race_laps['PitInTime'])
    race_laps["PitInTime"]=race_laps['PitInTime'].astype('timedelta64[s]').astype('int64')
    race_laps['LapTime']=race_laps['LapTime'].apply(lambda x: x[7:])
    for driverId in race_laps['DriverNumber'].unique():
        driver_result=driver_data[driverId]
        lap_times=race_laps.loc[race_laps['DriverNumber']==driverId,['LapNumber',"Compound","LapTime","PitInTime"]]
        lap_times['PitStop']=lap_times['PitInTime'].apply(lambda x:True if x>0 else False)
        laps=list(lap_times['LapNumber'].values)
        laptime=list(lap_times['LapTime'].values)
        pipstop=list(lap_times["PitStop"].values)
        compound=list(lap_times['Compound'].values)
        output.append(LapTimesOut(
            driver_name=driver_result['FullName'],
            driver_number=driverId,
            laptime=laptime,
            laps=laps,
            pitstop=pipstop,
            compound=compound
        ))
    return output