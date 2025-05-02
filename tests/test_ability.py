import unittest
from src.ability import Ability

class TestAbility(unittest.TestCase):
    def setUp(self):
        self.valid_ability = Ability(
            name = "Fireball",
            damage = "30"
        )