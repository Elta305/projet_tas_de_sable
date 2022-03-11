########################
# MITD-03
# Frédéric Li Combeau
# Lisa Vauvert
# Victor Combemorel
# Manel Mokrab
# https://github.com/uvsq-info/l1-python
########################

# import des librairies

import tkinter as tk
import random as rd
import os


########################

# constantes

HEIGHT = 600
WIDTH = 600
N = 5
CONFIGURATION_COURANTE = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

SAUVEGARDES = []
SAUVEGARDE_TMP = []

INTERRUPTION = False

TEMPS_ATTENTE = 1000

########################

# fonctions

def init_terrain():
    grille = []
    for i in range(N-2):
        grille.append(['#'])
        for j in range(N-2):
            grille[i].append(0)
        grille[i].append('#')
    grille.insert(0, ['#'] * N)
    grille.append(['#'] * N)
    return init_affichage(grille)

def init_affichage(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            canvas.create_text(50, 50, text = str(grid[i][j]))

def init_aleatoire():
    global SAUVEGARDE_TMP
    grille = []
    for i in range(N-2):
        grille.append(['#'])
        for j in range(N-2):
            grille[i].append(rd.randint(0, 6))
        grille[i].append('#')
    grille.insert(0, ['#'] * N)
    grille.append(['#'] * N)
    SAUVEGARDE_TMP = grille
    return init_affichage(grille)


def sauvegarder_config():
    global SAUVEGARDES, SAUVEGARDE_TMP
    SAUVEGARDES.append(SAUVEGARDE_TMP)
    return

def charger_config():
    global SAUVEGARDES, SAUVEGARDE_TMP
    num = int(input("Entrez le numéro de la sauvegarde à charger"))
    SAUVEGARDE_TMP = SAUVEGARDES[num]
    return init_affichage(SAUVEGARDE_TMP)

def addition():
    pass

def soustraction():
    pass

def stabilisation():
    list=[]
    for i in range(N+2): 
        list.append([])
        for j in range(N+2):
            if i==0 :
                list[i].append('#')
            elif j==0:
                list[i].append('#')
            elif i==N+1:
                list[i].append('#')
            elif j==N+1:
                list[i].append('#')
            else:
                list[i].append(0)
    return(list)

def interruption():
    global INTERRUPTION
    INTERRUPTION = True

def reprendre():
    global INTERRUPTION
    INTERRUPTION = False
    stabilisation()

# fonctions presets

def preset_random():
    global SAUVEGARDE_TMP
    grille = []
    for i in range(N-2):
        grille.append(['#'])
        for j in range(N-2):
            grille[i].append(rd.randint(0, 3))
        grille[i].append('#')
    grille.insert(0, ['#'] * N)
    grille.append(['#'] * N)
    SAUVEGARDE_TMP = grille
    return init_affichage(grille)

def preset_pilecentree():
    pass

def preset_maxstable():
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

def preset_identity():
    pass
    
def edition_taille():
    global N
    N = int(input("Choisissez une nouvelle taille de tableau"))
    return init_terrain()

def edition_temps():
    global TEMPS_ATTENTE
    TEMPS_ATTENTE = int(input("Choisissez le temps d'attente entre chaque stabilisation en millisecondes"))
    return TEMPS_ATTENTE


########################

# affichage


root = tk.Tk()

canvas = tk.Canvas(root, height=500, width = 500)
canvas.grid(column = 0, row = 0)

Initialisation = tk.Button(root, text="Initialisation", fg="black", command= Initialisation_bouton)
Initialisation.grid(column=1, row=0)

Aleatoire = tk.Button(root, text="Aleatoire", fg="black", command=init_aleatoire)
Aleatoire.grid(column=1, row=0)

Sauvegarder = tk.Button(root, text="Sauvergarder", fg="black", command=sauvegarder_config)
Sauvegarder.grid(column=1, row=0)

Charge = tk.Button(root, text="Charge", fg="black", command=charger_config)
Charge.grid(column=1, row=0)

Additionner = tk.Button(root, text="Additionner", fg="black", command=addition)
Additionner.grid(column=1, row=0)

Soustraire = tk.Button(root, text="Soustraire", fg="black", command=soustraction)
Soustraire.grid(column=1, row=0)

Stabiliser = tk.Button(root, text="Stabiliser", fg="black", command=stabilisation)
Stabiliser.grid(column=1, row=0)

Interrompre = tk.Button(root, text="Interrompre", fg="black", command=interruption)
Interrompre.grid(column=1, row=0)

Reprendre = tk.Button(root, text="Reprendre", fg="black", command=reprendre)
Reprendre.grid(column=1, row=0)

# boutons presets 

Random = tk.Button(root, text="Random", fg="black", command=preset_random)
Random.grid(column = 1, row = 1)

Pile_centree = tk.Button(root, text="pile centrée", fg="black", command=preset_pilecentree)
Pile_centree.grid(column = 1, row = 1)

Max_stable = tk.Button(root, text="Max stable", fg="black", command=preset_maxstable)
Max_stable.grid(column = 1, row = 1)

Double_max_stable = tk.Button(root, text="Double max stable", fg="black", command=preset_doublemaxstable)
Double_max_stable.grid(column = 1, row = 1)

Identify = tk.Button(root, text="Identity", fg="black", command=preset_identity)
Identify.grid(column = 1, row = 1)

# boutons édition

Edition= tk.Button(root, text="Edition", fg="red", command=edition_taille)
Edition.grid(column=1, row=0)

Taille= tk.Button(root, text="Taille", fg="red", command=edition_temps)
Taille.grid(column=1, row=0)


initialisation()
root.mainloop()
