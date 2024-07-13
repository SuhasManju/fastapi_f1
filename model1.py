# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, ForeignKey, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Continent(Base):
    __tablename__ = 'continent'

    id = Column(String(100), primary_key=True)
    code = Column(String(2), nullable=False, unique=True)
    name = Column(String(100), nullable=False, unique=True)
    demonym = Column(String(100), nullable=False)


t_driver_of_the_day_result = Table(
    'driver_of_the_day_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('percentage', DECIMAL(4, 1))
)


class Entrant(Base):
    __tablename__ = 'entrant'

    id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False, index=True)


t_fastest_lap = Table(
    'fastest_lap', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('lap', Integer),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer)
)


t_free_practice_1_result = Table(
    'free_practice_1_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('laps', Integer)
)


t_free_practice_2_result = Table(
    'free_practice_2_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('laps', Integer)
)


t_free_practice_3_result = Table(
    'free_practice_3_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('laps', Integer)
)


t_free_practice_4_result = Table(
    'free_practice_4_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('laps', Integer)
)


t_pit_stop = Table(
    'pit_stop', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('stop', Integer),
    Column('lap', Integer),
    Column('time', String(20)),
    Column('time_millis', Integer)
)


t_pre_qualifying_result = Table(
    'pre_qualifying_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('laps', Integer)
)


t_qualifying_1_result = Table(
    'qualifying_1_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('laps', Integer)
)


t_qualifying_2_result = Table(
    'qualifying_2_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('laps', Integer)
)


t_qualifying_result = Table(
    'qualifying_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('q1', String(20)),
    Column('q1_millis', Integer),
    Column('q2', String(20)),
    Column('q2_millis', Integer),
    Column('q3', String(20)),
    Column('q3_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('laps', Integer)
)


t_race_result = Table(
    'race_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('shared_car', TINYINT(1)),
    Column('laps', Integer),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('time_penalty', String(20)),
    Column('time_penalty_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('gap_laps', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('reason_retired', String(100)),
    Column('points', DECIMAL(8, 2)),
    Column('grid_position_number', Integer),
    Column('grid_position_text', String(2)),
    Column('positions_gained', Integer),
    Column('pit_stops', Integer),
    Column('fastest_lap', TINYINT(1)),
    Column('driver_of_the_day', TINYINT(1)),
    Column('grand_slam', TINYINT(1))
)


class Season(Base):
    __tablename__ = 'season'

    year = Column(Integer, primary_key=True)


t_sprint_qualifying_result = Table(
    'sprint_qualifying_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('q1', String(20)),
    Column('q1_millis', Integer),
    Column('q2', String(20)),
    Column('q2_millis', Integer),
    Column('q3', String(20)),
    Column('q3_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('laps', Integer)
)


t_sprint_race_result = Table(
    'sprint_race_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('laps', Integer),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('time_penalty', String(20)),
    Column('time_penalty_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('gap_laps', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('reason_retired', String(100)),
    Column('points', DECIMAL(8, 2)),
    Column('grid_position_number', Integer),
    Column('grid_position_text', String(2)),
    Column('positions_gained', Integer)
)


t_sprint_starting_grid_position = Table(
    'sprint_starting_grid_position', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('grid_penalty', String(20)),
    Column('grid_penalty_positions', Integer),
    Column('time', String(20)),
    Column('time_millis', Integer)
)


t_starting_grid_position = Table(
    'starting_grid_position', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('grid_penalty', String(20)),
    Column('grid_penalty_positions', Integer),
    Column('time', String(20)),
    Column('time_millis', Integer)
)


t_warming_up_result = Table(
    'warming_up_result', metadata,
    Column('race_id', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('position_display_order', Integer),
    Column('position_number', Integer),
    Column('position_text', String(4)),
    Column('driver_number', String(3)),
    Column('driver_id', String(100)),
    Column('constructor_id', String(100)),
    Column('engine_manufacturer_id', String(100)),
    Column('tyre_manufacturer_id', String(100)),
    Column('time', String(20)),
    Column('time_millis', Integer),
    Column('gap', String(20)),
    Column('gap_millis', Integer),
    Column('interval', String(20)),
    Column('interval_millis', Integer),
    Column('laps', Integer)
)


class Country(Base):
    __tablename__ = 'country'

    id = Column(String(100), primary_key=True)
    alpha2_code = Column(String(2), nullable=False, unique=True)
    alpha3_code = Column(String(3), nullable=False, unique=True)
    name = Column(String(100), nullable=False, unique=True)
    demonym = Column(String(100))
    continent_id = Column(ForeignKey('continent.id'), nullable=False, index=True)

    continent = relationship('Continent')


class Circuit(Base):
    __tablename__ = 'circuit'

    id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    full_name = Column(String(100), nullable=False, index=True)
    previous_names = Column(String(255))
    type = Column(String(6), nullable=False, index=True)
    place_name = Column(String(100), nullable=False, index=True)
    country_id = Column(ForeignKey('country.id'), nullable=False, index=True)
    latitude = Column(DECIMAL(10, 6), nullable=False)
    longitude = Column(DECIMAL(10, 6), nullable=False)
    total_races_held = Column(Integer, nullable=False)

    country = relationship('Country')


class Constructor(Base):
    __tablename__ = 'constructor'

    id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    full_name = Column(String(100), nullable=False, index=True)
    country_id = Column(ForeignKey('country.id'), nullable=False, index=True)
    best_championship_position = Column(Integer)
    best_starting_grid_position = Column(Integer)
    best_race_result = Column(Integer)
    total_championship_wins = Column(Integer, nullable=False)
    total_race_entries = Column(Integer, nullable=False)
    total_race_starts = Column(Integer, nullable=False)
    total_race_wins = Column(Integer, nullable=False)
    total_1_and_2_finishes = Column(Integer, nullable=False)
    total_race_laps = Column(Integer, nullable=False)
    total_podiums = Column(Integer, nullable=False)
    total_podium_races = Column(Integer, nullable=False)
    total_championship_points = Column(DECIMAL(8, 2), nullable=False)
    total_pole_positions = Column(Integer, nullable=False)
    total_fastest_laps = Column(Integer, nullable=False)

    country = relationship('Country')


class Driver(Base):
    __tablename__ = 'driver'

    id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    first_name = Column(String(100), nullable=False, index=True)
    last_name = Column(String(100), nullable=False, index=True)
    full_name = Column(String(100), nullable=False, index=True)
    abbreviation = Column(String(3), nullable=False, index=True)
    permanent_number = Column(String(2), index=True)
    gender = Column(String(6), nullable=False, index=True)
    date_of_birth = Column(Date, nullable=False, index=True)
    date_of_death = Column(Date, index=True)
    place_of_birth = Column(String(100), nullable=False, index=True)
    country_of_birth_country_id = Column(ForeignKey('country.id'), nullable=False, index=True)
    nationality_country_id = Column(ForeignKey('country.id'), nullable=False, index=True)
    second_nationality_country_id = Column(ForeignKey('country.id'), index=True)
    best_championship_position = Column(Integer)
    best_starting_grid_position = Column(Integer)
    best_race_result = Column(Integer)
    total_championship_wins = Column(Integer, nullable=False)
    total_race_entries = Column(Integer, nullable=False)
    total_race_starts = Column(Integer, nullable=False)
    total_race_wins = Column(Integer, nullable=False)
    total_race_laps = Column(Integer, nullable=False)
    total_podiums = Column(Integer, nullable=False)
    total_points = Column(DECIMAL(8, 2), nullable=False)
    total_championship_points = Column(DECIMAL(8, 2), nullable=False)
    total_pole_positions = Column(Integer, nullable=False)
    total_fastest_laps = Column(Integer, nullable=False)
    total_driver_of_the_day = Column(Integer, nullable=False)
    total_grand_slams = Column(Integer, nullable=False)

    country_of_birth_country = relationship('Country', primaryjoin='Driver.country_of_birth_country_id == Country.id')
    nationality_country = relationship('Country', primaryjoin='Driver.nationality_country_id == Country.id')
    second_nationality_country = relationship('Country', primaryjoin='Driver.second_nationality_country_id == Country.id')


class EngineManufacturer(Base):
    __tablename__ = 'engine_manufacturer'

    id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    country_id = Column(ForeignKey('country.id'), nullable=False, index=True)
    best_championship_position = Column(Integer)
    best_starting_grid_position = Column(Integer)
    best_race_result = Column(Integer)
    total_championship_wins = Column(Integer, nullable=False)
    total_race_entries = Column(Integer, nullable=False)
    total_race_starts = Column(Integer, nullable=False)
    total_race_wins = Column(Integer, nullable=False)
    total_race_laps = Column(Integer, nullable=False)
    total_podiums = Column(Integer, nullable=False)
    total_podium_races = Column(Integer, nullable=False)
    total_championship_points = Column(DECIMAL(8, 2), nullable=False)
    total_pole_positions = Column(Integer, nullable=False)
    total_fastest_laps = Column(Integer, nullable=False)

    country = relationship('Country')


class GrandPrix(Base):
    __tablename__ = 'grand_prix'

    id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    full_name = Column(String(100), nullable=False, index=True)
    short_name = Column(String(100), nullable=False, index=True)
    abbreviation = Column(String(3), nullable=False, index=True)
    country_id = Column(ForeignKey('country.id'), index=True)
    total_races_held = Column(Integer, nullable=False)

    country = relationship('Country')


class SeasonEntrant(Base):
    __tablename__ = 'season_entrant'

    year = Column(ForeignKey('season.year'), primary_key=True, nullable=False, index=True)
    entrant_id = Column(ForeignKey('entrant.id'), primary_key=True, nullable=False, index=True)
    country_id = Column(ForeignKey('country.id'), nullable=False, index=True)

    country = relationship('Country')
    entrant = relationship('Entrant')
    season = relationship('Season')


class TyreManufacturer(Base):
    __tablename__ = 'tyre_manufacturer'

    id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    country_id = Column(ForeignKey('country.id'), nullable=False, index=True)
    best_starting_grid_position = Column(Integer)
    best_race_result = Column(Integer)
    total_race_entries = Column(Integer, nullable=False)
    total_race_starts = Column(Integer, nullable=False)
    total_race_wins = Column(Integer, nullable=False)
    total_race_laps = Column(Integer, nullable=False)
    total_podiums = Column(Integer, nullable=False)
    total_podium_races = Column(Integer, nullable=False)
    total_pole_positions = Column(Integer, nullable=False)
    total_fastest_laps = Column(Integer, nullable=False)

    country = relationship('Country')


class ConstructorPreviousNextConstructor(Base):
    __tablename__ = 'constructor_previous_next_constructor'

    constructor_id = Column(ForeignKey('constructor.id'), primary_key=True, nullable=False, index=True)
    previous_next_constructor_id = Column(ForeignKey('constructor.id'), primary_key=True, nullable=False, index=True)
    year_from = Column(Integer, primary_key=True, nullable=False)
    year_to = Column(Integer)

    constructor = relationship('Constructor', primaryjoin='ConstructorPreviousNextConstructor.constructor_id == Constructor.id')
    previous_next_constructor = relationship('Constructor', primaryjoin='ConstructorPreviousNextConstructor.previous_next_constructor_id == Constructor.id')


class DriverFamilyRelationship(Base):
    __tablename__ = 'driver_family_relationship'

    driver_id = Column(ForeignKey('driver.id'), primary_key=True, nullable=False, index=True)
    other_driver_id = Column(ForeignKey('driver.id'), primary_key=True, nullable=False, index=True)
    type = Column(String(50), primary_key=True, nullable=False)

    driver = relationship('Driver', primaryjoin='DriverFamilyRelationship.driver_id == Driver.id')
    other_driver = relationship('Driver', primaryjoin='DriverFamilyRelationship.other_driver_id == Driver.id')


class Race(Base):
    __tablename__ = 'race'
    __table_args__ = (
        Index('year', 'year', 'round', unique=True),
    )

    id = Column(Integer, primary_key=True)
    year = Column(ForeignKey('season.year'), nullable=False, index=True)
    round = Column(Integer, nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    time = Column(Text)
    grand_prix_id = Column(ForeignKey('grand_prix.id'), nullable=False, index=True)
    official_name = Column(String(100), nullable=False, index=True)
    qualifying_format = Column(String(20), nullable=False)
    sprint_qualifying_format = Column(String(20))
    circuit_id = Column(ForeignKey('circuit.id'), nullable=False, index=True)
    circuit_type = Column(String(6), nullable=False)
    course_length = Column(DECIMAL(6, 3), nullable=False)
    laps = Column(Integer, nullable=False)
    distance = Column(DECIMAL(6, 3), nullable=False)
    scheduled_laps = Column(Integer)
    scheduled_distance = Column(DECIMAL(6, 3))
    pre_qualifying_date = Column(Date)
    pre_qualifying_time = Column(String(5))
    free_practice_1_date = Column(Date)
    free_practice_1_time = Column(String(5))
    free_practice_2_date = Column(Date)
    free_practice_2_time = Column(String(5))
    free_practice_3_date = Column(Date)
    free_practice_3_time = Column(String(5))
    free_practice_4_date = Column(Date)
    free_practice_4_time = Column(String(5))
    qualifying_1_date = Column(Date)
    qualifying_1_time = Column(String(5))
    qualifying_2_date = Column(Date)
    qualifying_2_time = Column(String(5))
    qualifying_date = Column(Date)
    qualifying_time = Column(String(5))
    sprint_qualifying_date = Column(Date)
    sprint_qualifying_time = Column(String(5))
    sprint_race_date = Column(Date)
    sprint_race_time = Column(String(5))
    warming_up_date = Column(Date)
    warming_up_time = Column(String(5))

    circuit = relationship('Circuit')
    grand_prix = relationship('GrandPrix')
    season = relationship('Season')


class SeasonConstructorStanding(Base):
    __tablename__ = 'season_constructor_standing'

    year = Column(ForeignKey('season.year'), primary_key=True, nullable=False, index=True)
    position_display_order = Column(Integer, primary_key=True, nullable=False, index=True)
    position_number = Column(Integer, index=True)
    position_text = Column(String(4), nullable=False, index=True)
    constructor_id = Column(ForeignKey('constructor.id'), nullable=False, index=True)
    engine_manufacturer_id = Column(ForeignKey('engine_manufacturer.id'), nullable=False, index=True)
    points = Column(DECIMAL(8, 2), nullable=False)

    constructor = relationship('Constructor')
    engine_manufacturer = relationship('EngineManufacturer')
    season = relationship('Season')


class SeasonDriverStanding(Base):
    __tablename__ = 'season_driver_standing'

    year = Column(ForeignKey('season.year'), primary_key=True, nullable=False, index=True)
    position_display_order = Column(Integer, primary_key=True, nullable=False, index=True)
    position_number = Column(Integer, index=True)
    position_text = Column(String(4), nullable=False, index=True)
    driver_id = Column(ForeignKey('driver.id'), nullable=False, index=True)
    points = Column(DECIMAL(8, 2), nullable=False)

    driver = relationship('Driver')
    season = relationship('Season')


class SeasonEntrantConstructor(Base):
    __tablename__ = 'season_entrant_constructor'

    year = Column(ForeignKey('season.year'), primary_key=True, nullable=False, index=True)
    entrant_id = Column(ForeignKey('entrant.id'), primary_key=True, nullable=False, index=True)
    constructor_id = Column(ForeignKey('constructor.id'), primary_key=True, nullable=False, index=True)
    engine_manufacturer_id = Column(ForeignKey('engine_manufacturer.id'), primary_key=True, nullable=False, index=True)

    constructor = relationship('Constructor')
    engine_manufacturer = relationship('EngineManufacturer')
    entrant = relationship('Entrant')
    season = relationship('Season')


class SeasonEntrantDriver(Base):
    __tablename__ = 'season_entrant_driver'

    year = Column(ForeignKey('season.year'), primary_key=True, nullable=False, index=True)
    entrant_id = Column(ForeignKey('entrant.id'), primary_key=True, nullable=False, index=True)
    constructor_id = Column(ForeignKey('constructor.id'), primary_key=True, nullable=False, index=True)
    engine_manufacturer_id = Column(ForeignKey('engine_manufacturer.id'), primary_key=True, nullable=False, index=True)
    driver_id = Column(ForeignKey('driver.id'), primary_key=True, nullable=False, index=True)
    rounds = Column(String(100))
    rounds_text = Column(String(100))
    test_driver = Column(TINYINT(1), nullable=False)

    constructor = relationship('Constructor')
    driver = relationship('Driver')
    engine_manufacturer = relationship('EngineManufacturer')
    entrant = relationship('Entrant')
    season = relationship('Season')


class SeasonEntrantTyreManufacturer(Base):
    __tablename__ = 'season_entrant_tyre_manufacturer'

    year = Column(ForeignKey('season.year'), primary_key=True, nullable=False, index=True)
    entrant_id = Column(ForeignKey('entrant.id'), primary_key=True, nullable=False, index=True)
    constructor_id = Column(ForeignKey('constructor.id'), primary_key=True, nullable=False, index=True)
    engine_manufacturer_id = Column(ForeignKey('engine_manufacturer.id'), primary_key=True, nullable=False, index=True)
    tyre_manufacturer_id = Column(ForeignKey('tyre_manufacturer.id'), primary_key=True, nullable=False, index=True)

    constructor = relationship('Constructor')
    engine_manufacturer = relationship('EngineManufacturer')
    entrant = relationship('Entrant')
    tyre_manufacturer = relationship('TyreManufacturer')
    season = relationship('Season')


class RaceConstructorStanding(Base):
    __tablename__ = 'race_constructor_standing'

    race_id = Column(ForeignKey('race.id'), primary_key=True, nullable=False, index=True)
    position_display_order = Column(Integer, primary_key=True, nullable=False, index=True)
    position_number = Column(Integer, index=True)
    position_text = Column(String(4), nullable=False, index=True)
    constructor_id = Column(ForeignKey('constructor.id'), nullable=False, index=True)
    engine_manufacturer_id = Column(ForeignKey('engine_manufacturer.id'), nullable=False, index=True)
    points = Column(DECIMAL(8, 2), nullable=False)
    positions_gained = Column(Integer)

    constructor = relationship('Constructor')
    engine_manufacturer = relationship('EngineManufacturer')
    race = relationship('Race')


class RaceDatum(Base):
    __tablename__ = 'race_data'

    race_id = Column(ForeignKey('race.id'), primary_key=True, nullable=False, index=True)
    type = Column(String(50), primary_key=True, nullable=False, index=True)
    position_display_order = Column(Integer, primary_key=True, nullable=False)
    position_number = Column(Integer, index=True)
    position_text = Column(String(4), nullable=False, index=True)
    driver_number = Column(String(3), nullable=False, index=True)
    driver_id = Column(ForeignKey('driver.id'), nullable=False, index=True)
    constructor_id = Column(ForeignKey('constructor.id'), nullable=False, index=True)
    engine_manufacturer_id = Column(ForeignKey('engine_manufacturer.id'), nullable=False, index=True)
    tyre_manufacturer_id = Column(ForeignKey('tyre_manufacturer.id'), nullable=False, index=True)
    practice_time = Column(String(20))
    practice_time_millis = Column(Integer)
    practice_gap = Column(String(20))
    practice_gap_millis = Column(Integer)
    practice_interval = Column(String(20))
    practice_interval_millis = Column(Integer)
    practice_laps = Column(Integer)
    qualifying_time = Column(String(20))
    qualifying_time_millis = Column(Integer)
    qualifying_q1 = Column(String(20))
    qualifying_q1_millis = Column(Integer)
    qualifying_q2 = Column(String(20))
    qualifying_q2_millis = Column(Integer)
    qualifying_q3 = Column(String(20))
    qualifying_q3_millis = Column(Integer)
    qualifying_gap = Column(String(20))
    qualifying_gap_millis = Column(Integer)
    qualifying_interval = Column(String(20))
    qualifying_interval_millis = Column(Integer)
    qualifying_laps = Column(Integer)
    starting_grid_position_grid_penalty = Column(String(20))
    starting_grid_position_grid_penalty_positions = Column(Integer)
    starting_grid_position_time = Column(String(20))
    starting_grid_position_time_millis = Column(Integer)
    race_shared_car = Column(TINYINT(1))
    race_laps = Column(Integer)
    race_time = Column(String(20))
    race_time_millis = Column(Integer)
    race_time_penalty = Column(String(20))
    race_time_penalty_millis = Column(Integer)
    race_gap = Column(String(20))
    race_gap_millis = Column(Integer)
    race_gap_laps = Column(Integer)
    race_interval = Column(String(20))
    race_interval_millis = Column(Integer)
    race_reason_retired = Column(String(100))
    race_points = Column(DECIMAL(8, 2))
    race_grid_position_number = Column(Integer)
    race_grid_position_text = Column(String(2))
    race_positions_gained = Column(Integer)
    race_pit_stops = Column(Integer)
    race_fastest_lap = Column(TINYINT(1))
    race_driver_of_the_day = Column(TINYINT(1))
    race_grand_slam = Column(TINYINT(1))
    fastest_lap_lap = Column(Integer)
    fastest_lap_time = Column(String(20))
    fastest_lap_time_millis = Column(Integer)
    fastest_lap_gap = Column(String(20))
    fastest_lap_gap_millis = Column(Integer)
    fastest_lap_interval = Column(String(20))
    fastest_lap_interval_millis = Column(Integer)
    pit_stop_stop = Column(Integer)
    pit_stop_lap = Column(Integer)
    pit_stop_time = Column(String(20))
    pit_stop_time_millis = Column(Integer)
    driver_of_the_day_percentage = Column(DECIMAL(4, 1))

    constructor = relationship('Constructor')
    driver = relationship('Driver')
    engine_manufacturer = relationship('EngineManufacturer')
    race = relationship('Race')
    tyre_manufacturer = relationship('TyreManufacturer')


class RaceDriverStanding(Base):
    __tablename__ = 'race_driver_standing'

    race_id = Column(ForeignKey('race.id'), primary_key=True, nullable=False, index=True)
    position_display_order = Column(Integer, primary_key=True, nullable=False, index=True)
    position_number = Column(Integer, index=True)
    position_text = Column(String(4), nullable=False, index=True)
    driver_id = Column(ForeignKey('driver.id'), nullable=False, index=True)
    points = Column(DECIMAL(8, 2), nullable=False)
    positions_gained = Column(Integer)

    driver = relationship('Driver')
    race = relationship('Race')
