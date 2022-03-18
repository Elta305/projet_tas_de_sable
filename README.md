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
Interrompre: Interrompt la stabilisation. Si activé, la stabilisation se fait étape par étape, cliquez sur le bouton reprendre pour que la stabilisation se fasse de nouveau de manière inintérrompue.  
Reprendre: Reprend la stabilisation.  

La colonne Presets, à droite du canvas, sont des presets.  

Random: Initialise la configuration avec des nombres aléatoires entre 0 et 3.  
Pile Centrée: Initialise la configuration courante avec un nombre choisi par l'utilisateur dans le terminal au centre.  
Max Stable: Initialise la configuration avec uniquement des 3.  
Double Max Stable: Initialise la configuration avec uniquement des 6.  
Identity: Initialise la configuration avec le preset Identity (Prend un peu de temps à charger selon la taille de la configuration).  
Flèche - Circuit Intégré - Megacorp - Bastion - Gemme - Emblème: Des presets originaux crées pour l'occasion :
![Emblème](https://media.discordapp.net/attachments/941701899760046170/952368739033157632/Capture_decran_2022-03-13_014737.png?width=1199&height=1207)

La colonne Edition, tout à droite, permet de modifier certains paramètres.  

Taille: Change la taille de la configuration avec le nombre donné dans le terminal. Lorsque la taille est de 50 ou plus, les nombres affichés disparaissent pour permettre une meilleure visibilité.  
Temps: Change le temps entre chaque étapes de la stabilisation (temps en millisecondes).  
Propagation4: Change la propagation aux 4 cases adjacentes (par défaut).  
Propagation8: Change la propagation aux 8 cases adjacentes. Si activée, la fonction Aléatoire initialisera la configuration avec des nombres aléatoires entre 0 et 10.  
