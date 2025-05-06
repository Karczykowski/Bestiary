import json
import os

class Bestiary:

    def __init__(self, name):
        self.name = name
        self.monsters = {}

    def add_monster(self, monster):
        if monster.name in self.monsters:
            raise ValueError(f"{monster.name} already exists in this bestiary")

        self.monsters[monster.name] = monster
        return True

    def remove_monster(self, name):
        if name not in self.monsters:
            raise ValueError(f"Monster {name} not found in the bestiary")

        return self.monsters.pop(name)

    def get_monster_by_name(self, name):
        return self.monsters.get(name)

    def get_monsters_by_ability(self, ability):
        return [
            monster for monster in self.monsters.values()
            if any(a.name == ability for a in monster.abilities)
        ]

    def get_monsters_by_region(self, region):
        return [monster for monster in self.monsters.values() if region in monster.region.name]

    def save_to_file(self, filename):
        data = {
            "name": self.name,
            "monsters": {name: json.loads(monster.to_json()) for name, monster in self.monsters.items()}
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return True

    @classmethod
    def load_from_file(cls, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")

        with open (filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        from monster import Monster, MonsterType
        from region import Region

        bestiary = cls(data["name"])

        for name, monster_data in data["monsters"].items():

            monster_data["monster_type"] = MonsterType[monster_data["monster_type"]]

            monster = Monster(
                monster_data["name"],
                monster_data["hit_points"],
                monster_data["region"],
                monster_data["monster_type"],
                monster_data["abilities"]
            )
            bestiary.monsters[name] = monster

        return bestiary
