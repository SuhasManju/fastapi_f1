from fastapi import APIRouter,HTTPException
from database import sessionLocal
from model import *
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
    result=db.query(Race.round,Race.name,Race.fp1_date,Race.date,Circuit.name,Circuit.location,Circuit.country).join(Race,Race.circuitId==Circuit.circuitId).filter(Race.year==year).order_by(Race.round).all()
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
    circuit_result=db.query(Circuit).filter(Circuit.circuitId==result.circuitId).first()
    fp1timings=create_datetime(result.fp1_date,result.fp1_time)
    racetimings=create_datetime(result.date,result.time)
    fp2timings=None
    fp3timings=None
    sprintquali=None
    qualitimings=None
    sprinttimings=None
    sprint=True if result.sprint_date else False
    if sprint:
        sprinttimings=create_datetime(result.sprint_date,result.sprint_time)
        if year>=2024:
            qualitimings=create_datetime(result.quali_date,result.quali_time)
            sprintquali=create_datetime(result.fp2_date,result.fp2_time)
        else:
            fp2timings=create_datetime(result.fp2_date,result.fp2_time)
            qualitimings=create_datetime(result.quali_date,result.quali_time)
    else:
        fp2timings=create_datetime(result.fp2_date,result.fp2_time)
        fp3timings=create_datetime(result.fp3_date,result.fp3_time)
        qualitimings=create_datetime(result.quali_date,result.quali_time)
    
    return RaceDetailsOut(
        name=result.name,
        fp1_timings=str(fp1timings),
        fp2_timings=str(fp2timings) if fp2timings else None,
        fp3_timings=str(fp3timings) if fp3timings else None,
        quali_timings=str(qualitimings) if qualitimings else None,
        race_timings=str(racetimings),
        sprint=sprint,
        sprint_quali_timings=str(sprintquali) if sprintquali else None,
        sprint_race_timings=str(sprinttimings) if sprinttimings else None,
        circuit_image=convert_img_base64(f"circuit_images/{circuit_result.circuitId}.svg.png")
    )
    
@dashbboard.post('/round/result')
def retrive_round_result(data:RaceResultIn):
    db=sessionLocal()    
    result=db.query(Race).filter(Race.round==data.round,Race.year==data.year).first()
    race_result=db.query(Result).filter(Result.raceId==result.raceId).order_by(Result.position).all()
    output=[]
    if not race_result:
        raise HTTPException(status_code=404,detail="Race has not happened yet")
    for r in race_result:
        driver_result=db.query(Driver).filter(Driver.driverId==r.driverId).first()
        construct_result=db.query(Constructor).filter(Constructor.constructorId==r.constructorId).first()
        if r.position==1:
            time=None
        else:
            if not r.time:
                time=retrive_status(db,r.statusId)
            else:
                time=str(r.time)
        output.append(RaceResultOut(
            driver_name=retrive_name(driver_result.forename,driver_result.surname),
            driver_short_code=driver_result.driverRef,
            constructor_name=construct_result.name,
            constructor_short_code=construct_result.constructorRef,
            driver_number=r.number,
            points=r.points,
            time=time 

        ))
    return output

    