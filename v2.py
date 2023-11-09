#!/bin/python 

import random

class Personnage:
    def __init__(self, nom, points_de_vie, endurance, defense, magie):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.endurance = endurance
        self.defense = defense
        self.magie = magie
        self.attaque = 10  # Attaque de base
        self.esquive = 10  # Pourcentage d'esquive de base

    def attaquer(self, adversaire, choix_attaque):
        if choix_attaque == 1:  # Patate
            degats = self.attaque
            self.endurance -= 2
        elif choix_attaque == 2:  # Double patate
            degats = self.attaque * 2
            self.endurance -= 6
        elif choix_attaque == 3 : #Triple monstre
            degats = self.attaque * 2.5
            self.endurance -= 8
        elif choix_attaque == 4 : #Il a pas vu
            degats = self.attaque * 3
            self.endurance -= -10
        

        # Gestion de l'esquive
        if random.randint(1, 100) <= adversaire.esquive:
            print(f"{adversaire.nom} esquive l'attaque de {self.nom} !")
        else:
            degats -= adversaire.defense 
            adversaire.points_de_vie -= degats
            print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

    def utiliser_sort(self, adversaire, choix_sort):
        if choix_sort == 1:  # Restauration d'endurance
            self.endurance += random.randint(30, 80)
            self.magie -= 3
        elif choix_sort == 2:  # Boule de feu
            degats = random.randint(10, 20)
            adversaire.points_de_vie -= degats
            self.magie -= 5
            print(f"{self.nom} lance une boule de feu sur {adversaire.nom} et lui inflige {degats} points de dégâts.")
        

    def se_defendre(self):
        self.defense += 5
        self.esquive += 10

    def ameliorer_caracteristique(self,choix):
        print(f"Caractéristiques de {self.nom}:")
        print(f"1. Points de vie: {self.points_de_vie}")
        print(f"2. Endurance: {self.endurance}")
        print(f"3. Défense: {self.defense}")
        print(f"4. Magie: {self.magie}")
#        choix = int(input("Choisissez la caractéristique à améliorer (1-4) : "))
        if choix == 1:
            self.points_de_vie += 20
        elif choix == 2:
            self.endurance += 10
        elif choix == 3:
            self.defense += 5
        elif choix == 4:
            self.magie += 10
        else:
            print("Choix invalide.")

# Créez les adversaires
adversaires = [Personnage("Noob", 100, 20, 15, 10),
              Personnage("Chakaroun", 120, 15, 10, 20),
              Personnage("M'lik", 80, 25, 20, 15),
              Personnage("Amzal", 90, 10, 30, 25),
              Personnage("Fayssal", 110, 20, 15, 30)]

# Créez le personnage du joueur
nom_joueur = input("Choisissez le nom de votre personnage : ")
personnage_joueur = Personnage(nom_joueur, 100, 20, 30, 10)

print("Bienvenue dans le jeu de combat en tour par tour !")

# Début des combats
victoires = 0
for adversaire in adversaires:
    print(f"\nVous affrontez {adversaire.nom} !")
    while personnage_joueur.points_de_vie > 0 and adversaire.points_de_vie > 0:
        print("\nTour de votre personnage :")
        print(f"Points de vie de {personnage_joueur.nom}: {personnage_joueur.points_de_vie}")
        print(f"Points de vie de {adversaire.nom}: {adversaire.points_de_vie}")
        print("1. Attaquer")
        print("2. Utiliser un sort")
        print("3. Se défendre")
#        print("4. Améliorer une caractéristique")

        choix_action = int(input("Que voulez-vous faire ? "))

        if choix_action == 1:
            choix_attaque = int(input("Choisissez une attaque (1.Patate - 2.Double patate - 3.Triple monstre - 4.Il voit pas) : "))
            personnage_joueur.attaquer(adversaire, choix_attaque)
        elif choix_action == 2:
            choix_sort = int(input("Choisissez un sort (1.Regeneration - 2.Double Rotor ) : "))
            personnage_joueur.utiliser_sort(adversaire, choix_sort)
        elif choix_action == 3:
            personnage_joueur.se_defendre()
        elif choix_action == 4:
            personnage_joueur.ameliorer_caracteristique()

        if adversaire.points_de_vie <= 0:
            print(f"Vous avez vaincu {adversaire.nom} !")
            victoires += 1
            break

        print("\nTour de l'adversaire :")
        choix_attaque = random.randint(1, 4)
        adversaire.attaquer(personnage_joueur, choix_attaque)

        if personnage_joueur.points_de_vie <= 0:
            print(f"{adversaire.nom} vous a vaincu...")
            break

# Fin des combats
print("\nLa partie est terminée.")
if victoires == len(adversaires):
    print("Tié un monstre !")
else:
    print("Alt+F4 sah....")
