import unittest
import json
from src.ability import Ability

class TestAbility(unittest.TestCase):
    def setUp(self):
        self.valid_ability = Ability(
            name = "Fireball",
            damage = 30
        )

    def test_ability_initialization(self):
        self.assertEqual(self.valid_ability.name, "Fireball")
        self.assertEqual(self.valid_ability.damage, 30)

    def test_to_json(self):
        json_str = self.valid_ability.to_json()
        data = json.loads(json_str)

        self.assertEqual(data["name"], "Fireball")
        self.assertEqual(data["damage"], 30)

    def test_from_json(self):
        json_str = self.valid_ability.to_json()
        new_ability = Ability.from_json(json_str)

        self.assertEqual(new_ability.name, "Fireball")
        self.assertEqual(new_ability.damage, 30)