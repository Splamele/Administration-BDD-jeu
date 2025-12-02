from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"] 
personnages = db["caracters"]
monstres = db["monsters"]

personnages_liste = [
    {"name": "Guerrier", "ATK" : 15, "DEF" : 10, "PV": 100},

    {"name" : "Mage", "ATK": 20, "DEF": 5, "PV": 80},

    {"name" : "Archer", "ATK": 18, "DEF": 7, "PV": 90},

    {"name" : "Voleur", "ATK": 22, "DEF": 8, "PV": 85},

    {"name" : "Paladin", "ATK": 14, "DEF": 12, "PV": 110},

    {"name" : "Sorcier", "ATK": 25, "DEF": 3, "PV": 70},

    {"name": "Chevalier", "ATK": 17, "DEF": 15, "PV": 120},

    {"name" : "Moine", "ATK": 19, "DEF": 9, "PV": 95},

    {"name" : "Berserker", "ATK": 23, "DEF": 6, "PV": 105},

    {"name" : "Chasseur", "ATK": 16, "DEF": 11, "PV": 100}
    ]

monstres_liste = [
    {"name": "Gobelin", "ATK": 10, "DEF": 5, "PV": 50},

    {"name": "Orc", "ATK": 20, "DEF": 8, "PV": 120},

    {"name": "Dragon", "ATK": 35, "DEF": 20, "PV": 300},

    {"name": "Zombie", "ATK": 12, "DEF": 6, "PV": 70},

    {"name": "Troll", "ATK": 25, "DEF": 15, "PV": 200},

    {"name": "Spectre", "ATK": 18, "DEF": 10, "PV": 100},

    {"name": "Golem", "ATK": 30, "DEF": 25, "PV": 250},

    {"name": "Vampire", "ATK": 22, "DEF": 12, "PV": 150},

    {"name": "Loup-garou", "ATK": 28, "DEF": 18, "PV": 180},

    {"name": "Squelette", "ATK": 15, "DEF": 7,"PV": 90}
]

def ajouter_plusieurs (liste, db_choix):
    result = db_choix.insert_many(liste)
    print("Les données ont été correctement ajouter", result.inserted_ids)


ajouter_plusieurs(personnages_liste, personnages)
ajouter_plusieurs(monstres_liste, monstres)