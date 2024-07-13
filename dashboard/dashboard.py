from fastapi import APIRouter,HTTPException
from database import sessionLocal
from model1 import *
from .schema import *
from function import *


dashbboard=APIRouter(tags=['Dashboard'])

@dashbboard.get('/season')
def retrive_year():
    db=sessionLocal()
    result=db.query(Season).order_by(Season.year).all()
    return [r.year for r in result]

@dashbboard.get("/driver_standing")
def retrive_driver_standing(year:str):
    db=sessionLocal()


@dashbboard.get('/round')
def retrive_round(year:str):
    db=sessionLocal()
    output=[]
    result=db.query(Race.round,Race.official_name,Race.free_practice_1_date,Race.date,Circuit.name,Circuit.place_name,Country.name).join(Race,Race.circuit_id==Circuit.id).join(Country,Circuit.country_id==Country.id).filter(Race.year==year).order_by(Race.round).all()
    for round,name,start_date,end_date,circuit_name,location,country in result:
        output.append(RaceOut(
            round=round,
            name=name,
            start_date=str(start_date),
            end_date=str(end_date),
            location=", ".join([circuit_name,location,country])
        ))
    return output

@dashbboard.get('/round/detailed')
def retrive_detailed_round(year:int,round:int):
    db=sessionLocal()
    result=db.query(Race).filter(Race.round==round,Race.year==year).first()
    circuit_result=db.query(Circuit).filter(Circuit.id==result.circuit_id).first()
    fp1timings=create_datetime(result.free_practice_1_date,result.free_practice_1_time)
    racetimings=create_datetime(result.date,result.time)
    fp2timings=None
    fp3timings=None
    sprintquali=None
    qualitimings=None
    sprinttimings=None
    sprint=True if result.sprint_race_date else False
    if sprint:
        sprinttimings=create_datetime(result.sprint_race_date,result.sprint_race_time)
        if year>=2024:
            qualitimings=create_datetime(result.qualifying_date,result.qualifying_time)
            sprintquali=create_datetime(result.sprint_qualifying_date,result.sprint_qualifying_time)
        else:
            fp2timings=create_datetime(result.free_practice_2_date,result.free_practice_2_time)
            qualitimings=create_datetime(result.qualifying_date,result.qualifying_time)
    else:
        fp2timings=create_datetime(result.free_practice_2_date,result.free_practice_2_time)
        fp3timings=create_datetime(result.free_practice_3_date,result.free_practice_3_time)
        qualitimings=create_datetime(result.qualifying_date,result.qualifying_time)
    
    return RaceDetailsOut(
        name=result.official_name,
        fp1_timings=str(fp1timings),
        fp2_timings=str(fp2timings) if fp2timings else None,
        fp3_timings=str(fp3timings) if fp3timings else None,
        quali_timings=str(qualitimings) if qualitimings else None,
        race_timings=str(racetimings),
        sprint=sprint,
        sprint_quali_timings=str(sprintquali) if sprintquali else None,
        sprint_race_timings=str(sprinttimings) if sprinttimings else None,
        #circuit_image=convert_img_base64(f"circuit_images/{circuit_result.circuitId}.svg.png")
    )
    
@dashbboard.post('/round/race_result',response_model=List[RaceResultOut])
def retrive_round_result(data:RaceResultIn):
    retire_racers=[]
    db=sessionLocal()    
    result=db.query(Race).filter(Race.round==data.round,Race.year==data.year).first()
    race_result=db.query(t_race_result).filter(t_race_result.c.race_id==result.id).order_by(t_race_result.c.position_number).all()
    output=[]
    columns=t_race_result.c.keys()
    if not race_result:
        raise HTTPException(status_code=404,detail="Race has not happened yet")
    for r in race_result:
        race_data=dict(zip(columns,r))
        driver_result=db.query(Driver).filter(Driver.id==race_data['driver_id']).first()
        constructor_result=db.query(Constructor).filter(Constructor.id==race_data['constructor_id']).first()
        if race_data['position_number']:
            output.append(RaceResultOut(
                driver_name=driver_result.name,
                driver_id=race_data['driver_id'],
                constructor_name=constructor_result.name,
                constructor_id=race_data['constructor_id'],
                driver_number=race_data['driver_number'],
                points=race_data['points'],
                gap=race_data['gap'],
                interval=race_data['interval'],
                retired=race_data['reason_retired'],
                position_number=race_data['position_number']
        ))
        else:
            retire_racers.append(RaceResultOut(
                driver_name=driver_result.name,
                driver_id=race_data['driver_id'],
                constructor_name=constructor_result.name,
                constructor_id=race_data['constructor_id'],
                driver_number=race_data['driver_number'],
                points=race_data['points'],
                gap=race_data['gap'],
                interval=race_data['interval'],
                retired=race_data['reason_retired'],
                position_number=race_data['position_number']
        ))
    output.extend(retire_racers)
    return output

@dashbboard.post('/round/sprint_result')
def retive_sprint_result(data:RaceResultIn):
    db=sessionLocal()
    output=[]
    result=db.query(Race).filter(Race.round==data.round,Race.year==data.year).first()
    if not result.sprint_race_date:
        raise HTTPException(status_code=400,detail="This Race is not a sprint race")
    race_result=db.query(t_sprint_race_result).filter(t_sprint_race_result.c.race_id==result.id).order_by(t_sprint_race_result.c.position_number).all()
    columns=t_sprint_race_result.c.keys()
    if not race_result:
        raise HTTPException(status_code=404,detail="Race has not happened yet")
    for r in race_result:
        race_data=dict(zip(columns,r))
        driver_result=db.query(Driver).filter(Driver.id==race_data['driver_id']).first()
        constructor_result=db.query(Constructor).filter(Constructor.id==race_data['constructor_id']).first()
        output.append(RaceResultOut(
            driver_name=driver_result.name,
            driver_id=race_data['driver_id'],
            constructor_name=constructor_result.name,
            constructor_id=race_data['constructor_id'],
            driver_number=race_data['driver_number'],
            points=race_data['points'],
            gap=race_data['gap'],
            interval=race_data['interval'],
            retired=race_data['reason_retired'],
            position_number=race_data['position_number']
        ))
    return output


@dashbboard.post('/round/race_quali_result')
def retrive_quali_result(data:RaceResultIn):
    db=sessionLocal()
    output=[]
    result=db.query(Race).filter(Race.round==data.round,Race.year==data.year).first()
    quali_result=db.query(t_qualifying_result).filter(t_qualifying_result.c.race_id==result.id).order_by(t_qualifying_result.c.position_number).all()
    if not quali_result:
        raise HTTPException(status_code=404,detail="Qualifying result not found")
    columns=t_qualifying_result.c.keys()
    for r in quali_result:
        race_data=dict(zip(columns,r))
        driver_result=db.query(Driver).filter(Driver.id==race_data['driver_id']).first()
        constructor_result=db.query(Constructor).filter(Constructor.id==race_data['constructor_id']).first()
        output.append(QualiResultOut(
            driver_name=driver_result.name,
            driver_id=driver_result.id,
            constructor_name=constructor_result.name,
            constructor_id=constructor_result.id,
            driver_number=race_data['driver_number'],
            q1=race_data['q1'],
            q2=race_data['q2'],
            q3=race_data['q3'],
            position_number=race_data['position_number']
        ))
    return output

@dashbboard.post('/round/sprint_quali_result')
def retrive_sprint_quali_result(data:RaceResultIn):
    db=sessionLocal()
    output=[]
    result=db.query(Race).filter(Race.round==data.round,Race.year==data.year).first()
    quali_result=db.query(t_sprint_qualifying_result).filter(t_sprint_qualifying_result.c.race_id==result.id).order_by(t_sprint_qualifying_result.c.position_number).all()
    if not quali_result:
        raise HTTPException(status_code=404,detail="Qualifying result not found")
    columns=t_sprint_qualifying_result.c.keys()
    for r in quali_result:
        race_data=dict(zip(columns,r))
        driver_result=db.query(Driver).filter(Driver.id==race_data['driver_id']).first()
        constructor_result=db.query(Constructor).filter(Constructor.id==race_data['constructor_id']).first()
        output.append(QualiResultOut(
            driver_name=driver_result.name,
            driver_id=driver_result.id,
            constructor_name=constructor_result.name,
            constructor_id=constructor_result.id,
            driver_number=race_data['driver_number'],
            q1=race_data['q1'],
            q2=race_data['q2'],
            q3=race_data['q3'],
            position_number=race_data['position_number']
        ))
    return output
    
@dashbboard.post('/round/fp1_result')
def retive_sprint_result(data:RaceResultIn):
    db=sessionLocal()
    output=[]
    result=db.query(Race).filter(Race.round==data.round,Race.year==data.year).first()
    race_result=db.query(t_free_practice_1_result).filter(t_free_practice_1_result.c.race_id==result.id).order_by(t_free_practice_1_result.c.position_number).all()
    columns=t_free_practice_1_result.c.keys()
    if not race_result:
        raise HTTPException(status_code=404,detail="Race has not happened yet")
    for r in race_result:
        race_data=dict(zip(columns,r))
        driver_result=db.query(Driver).filter(Driver.id==race_data['driver_id']).first()
        constructor_result=db.query(Constructor).filter(Constructor.id==race_data['constructor_id']).first()
        output.append(PracticeResultOut(
            driver_name=driver_result.name,
            driver_id=race_data['driver_id'],
            constructor_name=constructor_result.name,
            constructor_id=race_data['constructor_id'],
            driver_number=race_data['driver_number'],
            gap=race_data['gap'],
            interval=race_data['interval'],
            laps=race_data['laps'],
            time=str(race_data['time']),
            position_number=race_data['position_number']
        ))
    return output

@dashbboard.post('/round/fp2_result')
def retive_sprint_result(data:RaceResultIn):
    db=sessionLocal()
    output=[]
    result=db.query(Race).filter(Race.round==data.round,Race.year==data.year).first()
    race_result=db.query(t_free_practice_2_result).filter(t_free_practice_2_result.c.race_id==result.id).order_by(t_free_practice_2_result.c.position_number).all()
    columns=t_free_practice_2_result.c.keys()
    if not race_result:
        raise HTTPException(status_code=404,detail="Race has not happened yet")
    for r in race_result:
        race_data=dict(zip(columns,r))
        driver_result=db.query(Driver).filter(Driver.id==race_data['driver_id']).first()
        constructor_result=db.query(Constructor).filter(Constructor.id==race_data['constructor_id']).first()
        output.append(PracticeResultOut(
            driver_name=driver_result.name,
            driver_id=race_data['driver_id'],
            constructor_name=constructor_result.name,
            constructor_id=race_data['constructor_id'],
            driver_number=race_data['driver_number'],
            gap=race_data['gap'],
            interval=race_data['interval'],
            laps=race_data['laps'],
            time=str(race_data['time']),
            position_number=race_data['position_number']
        ))
    return output

@dashbboard.post('/round/fp3_result')
def retive_sprint_result(data:RaceResultIn):
    db=sessionLocal()
    output=[]
    result=db.query(Race).filter(Race.round==data.round,Race.year==data.year).first()
    race_result=db.query(t_free_practice_3_result).filter(t_free_practice_3_result.c.race_id==result.id).order_by(t_free_practice_3_result.c.position_number).all()
    columns=t_free_practice_3_result.c.keys()
    if not race_result:
        raise HTTPException(status_code=404,detail="Race has not happened yet")
    for r in race_result:
        race_data=dict(zip(columns,r))
        driver_result=db.query(Driver).filter(Driver.id==race_data['driver_id']).first()
        constructor_result=db.query(Constructor).filter(Constructor.id==race_data['constructor_id']).first()
        output.append(PracticeResultOut(
            driver_name=driver_result.name,
            driver_id=race_data['driver_id'],
            constructor_name=constructor_result.name,
            constructor_id=race_data['constructor_id'],
            time=str(race_data['time']),
            driver_number=race_data['driver_number'],
            gap=race_data['gap'],
            interval=race_data['interval'],
            laps=race_data['laps'],
            position_number=race_data['position_number']
        ))
    return output