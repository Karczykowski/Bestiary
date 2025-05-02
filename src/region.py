import json

class Region:

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            "name": self.name
        }

    def to_json(self):

        data = {
            "name": self.name,
        }

        return json.dumps(data, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_str):

        data = json.loads(json_str)

        region= cls(
            data["name"],
        )

        return region