from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"] 
personnages = db["caracters"]
monstres = db["monsters"]

PERSONNAGES_LISTE = [
    {"name": "Lycaon", "ATK" : 17, "DEF" : 20, "PV": 140},

    {"name" : "Ellen", "ATK": 29, "DEF": 15, "PV": 110},

    {"name" : "Miyabi", "ATK": 35, "DEF": 7, "PV": 80},

    {"name" : "Scaramouche", "ATK": 23, "DEF": 8, "PV": 100},

    {"name" : "Durin", "ATK": 18, "DEF": 6, "PV": 60},

    {"name": "Fishl", "ATK": 20, "DEF": 18, "PV": 90},

    {"name" : "Kafka", "ATK": 27, "DEF": 16, "PV": 120},

    {"name" : "La Grande Herta", "ATK": 31, "DEF": 14, "PV": 110},

    {"name" : "Saber", "ATK": 34, "DEF": 16, "PV": 120},

    {"name" : "Miku", "ATK": 20, "DEF": 13, "PV": 100}
    ]

MONSTRES_LISTE = [
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


ajouter_plusieurs(PERSONNAGES_LISTE, personnages)
ajouter_plusieurs(MONSTRES_LISTE, monstres)