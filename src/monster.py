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
