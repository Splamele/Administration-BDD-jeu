import random
from models import Character, Monster
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"]  # Sélection ou création de la base test_db
caraters = db["caracters"]
monstres = db["monsters"]


def monstre_hasard ():
    monstre_selectioner = random.choice(list(monstres.find()))
    #return Monster.from_dict(monstre_selectioner)
    return Monster.from_dict(monstre_selectioner)

print(monstre_hasard())