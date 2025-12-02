1. **Initialisation de la base de données**
    - Script `db_init.py` pour insérer les personnages et monstres dans MongoDB.
2. **Lancement du jeu**
    - Script `main.py` proposant le menu principal et gérant les interactions.
3. **Gestion des combats**
    - Script `game.py` gérant la logique du combat.
4. **Modélisation des données**
    - Script `models.py` contenant les classes pour les personnages et les monstres. les stats atq, hp, shield (pour la partie orienter objet) lasse caracter avec pv atq...
5. **Fonctions utilitaires**
    - Script `utils.py` contenant les fonctions pour l'affichage et la gestion des données.


### Exécution du projet

1. Initialiser la base de données :
    python db_init.py
    
2. Lancer le jeu :
    python main.py