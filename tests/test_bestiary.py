import os.path
import tempfile
import unittest
from src.bestiary import Bestiary
from src.monster import Monster, MonsterType
from src.ability import Ability
from src.region import Region

class TestBestiary(unittest.TestCase):

    def setUp(self):
        self.bestiary = Bestiary(
            name = "Monster Book"
        )

        self.region1 = Region(
            name = "Swamp"
        )

        self.region2 = Region(
            name = "Mountains"
        )

        self.ability1 = Ability(
            name = "Fire Breath",
            damage = 30
        )

        self.ability2 = Ability(
            name = "Bite",
            damage = 10
        )

        self.monster1 = Monster(
            name = "Red Dragon",
            hit_points = 120,
            region = self.region2,
            monster_type = MonsterType.DRAGON,
            abilities = [self.ability1, self.ability2]
        )

        self.monster2 = Monster(
            name = "Crocodile",
            hit_points = 15,
            region = self.region1,
            monster_type = MonsterType.AQUATIC,
            abilities = [self.ability2]
        )

        self.monster3 = Monster(
            name = "Bandit",
            hit_points = 10,
            region = self.region1,
            monster_type = MonsterType.HUMANOID
        )

    def test_bestiary_initialization(self):
        self.assertEqual(self.bestiary.name, "Monster Book")
        self.assertEqual(len(self.bestiary.monsters), 0)

    def test_add_monster(self):
        self.assertTrue(self.bestiary.add_monster(self.monster1))
        self.assertEqual(len(self.bestiary.monsters), 1)
        self.assertEqual(self.bestiary.monsters[self.monster1.name], self.monster1)

    def test_add_duplicate_monster_raises_error(self):
        self.bestiary.add_monster(self.monster1)

        with self.assertRaises(ValueError):
            self.bestiary.add_monster(self.monster1)

    def test_remove_book(self):
        self.bestiary.add_monster(self.monster1)
        removed_monster = self.bestiary.remove_monster(self.monster1.name)

        self.assertEqual(removed_monster, self.monster1)
        self.assertEqual(len(self.bestiary.monsters), 0)

    def test_remove_fake_monster_raises_error(self):
        with self.assertRaises(ValueError):
            self.bestiary.remove_monster("fake-monster-name")

    def test_get_monster_by_name(self):
        self.bestiary.add_monster(self.monster1)
        self.bestiary.add_monster(self.monster2)

        returned_monster = self.bestiary.get_monster_by_name(self.monster1.name)
        self.assertEqual(returned_monster, self.monster1)

        fake_monster = self.bestiary.get_monster_by_name("fake-monster-name")
        self.assertIsNone(fake_monster)


    def test_get_monsters_by_ability(self):
        self.bestiary.add_monster(self.monster1)
        self.bestiary.add_monster(self.monster2)

        monsters_with_bite = self.bestiary.get_monsters_by_ability("Bite")
        self.assertEqual(len(monsters_with_bite), 2)

        monster_with_fake_ability = self.bestiary.get_monsters_by_ability("fake-ability")
        self.assertEqual(len(monster_with_fake_ability), 0)



    def test_get_monsters_by_region(self):
        self.bestiary.add_monster(self.monster2)

        monster_from_swamp = self.bestiary.get_monsters_by_region("Swamp")
        self.assertEqual(len(monster_from_swamp), 1)

        monster_from_fake_region = self.bestiary.get_monsters_by_region("fake-region")
        self.assertEqual(len(monster_from_fake_region), 0)

    def test_save_and_load_from_file(self):
        self.bestiary.add_monster(self.monster1)
        self.bestiary.add_monster(self.monster2)

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name

        try:
            self.bestiary.save_to_file(temp_filename)

            import json
            with open(temp_filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.assertEqual(data["name"], "Monster Book")
            self.assertEqual(len(data["monsters"]), 2)

        finally:
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
