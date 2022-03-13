########################
# MITD-03
# Frédéric Li Combeau
# Lisa Vauvert
# Victor Combemorel
# Manel Mokrab
# https://github.com/uvsq-info/l1-python
########################

# Import des librairies

import tkinter as tk
import random as rd


########################

# Variables globales


HAUTEUR = 800
LARGEUR = 800
N = 15

SAUVEGARDES = []
SAUVEGARDE_TMP = []

TEMPS_ATTENTE = 100
PROPAGATION = 4
INTERRUPTION = False


####################
# Fonctions


def init_terrain():
    """ -> func
        Renvoie la fonction init_affichage avec une matrice remplie de 0 en paramètres
    """
    global SAUVEGARDE_TMP
    grille = []
    for i in range(N-2):
        grille.append(['#'])
        for j in range(N-2):
            grille[i].append(0)
        grille[i].append('#')
    grille.insert(0, ['#'] * N)
    grille.append(['#'] * N)
    SAUVEGARDE_TMP = grille
    return init_affichage(grille)


def init_aleatoire():
    """ -> func
        Renvoie la fonction init_affichage avec une matrice remplie de nombres aléatoires entre 0 et 6 en paramètres
    """
    global SAUVEGARDE_TMP, PROPAGATION
    grille = []
    nb = 6
    if PROPAGATION == 8:
        nb = 10
    for i in range(N-2):
        grille.append(['#'])
        for j in range(N-2):
            grille[i].append(rd.randint(0, nb))
        grille[i].append('#')
    grille.insert(0, ['#'] * N)
    grille.append(['#'] * N)
    SAUVEGARDE_TMP = grille
    return init_affichage(grille)


def init_affichage(grille):
    """ Affiche la grille en paramètre dans un canvas tkinter """
    couleurs = ["green yellow", "green3", "green", "yellow", "goldenrod1", "orange2", "chocolate1", "red", "red3", "purple3"]

    global HAUTEUR, LARGEUR, N
    hauteur_case = HAUTEUR // N
    largeur_case = LARGEUR // N
    color = "gray"

    for i in range(len(grille)):
        for j in range(len(grille[i])):

            if grille[i][j] == "#":
                color = "gray"
            elif grille[i][j] <= 9:
                color = couleurs[grille[i][j]]
            else:
                color = couleurs[9]

            canvas.create_rectangle((j*largeur_case), (i*hauteur_case), (j*largeur_case+largeur_case), (i*hauteur_case+hauteur_case), fill=color)
            if N < 50:
                canvas.create_text(((j*largeur_case) + (largeur_case//2)), ((i*hauteur_case) + (hauteur_case // 2)), text=str(grille[i][j]))


def sauvegarder_config():
    """ Sauvegarde la configuration courante """
    global SAUVEGARDES, SAUVEGARDE_TMP
    SAUVEGARDES.append(SAUVEGARDE_TMP)


def charger_config():
    """ Charge la configuration choisie """
    global SAUVEGARDES, SAUVEGARDE_TMP
    num = int(input("Entrez le numéro de la sauvegarde à charger"))
    if len(SAUVEGARDES) < num:
        return print("Configuration inexistante !")
    SAUVEGARDE_TMP = SAUVEGARDES[num]
    return init_affichage(SAUVEGARDES[num])


def addition():
    """ -> func
        Renvoie la fonction init_affichage avec tab1 une liste qui est l'addition entre la configuration courante et la sauvegarde choisie en paramètre
    """
    global SAUVEGARDES, SAUVEGARDE_TMP
    num = int(input("Entrez le numéro de la sauvegarde à additionner avec cette configuration"))
    if len(SAUVEGARDES) < num:
        return print("Configuration inexistante !")
    tab1 = SAUVEGARDE_TMP[1:-1]
    tab2 = SAUVEGARDES[num][1:-1]

    for i in range(len(tab1)):
        for j in range(len(tab1[i])):
            if isinstance(tab1[i][j], int):
                tab1[i][j] += tab2[i][j]
    
    tab1.insert(0, ['#'] * N)
    tab1.append(['#'] * N)
    SAUVEGARDE_TMP = tab1
    return init_affichage(tab1)


def soustraction():
    """ -> func
        Renvoie la fonction init_affichage avec tab1 une liste qui est la soustraction entre la configuration courante et la sauvegarde choisie en paramètre
    """
    global SAUVEGARDES, SAUVEGARDE_TMP
    num = int(input("Entrez le numéro de la sauvegarde à soustraire avec cette configuration"))
    if len(SAUVEGARDES) < num:
        return print("Configuration inexistante !")
    tab1 = SAUVEGARDE_TMP[1:-1]
    tab2 = SAUVEGARDES[num][1:-1]
    for i in range(len(tab1)):
        for j in range(len(tab1[i])):
            if isinstance(tab1[i][j], int):
                tab1[i][j] -= tab2[i][j]
                if tab1[i][j] < 0:
                    tab1[i][j] = 0
                
    
    tab1.insert(0, ['#'] * N)
    tab1.append(['#'] * N)
    SAUVEGARDE_TMP = tab1
    return init_affichage(tab1)


def stabilisation():
    """ Stabilise le tas de sable jusqu'à que le tas ne puisse plus être stabilisé """
    global SAUVEGARDE_TMP, INTERRUPTION, TEMPS_ATTENTE, PROPAGATION
    tab = SAUVEGARDE_TMP
    continuer = False
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if isinstance(tab[i][j], int):
                if PROPAGATION == 4:
                    if tab[i][j] >= 4:
                        if (isinstance(tab[i-1][j], int)):
                            tab[i-1][j] += 1
                        if (isinstance(tab[i+1][j], int)):
                            tab[i+1][j] += 1
                        if (isinstance(tab[i][j-1], int)):
                            tab[i][j-1] += 1
                        if (isinstance(tab[i][j+1], int)):
                            tab[i][j+1] += 1
                        tab[i][j] -= 4
                else: 
                    if tab[i][j] >= 8:
                        if (isinstance(tab[i-1][j], int)):
                            tab[i-1][j] += 1
                        if (isinstance(tab[i+1][j], int)):
                            tab[i+1][j] += 1
                        if (isinstance(tab[i][j-1], int)):
                            tab[i][j-1] += 1
                        if (isinstance(tab[i][j+1], int)):
                            tab[i][j+1] += 1
                        if (isinstance(tab[i-1][j-1], int)):
                            tab[i-1][j-1] += 1
                        if (isinstance(tab[i+1][j+1], int)):
                            tab[i+1][j+1] += 1
                        if (isinstance(tab[i+1][j-1], int)):
                            tab[i+1][j-1] += 1
                        if (isinstance(tab[i+1][j+1], int)):
                            tab[i+1][j+1] += 1
                        tab[i][j] -= 8

    init_affichage(tab)
    tab2 = tab[1: -1]
    for i in range(len(tab2)):
        for j in range(len(tab2[i][1: -1])):
            if PROPAGATION == 4:
                if tab2[i][j+1] >= 4:
                    continuer = True
            else:
                if tab2[i][j+1] >= 8:
                    continuer = True
    if continuer is False:
        return
    if INTERRUPTION is False:
        root.after(TEMPS_ATTENTE, stabilisation)


def interruption():
    """ Interrompt la stabilisation """
    global INTERRUPTION
    INTERRUPTION = True


def reprendre():
    """ -> func
        Reprend la stabilisation
    """
    global INTERRUPTION
    INTERRUPTION = False
    return stabilisation()


# Presets


def preset_random():
    """ -> func
        Renvoie la fonction init_affichage avec une matrice remplie de nombres entre 0 et 3 en paramètres
    """
    global SAUVEGARDE_TMP
    grille = []
    for i in range(N-2):
        grille.append(['#'])
        for j in range(N-2):
            grille[i].append(rd.randint(0,3))
        grille[i].append('#')
    grille.insert(0, ['#'] * N)
    grille.append(['#'] * N)
    SAUVEGARDE_TMP = grille
    return init_affichage(grille)


def preset_pilecentree():
    """ -> func
        Renvoie la fonction init_affichage avec une matrice remplie de 0 sauf au centre ou la valeur est choisie par l'utilisateur
    """
    global SAUVEGARDE_TMP
    grille = SAUVEGARDE_TMP
    grille[N//2][N//2] = int(input("Entrez la valeur que vous voulez mettre au centre: "))
    if grille[N//2][N//2] < 0:
        return print("Vous ne pouvez pas mettre de nombres négatifs !")
    SAUVEGARDE_TMP = grille
    return init_affichage(grille)


def preset_maxstable():
    """ -> func
        Renvoie la fonction init_affichage avec une matrice remplie de 3
    """
    global SAUVEGARDE_TMP
    grille = []
    for i in range(N-2):
        grille.append(['#'])
        for j in range(N-2):
            grille[i].append(3)
        grille[i].append('#')
    grille.insert(0, ['#'] * N)
    grille.append(['#'] * N)
    SAUVEGARDE_TMP = grille
    return init_affichage(grille)


def preset_doublemaxstable():
    """ -> func
        Renvoie la fonction init_affichage avec une matrice remplie de 6
    """
    global SAUVEGARDE_TMP
    grille = []
    for i in range(N-2):
        grille.append(['#'])
        for j in range(N-2):
            grille[i].append(6)
        grille[i].append('#')
    grille.insert(0, ['#'] * N)
    grille.append(['#'] * N)
    SAUVEGARDE_TMP = grille
    return init_affichage(grille)


# Sous-fonctions des presets suivants


def doublemax():
    """ -> list
        Renvoie une matrice remplie de 6
    """
    grille = []
    for i in range(N-2):
        grille.append(['#'])
        for j in range(N-2):
            grille[i].append(6)
        grille[i].append('#')
    grille.insert(0, ['#'] * N)
    grille.append(['#'] * N)
    return grille


def stab(tab):
    """ Stabilise une fois la matrice """
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if isinstance(tab[i][j], int):
                if tab[i][j] >= 4:
                    if (isinstance(tab[i-1][j], int)):
                        tab[i-1][j] += 1
                    if (isinstance(tab[i+1][j], int)):
                        tab[i+1][j] += 1
                    if (isinstance(tab[i][j-1], int)):
                        tab[i][j-1] += 1
                    if (isinstance(tab[i][j+1], int)):
                        tab[i][j+1] += 1
                    tab[i][j] -= 4


def soustract(grille, grille2):
    """ Soustrait la matrice grille1 à la matrice grille2 """
    grille = grille[1:-1]
    grille2 = grille2[1:-1]
    for i in range(len(grille2)):
        for j in range(len(grille2[i])):
            if isinstance(grille2[i][j], int):
                grille2[i][j] -= grille[i][j]
                if grille2[i][j] < 0:
                    grille2[i][j] = 0

    grille2.insert(0, ['#'] * N)
    grille2.append(['#'] * N)
    return grille2


def preset_identity():
    """ -> func
        Renvoie le preset Identity
    """
    global SAUVEGARDE_TMP
    
    grille = doublemax()
    tab = grille[1: -1]
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 4:
                stab(grille)

    grille2 = doublemax()            
    tab2 = soustract(grille, grille2)
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 3:
                stab(tab2)
    SAUVEGARDE_TMP = tab2
    return init_affichage(tab2)


def preset_fleche():
    """ -> func
        Renvoie le preset Flèche
    """
    global SAUVEGARDE_TMP
    
    grille = doublemax()
    tab = grille[1: -1]
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 3:
                stab(grille)

    grille2 = doublemax()            
    tab2 = soustract(grille, grille2)
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 4:
                stab(tab2)
    SAUVEGARDE_TMP = tab2
    return init_affichage(tab2)


def preset_circuit_integre():
    """ -> func
        Renvoie le preset Circuit intégré
    """
    global SAUVEGARDE_TMP
    
    grille = doublemax()
    tab = grille[1: -1]
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 4:
                stab(grille)

    grille2 = doublemax()            
    tab2 = soustract(grille, grille2)
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 4:
                stab(tab2)
    SAUVEGARDE_TMP = tab2
    return init_affichage(tab2)


def preset_megacorp():
    """ -> func
        Renvoie le preset Megacorp
    """
    global SAUVEGARDE_TMP
    
    grille = doublemax()
    tab = grille[1: -1]
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 5:
                stab(grille)

    grille2 = doublemax()            
    tab2 = soustract(grille, grille2)
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 5:
                stab(tab2)
    SAUVEGARDE_TMP = tab2
    return init_affichage(tab2)


def preset_bastion():
    """ -> func
        Renvoie le preset Bastion
    """
    global SAUVEGARDE_TMP
    
    grille = doublemax()
    tab = grille[1: -1]
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 4:
                stab(grille)

    grille2 = doublemax()            
    tab2 = soustract(grille, grille2)
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 5:
                stab(tab2)
    SAUVEGARDE_TMP = tab2
    return init_affichage(tab2)


def preset_gemme():
    """ -> func
        Renvoie le preset Gemme
    """
    global SAUVEGARDE_TMP
    
    grille = doublemax()
    tab = grille[1: -1]
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 5:
                stab(grille)

    grille2 = doublemax()            
    tab2 = soustract(grille, grille2)
    stab(tab2)
    SAUVEGARDE_TMP = tab2
    return init_affichage(tab2)


def preset_embleme():
    """ -> func
        Renvoie le preset Emblème
    """
    global SAUVEGARDE_TMP
    
    grille = doublemax()
    tab = grille[1: -1]
    for i in range(len(tab)):
        for j in range(len(tab[i][1: -1])):
            if tab[i][j+1] >= 4:
                stab(grille)

    grille2 = doublemax()            
    tab2 = soustract(grille, grille2)
    stab(tab2)
    SAUVEGARDE_TMP = tab2
    return init_affichage(tab2)


# Edition


def edition_taille():
    """ -> func
        Renvoie la fonction init_terrain avec la taille de tableau choisi
    """
    global N
    tmp = N
    N = int(input("Choisissez une nouvelle taille de tableau: "))
    if N <= 3:
        N = tmp
        return print("Vous ne pouvez pas créer de matrice aussi petites !")
    return init_terrain()


def edition_temps():
    """ -> int
        Renvoie le temps d'attente choisi en millisecondes
    """
    global TEMPS_ATTENTE
    TEMPS_ATTENTE = int(input("Choisissez le temps d'attente entre chaque stabilisation en millisecondes: "))
    return TEMPS_ATTENTE


def propagation4():
    """ Change la propagation aux 4 cases adjacentes """
    global PROPAGATION
    PROPAGATION = 4


def propagation8():
    """ Change la propagation aux 8 cases adjacentes """
    global PROPAGATION
    PROPAGATION = 8


#########################

# Partie principale

root = tk.Tk()
root.title("Génération de terrain")

canvas = tk.Canvas(root, height=HAUTEUR, width=LARGEUR)
canvas.grid(column=1, row=0, rowspan=9)

# Création des widgets

bouton_init = tk.Button(text="Initialisation", command=init_terrain)
bouton_init.grid(column=0, row=0)
bouton_aleatoire = tk.Button(text="Aléatoire", command=init_aleatoire)
bouton_aleatoire.grid(column=0, row=1)

bouton_save = tk.Button(text="Sauvegarder", command=sauvegarder_config)
bouton_save.grid(column=0, row=2)
bouton_load = tk.Button(text="Charger", command=charger_config)
bouton_load.grid(column=0, row=3)

bouton_add = tk.Button(text="Additionner", command=addition)
bouton_add.grid(column=0, row=4)
bouton_sub = tk.Button(text="Soustraire", command=soustraction)
bouton_sub.grid(column=0, row=5)

bouton_stab = tk.Button(text="Stabiliser", command=stabilisation)
bouton_stab.grid(column=0, row=6)
bouton_int = tk.Button(text="Interrompre", command=interruption)
bouton_int.grid(column=0, row=7)
bouton_rep = tk.Button(text="Reprendre", command=reprendre)
bouton_rep.grid(column=0, row=8)

# Presets

preset = tk.Label(text='Presets')
preset.grid(column=2, row=0)

bouton_preset_rdm = tk.Button(text="Random", command=preset_random)
bouton_preset_rdm.grid(column=2, row=1)
bouton_preset_pilecentree = tk.Button(text="Pile Centrée", command=preset_pilecentree)
bouton_preset_pilecentree.grid(column=2, row=2)
bouton_preset_maxstable = tk.Button(text="Max Stable", command=preset_maxstable)
bouton_preset_maxstable.grid(column=2, row=3)
bouton_preset_doublemaxstable = tk.Button(text="Double Max Stable", command=preset_doublemaxstable)
bouton_preset_doublemaxstable.grid(column=2, row=4)
bouton_preset_identity = tk.Button(text="Identity", command=preset_identity)
bouton_preset_identity.grid(column=2, row=5)
bouton_preset_fleche = tk.Button(text="Flèche", command=preset_fleche)
bouton_preset_fleche.grid(column=2, row=6)
bouton_preset_circuit_integre = tk.Button(text="Circuit Intégré", command=preset_circuit_integre)
bouton_preset_circuit_integre.grid(column=2, row=7)
bouton_preset_megacorp = tk.Button(text="Megacorp", command=preset_megacorp)
bouton_preset_megacorp.grid(column=2, row=8)

bouton_preset_bastion = tk.Button(text="Bastion", command=preset_bastion)
bouton_preset_bastion.grid(column=3, row=6)
bouton_preset_gemme = tk.Button(text="Gemme", command=preset_gemme)
bouton_preset_gemme.grid(column=3, row=7)
bouton_preset_embleme = tk.Button(text="Emblème", command=preset_embleme)
bouton_preset_embleme.grid(column=3, row=8)

# Edition

edition = tk.Label(text='Edition')
edition.grid(column=4, row=0)

bouton_edition_taille = tk.Button(text="Taille", command=edition_taille)
bouton_edition_taille.grid(column=4, row=1)
bouton_edition_temps = tk.Button(text="Temps", command=edition_temps)
bouton_edition_temps.grid(column=4, row=2)
bouton_edition_propagation4 = tk.Button(text="Propagation 4", command=propagation4)
bouton_edition_propagation4.grid(column=4, row=3)
bouton_edition_propagation8 = tk.Button(text="Propagation 8", command=propagation8)
bouton_edition_propagation8.grid(column=4, row=4)

init_terrain()
root.mainloop()
