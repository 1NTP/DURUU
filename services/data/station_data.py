from dataclasses import dataclass, field, asdict


@dataclass
class StationData:
    id: str = "none"
    name: str = "none"
    
    def to_dict(self) -> dict:
        return asdict(self)
    
    def load_from_dict(self, data: dict):
        self.id = data.get("id", "none")
        self.name = data.get("name", "none")