import random
from models import Character, Monster

def get_choice(prompt, valid_choices=None):
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        if valid_choices is not None and user_input not in valid_choices:
            print(f"Veuillez entrer une des valeurs suivantes : {valid_choices}")
            continue
        return user_input

def monstre_hasard (db):
    monstre_selectioner = random.choice(list(db.monsters.find()))
    return Monster.from_dict(monstre_selectioner)

def save_score(db, name_user, waves):
    db.scores.insert_one({
        "player": name_user,
        "waves": waves
    })

def show_scores(db):
    best_scores = db.scores.find().sort("waves", -1).limit(3)
    print("\nLe classement des 3 meilleurs runs :\n")
    for i, s in enumerate(best_scores, start=1):
        print(f"{i}. {s['player']} - {s['waves']} vagues")
        found = True
    if not found:
        print("Aucun score enregistré.")