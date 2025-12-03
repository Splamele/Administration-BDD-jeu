import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
from game import start_game
from models import Character

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"]  # Sélection ou création de la base test_db
caraters = db["caracters"]
monstres = db["monsters"]
scores = db["scores"]

def show_main_menu():

    while True :

        print("1: Lancer le jeu")
        print("2: Afficher le classement")
        print("3: quitter")

        choix = input("Votre choix : ")

        if choix == "1" :
            name_user = input("Nom de l'utilisateur : ")
            print("Fait le choix de ton équipe (3 personnages)")
            team_objs = [Character.from_dict(p) for p in team]

            waves = start_game(name_user, team_objs)
        
        elif choix == "2":
            print("classement : ")
        
        elif choix == "3":
            print("Fermeture du jeu...")
            sys.exit(0)
        
        else : 
            print("Mauvaise valeur, c'est 1, 2 ou 3. \n")


if __name__ == "__main__":
    show_main_menu()
