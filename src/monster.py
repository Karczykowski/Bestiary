import json
from enum import Enum, auto

class MonsterType(Enum):
    DRAGON = auto()
    HUMANOID = auto()
    FLYING = auto()
    AQUATIC = auto()
    ALIEN = auto()
    OTHER = auto()

class Monster:

    def __init__(self, name, hit_points, region, monster_type = MonsterType.OTHER, abilities = None):
        self.name = name
        self.hit_points = hit_points
        self.region = region
        self.monster_type = monster_type

        if abilities is not None:
            self.abilities = abilities

    def to_json(self):

        data = {
            "name": self.name,
            "hit_points": self.hit_points,
            "region": self.region.to_dict(),
            "monster_type": self.monster_type.name,
            "abilities": [ability.to_dict() for ability in self.abilities]
        }

        return json.dumps(data, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_str):

        data = json.loads(json_str)
        monster_type = MonsterType[data["monster_type"]]

        monster = cls(
            data["name"],
            data["hit_points"],
            data["region"],
            monster_type,
            data["abilities"]

        )

        return monster