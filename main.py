import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
from game import start_game
from models import Character
from utils import get_choice

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"]  # Sélection ou création de la base test_db
caracters = db["caracters"]
monstres = db["monsters"]
scores = db["scores"]

def print_menu():
    print("1: Lancer le jeu")
    print("2: Afficher le classement")
    print("3: quitter")

def liste_personnage():
    persos = list(caracters.find())           
    print("Tous les personnages utilisables ")
    for i, p in enumerate(persos):
        print(f"{i + 1}. {p['name']} - ATK: {p['ATK']} | DEF: {p['DEF']} | PV: {p['PV']}")
    return persos

def choix_equipe():
    print("Fait le choix de ton équipe (3 personnages)")
    persos = liste_personnage()
    equipe = []
    for i in range(3):
        choix = get_choice("Entrer le numéro du personnage : ",valid_choices=list(range(1, len(persos) + 1)))
        perso = persos.pop(choix - 1)
        equipe.append(perso)
        print(f"{perso['name']} a été ajouter à votre équipe !")

    return [Character.from_dict(p) for p in equipe]

def show_scores():
    best_scores = scores.find().sort("waves", -1).limit(3)
    for i, s in enumerate(best_scores, start=1):
        print(f"{i}. {s['player']} - {s['waves']} vagues")
        found = True
    if not found:
        print("Aucun score enregistré.")

def show_main_menu():
    while True :
        print_menu()
        choix = get_choice("Votre choix : ", [1,2,3])
        if choix == 1 :
            name_user = input("Nom de l'utilisateur : ")
            start_game(name_user, choix_equipe())
        elif choix == 2:
            show_scores()
        elif choix == 3:
            print("Fermeture du jeu...")
            sys.exit(0)

if __name__ == "__main__":
    show_main_menu()
