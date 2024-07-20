from fastapi import APIRouter,Depends,HTTPException
import fastf1.api
from .schema import *
from database2 import sessionLocal
from model2 import *
import pandas as pd
import fastf1
import fastf1.api

detailed_api=APIRouter(tags=['Detailed report'])

@detailed_api.post("/round/race_result/laptimes")
def retrive_laptimes(data:RaceResultIn):
    db=sessionLocal()
    output=[]
    race_result=db.query(Race).filter(Race.round==data.round,Race.year==data.year).first()
    result=db.query(Laptime.raceId,Laptime.driverId,Laptime.lap,Laptime.position,Laptime.time,Laptime.milliseconds).filter(Laptime.raceId==race_result.raceId).all()
    df=pd.DataFrame(result,columns=["raceId","driverId","lap","position","time","milliseconds"])
    for driverId in df['driverId'].unique():
        lap_df=df.loc[df['driverId']==driverId,:]
        driver_result=db.query(Driver).filter(Driver.driverId==driverId).first()
        laps=list(lap_df['lap'].values)
        position=list(lap_df['position'].values)
        laptimes=list(lap_df["time"].values)
        output.append(LapTimesOut(
            driver_name=driver_result.forename+" "+driver_result.surname,
            driver_number=driver_result.number,
            laps=laps,
            laptimes=laptimes,
            position=position
        ))
    return output

@detailed_api.post("/round/race_result/driver_info")
def retrive_driver_info(data:RaceResultIn):
    race=fastf1.get_session(year=data.year,gp=data.round,identifier="Race")
    driver_data=fastf1.api.driver_info(race.api_path)
    return list(driver_data.values())

@detailed_api.post("/round/race_result/pitstop")
def retrive_pipstops(data:RaceResultIn):
    db=sessionLocal()
    race=fastf1.get_session(year=data.year,gp=data.round,identifier="Race")  
    race.load(laps=True)
    race_laps=race.laps
    output=[]
    driver_data=fastf1.api.driver_info(race.api_path)
    for driverId in race_laps['DriverNumber'].unique():
        driver_result=driver_data[driverId]
        lap_times=race_laps.loc[race_laps['DriverNumber']==driverId,['LapNumber',"Compound"]]
        laps=list(lap_times['LapNumber'].values)
        compound=list(lap_times['Compound'].values)
        output.append(DriverPitStop(
            driver_name=driver_result['FullName'],
            driver_number=driverId,
            laps=laps,
            compound=compound
        ))
    return output

    