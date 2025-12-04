import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
from game import choix_equipe, start_game
from models import Character
from utils import get_choice, show_scores

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"]  # Sélection ou création de la base test_db
caracters = db["caracters"]
monstres = db["monsters"]

def print_menu():
    print("\n---Menu Principal--- \n")
    print("1: Lancer le jeu")
    print("2: Afficher le classement")
    print("3: Quitter")


def show_main_menu():
    while True :
        print_menu()
        choix = get_choice("\nVotre choix : ", [1,2,3])
        if choix == 1 :
            name_user = input("Nom de l'utilisateur : ")
            start_game(name_user, choix_equipe())
        elif choix == 2:
            show_scores(db)
        elif choix == 3:
            print("Fermeture du jeu...")
            sys.exit(0)

if __name__ == "__main__":
    show_main_menu()
