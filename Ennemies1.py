#!/bin/python

class Personnage:
        def __init__ (self, nom, pv, end, mag):
                self.nom = nom
                self.pv = pv
                self.end = end
                self.mag = mag

#Creation du premier adversaire


#Creation instance  du perso avec ses caracteristiques
premier=Personnage(Noob, 50, 10,5)

#Annonce de l'ennemi
print(f"Prochain adversaire: {premier} !")
#Afficher les caracteristique du perso
print(f"Nom: {premier.nom}")
print(f"PV: {premier.pv}")
print(f"END: {premier.end}")
print(f"MAG: {premier.mag}")

