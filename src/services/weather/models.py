from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, text, Numeric, String

from src.database import Base


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    weather_datetime = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    temp = Column(Numeric(precision=6, scale=3, asdecimal=False), comment='Units: Celsius')
    temp_min = Column(Numeric(precision=6, scale=3, asdecimal=False), comment='Units: Celsius')
    temp_max = Column(Numeric(precision=6, scale=3, asdecimal=False), comment='Units: Celsius')
    pressure = Column(Integer, comment='Units: hPa')
    humidity = Column(Integer, comment='Units: %')
    visibility = Column(Integer, comment='Units: meter')
    wind_speed = Column(Numeric(precision=4, scale=2, asdecimal=False), comment='Units: meter/sec')
    rain = Column(String(25), comment='Units: mm')
    snow = Column(String(25), comment='Units: mm')
    clouds = Column(Integer, comment='Units: %')

