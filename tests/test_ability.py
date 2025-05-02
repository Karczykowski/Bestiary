import unittest
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