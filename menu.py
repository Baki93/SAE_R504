#!/bin/python

import subprocess	


def afficher_menu():
	print("One vs One Tournament")
	print("1. Start")
	print("2. Crédit")
	print("3. Quitter")

def commencer_partie():
	print("La partie commence !")
	#Execution de v2.py
	subprocess.run(["python", "v2.py"])

def credit():
	print("Jeu de combat tour par tour en un contre un. Le système est facile a comprendre donc pas de tuto")
	print("Auteur: Kamel UNIQUEMENT il a triché. Karl a servi a rien la vérité")

while True:
	afficher_menu()
	choix = input("Fait ton choix bombarde:   ")
	if choix=="1":
		commencer_partie()
	elif choix=="2":
		credit()
	elif choix=="3":
		print("Wa t'es nul Alt+F4")
		break
	else:
		print("Ca me régale c'est soit 1 2 ou 3 mon reuf réveille toi !!!")

