import unittest
from src.monster import Monster, MonsterType
from src.region import Region
from src.ability import Ability

class TestMonster(unittest.TestCase):
    def setUp(self):
        self.ability1 = Ability(
            name = "Fireball",
            damage = 30
        )

        self.ability2 = Ability(
            name = "Bite",
            damage = 5
        )

        self.ability3 = Ability(
            name = "Wing Flap",
            damage = 15
        )

        self.region1 = Region(
            name = "Swamp"
        )

        self.region2 = Region(
            name = "Cave"
        )

        self.monster1 = Monster(
            name = "Zombie",
            hit_points = 20,
            region = self.region2,
            monster_type = MonsterType.HUMANOID,
            abilities = [self.ability2]
        )
        
        self.monster2 = Monster(
            name = "Black Dragon",
            hit_points = 200,
            region = self.region1,
            monster_type = MonsterType.DRAGON,
            abilities = [self.ability2, self.ability3]
        )