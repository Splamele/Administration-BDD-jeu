import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
from game import start_game
from models import Character

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"]  # Sélection ou création de la base test_db
caracters = db["caracters"]
monstres = db["monsters"]
scores = db["scores"]

def print_menu():
    print("1: Lancer le jeu")
    print("2: Afficher le classement")
    print("3: quitter")

def get_choice():
    choix = input("Votre choix : ")
    if choix in ['1','2','3']:
        return choix
    else:
         print("Mauvaise valeur, c'est 1, 2 ou 3. \n")

def show_main_menu():
    while True :
        print_menu()
        choix = get_choice()
        if choix == "1" :
            name_user = input("Nom de l'utilisateur : ")
            start_game(name_user, choix_equipe())
        elif choix == "2":
            show_scores()
        elif choix == "3":
            print("Fermeture du jeu...")
            sys.exit(0)
        else : 
            break

def liste_personnage():
    persos = list(caracters.find())           
    print("Tous les personnages utilisables ")
    for i, p in enumerate(persos):
        print(f"{i + 1}. {p['name']} - ATK: {p['atk']} | DEF: {p['defense']} | HP: {p['hp']}")
    return persos

def choix_equipe():
    print("Fait le choix de ton équipe (3 personnages)")
    persos = liste_personnage()
    equipe = []
    while len(equipe) < 3:
        try : 
            choix = int(input("Entrer le numéro du personnage :"))
            if choix < 1 or choix > len(persos):
                print("Numérot invalide")
                continue
            perso = persos[choix - 1]
            if perso in equipe:
                print("Ce personnage est déjà dans votre équipe.")
                continue

            equipe.append(perso)
            print(f"{perso['name']} a été ajouter à votre équipe !")

        except ValueError:
            print("Veuillez entrer un nombre valide.")
                        
    team_objs = [Character.from_dict(p) for p in equipe]
    return team_objs

def show_scores():
    best_scores = scores.find().sort("waves", -1).limit(3)
    for i, s in enumerate(best_scores, start=1):
        print(f"{i}. {s['player']} - {s['waves']} vagues")

if __name__ == "__main__":
    show_main_menu()
