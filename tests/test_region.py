import unittest
from src.region import Region

class TestRegion(unittest.TestCase):
    def setUp(self):
        self.valid_region = Region(
            name = "Swamp",
        )