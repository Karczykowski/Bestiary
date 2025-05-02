import unittest
import json
from src.region import Region

class TestRegion(unittest.TestCase):
    def setUp(self):
        self.valid_region = Region(
            name = "Swamp",
        )

    def test_region_initialization(self):
        self.assertEqual(self.valid_region.name, "Swamp")

    def test_to_json(self):
        json_str = self.valid_region.to_json()
        data = json.loads(json_str)

        self.assertEqual(data["name"], "Swamp")

    def test_from_json(self):
        json_str = self.valid_region.to_json()
        new_region = Region.from_json(json_str)

        self.assertEqual(new_region.name, "Swamp")