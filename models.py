class Character:
    def __init__(self, name, atk, defense, hp):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.hp = hp

    @staticmethod
    def from_dict(d):
        return Character(d["name"], d["atk"], d["defense"], d["hp"])


class Monster:
    def __init__(self, name, atk, defense, hp):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.hp = hp

    @staticmethod
    def from_dict(d):
        return Monster(d["name"], d["atk"], d["defense"], d["hp"])
