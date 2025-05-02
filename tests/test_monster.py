import unittest
import json
from src.monster import Monster, MonsterType
from src.region import Region
from src.ability import Ability

class TestMonster(unittest.TestCase):
    def setUp(self):
        self.valid_ability1 = Ability(
            name = "Fireball",
            damage = 30
        )

        self.valid_ability2 = Ability(
            name = "Bite",
            damage = 5
        )

        self.valid_region = Region(
            name = "Swamp"
        )

        self.valid_monster = Monster(
            name = "Green Hag",
            hit_points = 40,
            region = self.valid_region,
            monster_type = MonsterType.HUMANOID,
            abilities = [self.valid_ability1, self.valid_ability2]
        )


    def test_monster_initialization(self):
        self.assertEqual(self.valid_monster.name, "Green Hag")
        self.assertEqual(self.valid_monster.hit_points, 40)
        self.assertEqual(self.valid_monster.region, self.valid_region)
        self.assertEqual(self.valid_monster.monster_type, MonsterType.HUMANOID)
        self.assertEqual(self.valid_monster.abilities, [self.valid_ability1, self.valid_ability2])

    def test_to_json(self):
        json_str = self.valid_monster.to_json()
        data = json.loads(json_str)

        self.assertEqual(data["name"], "Green Hag")
        self.assertEqual(data["hit_points"], 40)
        self.assertEqual(data["region"], self.valid_region.to_dict())
        self.assertEqual(data["monster_type"], MonsterType.HUMANOID.name)
        self.assertEqual(data["abilities"], [self.valid_ability1.to_dict(), self.valid_ability2.to_dict()])

    def test_from_json(self):
        json_str = self.valid_monster.to_json()
        new_monster = Monster.from_json(json_str)

        self.assertEqual(new_monster.name, "Green Hag")
        self.assertEqual(new_monster.hit_points, 40)
        self.assertEqual(new_monster.region, self.valid_region.to_dict())
        self.assertEqual(new_monster.monster_type, MonsterType.HUMANOID)
        self.assertEqual(new_monster.abilities, [self.valid_ability1.to_dict(), self.valid_ability2.to_dict()])