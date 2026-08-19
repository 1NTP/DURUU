from flask import Blueprint
from services.station_service import StationService

station_service = StationService()
stations_api = Blueprint("stations", __name__)

@stations_api.get("/stations/<station>")
def get_station(station):
    station_data = station_service.get(station)
    if station_data:
        return station_data.to_dict()
    return {"error": "Not Found"}, 404

@stations_api.get("/stations/ids")
def get_station_ids():
    return station_service.get_ids()

@stations_api.get("/stations/names")
def get_station_names():
    return station_service.get_names()