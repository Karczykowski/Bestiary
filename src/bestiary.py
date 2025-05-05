import json

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
            if any(a.lower() == ability.lower() for a in monster.abilities)
        ]

    def get_monsters_by_region(self, region):
        return [monster for monster in self.monsters.values() if region.name.lower() in monster.region.name.lower()]
