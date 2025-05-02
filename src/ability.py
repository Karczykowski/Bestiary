import json

class Ability:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def to_dict(self):
        return {
            "name": self.name,
            "damage": self.damage
        }

    def to_json(self):

        data = {
            "name": self.name,
            "damage": self.damage,
        }

        return json.dumps(data, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_str):

        data = json.loads(json_str)

        ability = cls(
            data["name"],
            data["damage"],
        )

        return ability