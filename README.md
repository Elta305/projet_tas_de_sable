########################
# MITD-03
# Frédéric Li Combeau
# Lisa Vauvert
# Victor Combemorel
# Manel Mokrab
# https://github.com/uvsq-info/l1-python
########################

Projet de L1 sur les tas de sable "Abelian Sandpiles".

Mode d'emploi:

Les boutons de la première colonne sont les boutons de base du projet.

Initialisation: Initialise la configuration avec uniquement des 0.
Aléatoire: Initialise la configuration avec des nombres aléatoires entre 0 et 6.
Sauvegarder: Sauvegarde la configuration courante.
Charger: Charge une sauvegarde. Entrez 0 dans le terminal pour charger la dernière configuration sauvegardée et incrémentez de 1 pour accéder aux sauvegardes préédentes ou -1 pour la première et décrémentez pour les sauvegardes suivantes.
Addition: Additionne la configuration courante avec la configuration sauvegardée choisie dans le terminal.
Soustraction: Soustractionne la configuration courante avec la configuration sauvegardée choisie dans le terminal.
Stabilisation: Lance la stabilisation du tas de sable.
Interrompre: Interompt la stabilisation.
Reprendre: Remprend la stabilisation.

La colonne Presets, à droite du canvas, sont des presets.

Random: Initialise la configuration avec des nombres aléatoires entre 0 et 3.
Pile Centrée: Initialise la configuration avec uniquement des 0 et un nombre choisi par l'utilisateur dans le terminal au centre.
Max Stable: Initialise la configuration avec uniquement des 3.
Double Max Stable: Initialise la configuration avec uniquement des 6.
Identity: Initialise la configuration avec le preset Identity (Prend un peu de temps à charger selon la taille de la configuration.

La colonne Edition, tout à droite, permet de modifier certains paramètres.

Taille: Change la taille de la configuration avec le nombre donneé dans le terminal.
Temps: Change le temps entre chaque étapes de la stabilisation (temps en millisecondes).
