from dataclasses import dataclass, field, asdict


@dataclass
class LocationData:
    description: str = "none"


@dataclass
class FacilityData:
    type: str = "none"
    name: str = "none"
    locations: list[LocationData] = field(default_factory=list)


@dataclass
class StationData:
    id: str = "none"
    name: str = "none"
    facilities: list[FacilityData] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)

    def load_from_dict(self, data: dict):
        self.id = data.get("id", "none")
        self.name = data.get("name", "none")

        self.facilities = []

        for facility_data in data.get("facilities", []):
            facility = FacilityData(
                type=facility_data.get("type", "none"),
                name=facility_data.get("name", "none")
            )

            for location_data in facility_data.get("locations", []):
                location = LocationData(
                    description=location_data.get("description", "none")
                )

                facility.locations.append(location)

            self.facilities.append(facility)