from services.data.station_data import StationData
from pathlib import Path
import yaml

class StationService:
    def __init__(self):
        self.path = Path(__file__).parent.parent / "data"
        self.stations: dict = self._load_data()
    
    def _get_files(self, extension: str) -> list[Path]:
        return list(Path(self.path).rglob(f"*.{extension}"))

    def _load_data(self) -> list:
        data = []

        for file in self._get_files("yml"):
            with file.open("r", encoding="utf-8") as f:
                loaded = yaml.safe_load(f) or {}
            if not loaded:
                print(f"[log] empty station data: {file}")

            if not isinstance(loaded, dict):
                print(f"[log] invalid station data format: {file}")
                continue
            
            station_data = StationData()
            station_data.load_from_dict(loaded)
                
            with file.open("w", encoding="utf-8") as f:
                yaml.safe_dump(
                    station_data.to_dict(),
                    f,
                    allow_unicode=True,
                    sort_keys=False
                )
                
            data.append(station_data)

        return data
    
    def _get_all(self):
        return self.stations

    def get_ids(self) -> dict:
        ids = []
        
        for station in self.stations:
            ids.append(station.id) 
        
        return { "ids": ids }

    def get_names(self) -> dict:
        names = []
        
        for station in self.stations:
            names.append(station.names) 
        
        return { "names": names }

    def get(self, station):
        if station.isdigit():
            return self._get_by_id(int(station))

        return self._get_by_name(station)

    def _get_by_id(self, station_id) -> StationData | None:
        for station in self.stations:
            if station_id == station.id:
                return station 
        
        return None

    def _get_by_name(self, name) -> StationData | None:
        for station in self.stations:
            if name == station.name:
                return station 
        
        return None

    def get_facilities(self, station):
        ...

    def get_elevators(self, station):
        ...

    def get_toilets(self, station):
        ...