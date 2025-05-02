import unittest
from src.region import Region

class TestRegion(unittest.TestCase):
    def setUp(self):
        self.valid_region = Region(
            name = "Swamp",
        )

    def test_region_initialization(self):
        self.assertEqual(self.valid_region.name, "Swamp")