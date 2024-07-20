# coding: utf-8
from sqlalchemy import Column, Date, Float, Integer, String, Time, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Circuit(Base):
    __tablename__ = 'circuits'

    circuitId = Column(Integer, primary_key=True)
    circuitRef = Column(String(255), nullable=False, server_default=text("''"))
    name = Column(String(255), nullable=False, server_default=text("''"))
    location = Column(String(255))
    country = Column(String(255))
    lat = Column(Float)
    lng = Column(Float)
    alt = Column(Integer)
    url = Column(String(255), nullable=False, unique=True, server_default=text("''"))


class Constructorresult(Base):
    __tablename__ = 'constructorresults'

    constructorResultsId = Column(Integer, primary_key=True)
    raceId = Column(Integer, nullable=False, server_default=text("'0'"))
    constructorId = Column(Integer, nullable=False, server_default=text("'0'"))
    points = Column(Float)
    status = Column(String(255))


class Constructor(Base):
    __tablename__ = 'constructors'

    constructorId = Column(Integer, primary_key=True)
    constructorRef = Column(String(255), nullable=False, server_default=text("''"))
    name = Column(String(255), nullable=False, unique=True, server_default=text("''"))
    nationality = Column(String(255))
    url = Column(String(255), nullable=False, server_default=text("''"))


class Constructorstanding(Base):
    __tablename__ = 'constructorstandings'

    constructorStandingsId = Column(Integer, primary_key=True)
    raceId = Column(Integer, nullable=False, server_default=text("'0'"))
    constructorId = Column(Integer, nullable=False, server_default=text("'0'"))
    points = Column(Float, nullable=False, server_default=text("'0'"))
    position = Column(Integer)
    positionText = Column(String(255))
    wins = Column(Integer, nullable=False, server_default=text("'0'"))


class Driver(Base):
    __tablename__ = 'drivers'

    driverId = Column(Integer, primary_key=True)
    driverRef = Column(String(255), nullable=False, server_default=text("''"))
    number = Column(Integer)
    code = Column(String(3))
    forename = Column(String(255), nullable=False, server_default=text("''"))
    surname = Column(String(255), nullable=False, server_default=text("''"))
    dob = Column(Date)
    nationality = Column(String(255))
    url = Column(String(255), nullable=False, unique=True, server_default=text("''"))


class Driverstanding(Base):
    __tablename__ = 'driverstandings'

    driverStandingsId = Column(Integer, primary_key=True)
    raceId = Column(Integer, nullable=False, server_default=text("'0'"))
    driverId = Column(Integer, nullable=False, server_default=text("'0'"))
    points = Column(Float, nullable=False, server_default=text("'0'"))
    position = Column(Integer)
    positionText = Column(String(255))
    wins = Column(Integer, nullable=False, server_default=text("'0'"))


class Laptime(Base):
    __tablename__ = 'laptimes'

    raceId = Column(Integer, primary_key=True, nullable=False, index=True)
    driverId = Column(Integer, primary_key=True, nullable=False)
    lap = Column(Integer, primary_key=True, nullable=False)
    position = Column(Integer)
    time = Column(String(255))
    milliseconds = Column(Integer)


class Pitstop(Base):
    __tablename__ = 'pitstops'

    raceId = Column(Integer, primary_key=True, nullable=False, index=True)
    driverId = Column(Integer, primary_key=True, nullable=False)
    stop = Column(Integer, primary_key=True, nullable=False)
    lap = Column(Integer, nullable=False)
    time = Column(Time, nullable=False)
    duration = Column(String(255))
    milliseconds = Column(Integer)


class Qualifying(Base):
    __tablename__ = 'qualifying'

    qualifyId = Column(Integer, primary_key=True)
    raceId = Column(Integer, nullable=False, server_default=text("'0'"))
    driverId = Column(Integer, nullable=False, server_default=text("'0'"))
    constructorId = Column(Integer, nullable=False, server_default=text("'0'"))
    number = Column(Integer, nullable=False, server_default=text("'0'"))
    position = Column(Integer)
    q1 = Column(String(255))
    q2 = Column(String(255))
    q3 = Column(String(255))


class Race(Base):
    __tablename__ = 'races'

    raceId = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False, server_default=text("'0'"))
    round = Column(Integer, nullable=False, server_default=text("'0'"))
    circuitId = Column(Integer, nullable=False, server_default=text("'0'"))
    name = Column(String(255), nullable=False, server_default=text("''"))
    date = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    time = Column(Time)
    url = Column(String(255), unique=True)
    fp1_date = Column(Date)
    fp1_time = Column(Time)
    fp2_date = Column(Date)
    fp2_time = Column(Time)
    fp3_date = Column(Date)
    fp3_time = Column(Time)
    quali_date = Column(Date)
    quali_time = Column(Time)
    sprint_date = Column(Date)
    sprint_time = Column(Time)


class Result(Base):
    __tablename__ = 'results'

    resultId = Column(Integer, primary_key=True)
    raceId = Column(Integer, nullable=False, server_default=text("'0'"))
    driverId = Column(Integer, nullable=False, server_default=text("'0'"))
    constructorId = Column(Integer, nullable=False, server_default=text("'0'"))
    number = Column(Integer)
    grid = Column(Integer, nullable=False, server_default=text("'0'"))
    position = Column(Integer)
    positionText = Column(String(255), nullable=False, server_default=text("''"))
    positionOrder = Column(Integer, nullable=False, server_default=text("'0'"))
    points = Column(Float, nullable=False, server_default=text("'0'"))
    laps = Column(Integer, nullable=False, server_default=text("'0'"))
    time = Column(String(255))
    milliseconds = Column(Integer)
    fastestLap = Column(Integer)
    rank = Column(Integer, server_default=text("'0'"))
    fastestLapTime = Column(String(255))
    fastestLapSpeed = Column(String(255))
    statusId = Column(Integer, nullable=False, server_default=text("'0'"))


class Season(Base):
    __tablename__ = 'seasons'

    year = Column(Integer, primary_key=True, server_default=text("'0'"))
    url = Column(String(255), nullable=False, unique=True, server_default=text("''"))


class Sprintresult(Base):
    __tablename__ = 'sprintresults'

    sprintResultId = Column(Integer, primary_key=True)
    raceId = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    driverId = Column(Integer, nullable=False, server_default=text("'0'"))
    constructorId = Column(Integer, nullable=False, server_default=text("'0'"))
    number = Column(Integer, nullable=False, server_default=text("'0'"))
    grid = Column(Integer, nullable=False, server_default=text("'0'"))
    position = Column(Integer)
    positionText = Column(String(255), nullable=False, server_default=text("''"))
    positionOrder = Column(Integer, nullable=False, server_default=text("'0'"))
    points = Column(Float, nullable=False, server_default=text("'0'"))
    laps = Column(Integer, nullable=False, server_default=text("'0'"))
    time = Column(String(255))
    milliseconds = Column(Integer)
    fastestLap = Column(Integer)
    fastestLapTime = Column(String(255))
    statusId = Column(Integer, nullable=False, server_default=text("'0'"))


class Status(Base):
    __tablename__ = 'status'

    statusId = Column(Integer, primary_key=True)
    status = Column(String(255), nullable=False, server_default=text("''"))
