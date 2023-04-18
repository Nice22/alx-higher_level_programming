#!/usr/bin/python3
import itertools

# Définir les réponses possibles
reponses = ['o', 'n']

# Générer toutes les combinaisons possibles
combinations = list(itertools.product(reponses, repeat=10))

# Afficher le nombre de combinaisons possibles
print("Nombre de combinaisons possibles :", len(combinations))

# Afficher les 10 premières combinaisons
print("10 premières combinaisons :")
for i in range(1024):
    print(combinations[i])
