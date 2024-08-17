from model2 import Race as Race1, Circuit as Circuit1
from database2 import sessionLocal
from .schema import *
from fastapi import HTTPException
from function import *

def retrive_previous_round_timings(year:int):
    db=sessionLocal()
    result=db.query(Race1.round,Race1.name,Race1.fp1_date,Race1.date,Circuit1.name,Circuit1.location,Circuit1.country,Circuit1.lat,Circuit1.lng).filter(Circuit1.circuitId==Race1.circuitId,Race1.year==year).order_by(Race1.round).all()
    if not result:
        raise HTTPException(status_code=404,detail=f"Races not found for {year}")
    output=[]
    for round,name,start_date,end_date,circuit_name,location,country,lat,lng in result:
        output.append(
            RaceOut(
                round=round,
                name=name,
                start_date=str(start_date) if start_date else None,
                end_date=str(end_date),
                location=", ".join([circuit_name,location,country]),
                co_ordinates=[lat,lng]
            )
        )
    return output

def retrive_previous_round_detailed_timings(year:int,round:int):
    db=sessionLocal()
    result:Race1=db.query(Race1).filter(Race1.round==round,Race1.year==year).first()
    if not result:
        raise HTTPException(status_code=404,detail=f"Race Details not found year - {year} and round - {round}")
    fp1timings=create_datetime(result.fp1_date,result.fp1_time) if result.fp1_date else None
    racetimings=create_datetime(result.date,result.time)
    fp2timings=None
    fp3timings=None
    sprintquali=None
    qualitimings=create_datetime(result.quali_date,result.quali_time) if result.quali_date else None
    sprinttimings=None
    sprint=True if result.sprint_date else False
    if year==2023:
        if sprint:
            sprintquali=create_datetime(result.fp2_date,result.fp2_time)
            sprinttimings=create_datetime(result.sprint_date,result.sprint_time)
        else:
            fp2timings=create_datetime(result.fp2_date,result.fp2_time)
            fp3timings=create_datetime(result.fp3_date,result.fp3_time)
    else:
        if sprint:
            fp2timings=create_datetime(result.fp2_date,result.fp2_time)
            sprinttimings=create_datetime(result.sprint_date,result.sprint_time)
        else:
            fp2timings=create_datetime(result.fp2_date,result.fp2_time) if result.fp2_date else None
            fp3timings=create_datetime(result.fp3_date,result.fp3_time) if result.fp3_date else None
    return RaceDetailsOut(
            name=result.name,
            fp1_timings=str(fp1timings) if fp1timings else None,
            fp2_timings=str(fp2timings) if fp2timings else None,
            fp3_timings=str(fp3timings) if fp3timings else None,
            quali_timings=str(qualitimings) if qualitimings else None,
            race_timings=str(racetimings),
            sprint=sprint,
            sprint_quali_timings=str(sprintquali) if sprintquali else None,
            sprint_race_timings=str(sprinttimings) if sprinttimings else None,
            circuit_image=convert_img_base64(f"circuit_images/{year}/{round}.svg")
        )

    

