from fastapi import APIRouter,Depends,HTTPException
import fastf1
from .schema import *
import os
import pandas as pd
from datetime import timedelta

quali_reports=APIRouter(tags=['Quali Report'])

@quali_reports.post("/round/quali_result")
def retrive_quali_reports(data:RaceResultIn):
    directory=f"quali/laps/{data.year}/{data.round}"
    telemetry_directory=f"quali/telemetry/{data.year}/{data.round}"
    output=[]
    if os.path.exists(f"quali/laps/{data.year}/{data.round}/laps.csv"):
        laps=pd.read_csv(f"quali/laps/{data.year}/{data.round}/laps.csv")
        telemetry={}
        for driverId in laps['DriverNumber'].unique():
            telemetry[driverId]=pd.read_csv(f"{telemetry_directory}/{driverId}.csv")
    else:
        race=fastf1.get_session(year=data.year,gp=data.round,identifier="Q")
        race.load(laps=True)
        race.load(telemetry=True)
        laps=race.laps
        os.makedirs(directory)
        laps.to_csv(f"{directory}/laps.csv")
        telemetry=race.car_data
        telemetry_directory=f"quali/telemetry/{data.year}/{data.round}"
        os.makedirs(telemetry_directory)
        for driverId in laps['DriverNumber'].unique():
            telemetry[driverId].to_csv(f"{telemetry_directory}/{driverId}.csv")
    
    for driverId in laps['DriverNumber'].unique():
        lap_times=laps.loc[laps['DriverNumber']==driverId,:]
        telemetry_data=telemetry[driverId]
        lap_times.loc[:,'LapTime']=pd.to_timedelta(lap_times['LapTime'])
        lap_times.loc[:,'LapStartTime']=pd.to_timedelta(lap_times['LapStartTime'])
        shortest_time=lap_times.sort_values(['LapTime']).reset_index().iloc[0]
        lap_start_time=shortest_time["LapStartTime"]
        lap_end_time=lap_start_time+shortest_time['LapTime']
        telemetry_data.loc[:,'SessionTime']=pd.to_timedelta(telemetry_data['SessionTime'])
        quali_telemetry=telemetry_data.loc[telemetry_data['SessionTime']>=lap_start_time,:].loc[telemetry_data['SessionTime']<=lap_end_time,:]
        quali_telemetry['LapTime']=quali_telemetry['Time']-lap_start_time
        output.append(QualiAnalysisOut(
            driver_name=lap_times['Driver'].unique()[0],
            driver_number=driverId,
            lap_time=list(quali_telemetry['LapTime'].astype("str").values),
            speed=list(quali_telemetry['Speed'].values),
            throttle=list(quali_telemetry['Throttle'].values),
            rpm=list(quali_telemetry['RPM'].values),
            brake=list(quali_telemetry['Brake'].values),
            gear=list(quali_telemetry['nGear'].values),
        ))
        
    return output


