import random
import time
from models import Character, Monster
from pymongo import MongoClient
from utils import get_choice, monstre_hasard, save_score

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"]  # Sélection ou création de la base test_db

#def get_perso

def liste_personnage(perso=None):
    if perso is None :
        persos = list(db.caracters.find())           
    print("\nTous les personnages utilisables :\n")
    for i, p in enumerate(persos):
        print(f"{i + 1}. {p['name']} - ATK: {p['ATK']} | DEF: {p['DEF']} | PV: {p['PV']}")
    return persos

def choix_equipe():
    print("\nFait le choix de ton équipe (3 personnages)")
    persos = liste_personnage()
    equipe = []
    for i in range(3):
        print("\nPersonnages encore disponibles :")
        choix = get_choice("Entrer le numéro du personnage : ",list(range(1, len(persos) + 1)))
        perso = persos.pop(choix - 1)
        equipe.append(perso)
        print(f"{perso['name']} a été ajouter à votre équipe !")

    return [Character.from_dict(p) for p in equipe]


def is_caracter_alive(team):
    alive_heroes = [h for h in team if h.hp > 0]

    if not alive_heroes:
        print("Tous les héros sont ko...")
    return alive_heroes

def is_monstre_alive(monster):
    if monster.hp <= 0:
        print("Le monstre est Ko !")
        return False
    return True

def attaque(attacker, attacked):
    damage = max(0, attacker.atk - attacked.defense)
    attacked.hp -= damage
    print(f"{attacker.name} inflige {damage} dégâts → {attacked.name} ({attacked.hp} PV)")
    time.sleep(0.5)

def print_start_fight(monster):
    print("\n=== COMBAT ===")
    print(f"Vous affrontez : {monster.name} (ATK {monster.atk} | DEF {monster.defense} | PV {monster.hp})")

def fight(team, monster):
    print_start_fight(monster)
    while True:
        for hero in team:
            if hero.hp <= 0:
                continue

            attaque(hero, monster)

            if not is_monstre_alive(monster):
                return True 

        alive = is_caracter_alive(team)
        if not alive:   
            return False 

        hero_targeted = random.choice(alive)

        attaque(monster, hero_targeted)


def print_wave(wave):
        print( "=======================")
        print(f"       Vague {wave + 1} ")
        print( "=======================")

def print_game_end(waves):
    print("Fin de la partie")
    print(f"Score final : {waves} vagues")

def start_game(player_name, team):
    waves = 0
    print("\n=== Début de la partie ===")
    while True:
        print_wave(waves)
    
        monster = monstre_hasard(db)

        is_team_victorious = fight(team, monster)

        if not is_team_victorious:
            break 

        waves += 1
        print(f"Vagues complétées : {waves}")

    print_game_end(waves)
    save_score(db, player_name, waves)

    return waves