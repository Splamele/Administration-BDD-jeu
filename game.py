import random
from models import Character, Monster
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"]  # Sélection ou création de la base test_db

def monstre_hasard ():
    monstre_selectioner = random.choice(list(db.monsters.find()))
    return Monster.from_dict(monstre_selectioner)

#print(monstre_hasard())

def save_score(player_name, waves):
    db.scores.insert_one({
        "player": player_name,
        "waves": waves
    })


# Fonction d'un combat contre un monstre
def fight(team, monster):
    print("\n=== COMBAT ===")
    print(f"Vous affrontez : {monster.name} (ATK {monster.atk} | DEF {monster.defense} | PV {monster.hp})")

    # Boucle du combat
    while True:
        # ----- PHASE : Les héros attaquent -----
        for hero in team:
            if hero.hp <= 0:
                continue

            damage = max(0, hero.atk - monster.defense)
            monster.hp -= damage
            print(f"{hero.name} inflige {damage} dégâts → {monster.name} ({monster.hp} PV)")

            if monster.hp <= 0:
                print("Le monstre est Ko !")
                return True

        # ----- PHASE : Le monstre attaque -----
        alive_heroes = [h for h in team if h.hp > 0]

        if not alive_heroes:
            print("Tous les héros sont ko...")
            return False

        target = random.choice(alive_heroes)
        monster_damage = max(0, monster.atk - target.defense)
        target.hp -= monster_damage

        print(f"{monster.name} attaque {target.name} et inflige {monster_damage} dégâts → {target.hp} PV")

        # Check si le héros meurt
        if all(h.hp <= 0 for h in team):
            print("Tous les personnages de l'équipe sont ko...")
            return False


def start_game(player_name, team):
    waves = 0

    print("\n=== Début de la partie ===")
    print(f"Bonne chance {player_name} !")

    while True:
        monster = monstre_hasard()
        print( "=======================")
        print(f"\n--- Vague {waves + 1} ---")
        print( "=======================")

        victory = fight(team, monster)

        if not victory:
            break 

        waves += 1
        print(f"Vagues complétées : {waves}")

    print("\n=== Fin de la partie ===")
    print(f"Score final : {waves} vagues")

    # Sauvegarde score
    save_score(player_name, waves)

    return waves