from fastapi import APIRouter,HTTPException
from .schema import *
from database import sessionLocal
from model1 import *
import pandas as pd
import numpy as np
from  itertools import combinations
from sys import maxsize
import math

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    R = 6371.0
    distance = R * c
    
    return distance


def compare_driver_result(df:pd.DataFrame,race_df:pd.DataFrame):
    result_df=[]
    race_df['position_number'] = race_df['position_number'].replace(np.NaN, maxsize)
    df=df.groupby("constructor_id")
    for constructor_id,data in df:
        driver_list=list(combinations(data['driver_id'],2))
        for driver1,driver2 in driver_list:
            round1=set(race_df.loc[race_df['driver_id']==driver1,"round"].tolist())
            round2=set(race_df.loc[race_df['driver_id']==driver2,"round"].tolist())
            races_together=round1.intersection(round2)
            driver1_races=driver2_races=driver1_dnf=driver2_dnf=0
            for rounds in races_together:
                driver1round=race_df.loc[(race_df['driver_id']==driver1) & (race_df['round']==rounds),:].squeeze()
                driver2round=race_df.loc[(race_df['driver_id']==driver2) & (race_df['round']==rounds),:].squeeze()
                if  driver1round['position_number']==maxsize:
                    driver1_dnf+=1
                if  driver2round['position_number']==maxsize:
                    driver2_dnf+=1
                if (driver1round['position_number']<driver2round['position_number']) :
                    driver1_races+=1
                elif( driver1round['position_number']>driver2round['position_number']) :
                    driver2_races+=1
            result_df.append([constructor_id,driver1,driver2,driver1_races,driver2_races,driver1_dnf,driver2_dnf])
    return result_df

report_api=APIRouter(tags=['Reports'])

@report_api.post("/team_mate_comparision")
def retrive_team_mate_comparision(data:TeamMateIn):
    db=sessionLocal()
    output=[]
    result=db.query(SeasonEntrantDriver.driver_id,SeasonEntrantDriver.constructor_id).filter(SeasonEntrantDriver.year==data.year,SeasonEntrantDriver.rounds_text!=None).all()
    if not result:
        raise HTTPException(status_code=404,detail=f"No drivers found for the year - {data.year}")
    
    race_result=db.query(t_race_result).filter(t_race_result.c.year==data.year).all()
    sprint_result=db.query(t_sprint_race_result).filter(t_sprint_race_result.c.year==data.year).all()
    qualifying_result=db.query(t_qualifying_result).filter(t_qualifying_result.c.year==data.year).all()
    race_df=pd.DataFrame(race_result,columns=[t.name for t in t_race_result.columns])
    sprint_df=pd.DataFrame(sprint_result,columns=[t.name for t in t_sprint_race_result.columns])
    quali_df=pd.DataFrame(qualifying_result,columns=[t.name for t in t_qualifying_result.columns])
    df=pd.DataFrame(result,columns=['driver_id',"constructor_id"])

    result_df=compare_driver_result(df,race_df)
    result_array=np.array(result_df)
    sprint_result_df=compare_driver_result(df,sprint_df)
    sprint_result_array=np.array(sprint_result_df)
    quali_result_df=compare_driver_result(df,quali_df)
    quali_result_array=np.array(quali_result_df)

    team_result=db.query(Constructor).filter(Constructor.id.in_(result_array[:,0])).all()
    driver_result=db.query(Driver).filter(Driver.id.in_(result_array[:,1].tolist()+result_array[:,2].tolist())).all()
    const_dict={a.id:a for a in team_result}
    driver_dict={a.id:a for a in driver_result}
    output_dict={}

    for r in result_array:
        output_dict[(r[0],r[1],r[2])]=TeamMateOut(
            driver1=driver_dict[r[1]].name,
            driver2=driver_dict[r[2]].name,
            constructor=const_dict[r[0]].name,
            driver1_races=r[3],
            driver2_races=r[4],
            driver1_dnf=r[5],
            driver2_dnf=r[6],
        )
    for r in sprint_result_array:
        temp_data=output_dict[(r[0],r[1],r[2])]
        temp_data.sprint_driver1_races=int(r[3])
        temp_data.sprint_driver2_races=int(r[4])
        temp_data.sprint_driver1_dnf=int(r[5])
        temp_data.sprint_driver2_dnf=int(r[6])
        output_dict[(r[0],r[1],r[2])]=temp_data

    for r in quali_result_array:
        temp_data=output_dict[(r[0],r[1],r[2])]
        temp_data.quali_driver1=int(r[3])
        temp_data.quali_driver2=int(r[4])
        output_dict[(r[0],r[1],r[2])]=temp_data

    return list(output_dict.values())
        
@report_api.post("/distance_traveled")
def retrive_distance_travelled(data:TeamMateIn):
    db=sessionLocal()
    result=db.query(Race.round,Circuit.latitude,Circuit.longitude).filter(Race.circuit_id==Circuit.id,Race.year==data.year).order_by(Race.round).all()
    print(result)