class StationService:

    def __init__(self):
        self.stations = self._load_data()

    def _load_data(self) -> dict:
        # data에서 역 데이터 불러오기
        return {}

    def _get_all(self):
        return self.stations

    def get_ids(self) -> dict:
        return { "ids": [] }

    def get_names(self) -> dict:
        return { "names": [] }

    def get(self, station):
        if station.isdigit():
            return self._get_by_id(int(station))

        return self._get_by_name(station)

    def _get_by_id(self, station_id):
        ...

    def _get_by_name(self, name):
        ...

    def get_facilities(self, station):
        ...

    def get_elevators(self, station):
        ...

    def get_toilets(self, station):
        ...