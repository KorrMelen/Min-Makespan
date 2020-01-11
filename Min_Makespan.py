#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from statistics import mean
from math import ceil
from sys import exit
import Min_Makespan_Instance
import Min_Makespan_Algos

def input_choice():
	c = input("""Choix du mode de saisie des instances d'entrée:
	1 : Depuis un fichier
	2 : Au clavier
	3 : Génération d'une instance de type Im
	4 : Génération aléatoire de plusieurs instances
	5 : Quitter le programme\n""")
	c = int(c)
	if c == 5:
		exit()
	switcher = {
		1:Min_Makespan_Instance.input_file,
		2:Min_Makespan_Instance.input_keyboard,
		3:Min_Makespan_Instance.input_Im,
		4:Min_Makespan_Instance.input_Ir
	}
	func = (switcher.get(c, lambda: "Choix non défini"))
	return(func())


print("""#################################################################
#     Problème de MIN MAKESPAN : algorithme d'approximation     #
#################################################################""")

while(True):
	D,M = input_choice()

	print("#################################################################")
	
	if type(D[0]) == int :
		borneInfMax = max(D)
		borneInfMoy = ceil(sum(D)/len(M))
		resLSA = max(Min_Makespan_Algos.LSA(D.copy(),M.copy()))
		ratioLSA = resLSA / max(borneInfMoy,borneInfMax)
		resLPT = max(Min_Makespan_Algos.LPT(D.copy(),M.copy()))
		ratioLPT = resLPT / max(borneInfMax,borneInfMoy)

		print("Borne Inférieur Maximun = ",borneInfMax)
		print("Borne Inférieur Moyenne = ",borneInfMoy)
		print("Résultat LSA = ",resLSA)
		print("Ratio LSA = ",ratioLSA)
		print("Résultat LPT = ",resLPT)
		print("Ratio LPT = ",ratioLPT)

	else:
		ratioLSA = 0
		ratioLPT = 0
		for i in range(len(D)):
			borneInfMax = max(D[i])
			borneInfMoy = ceil(sum(D[i])/len(M[i]))
			ratioLSA += max(Min_Makespan_Algos.LSA(D[i].copy(),M[i].copy())) / max(borneInfMoy,borneInfMax)
			ratioLPT += max(Min_Makespan_Algos.LPT(D[i].copy(),M[i].copy())) / max(borneInfMax,borneInfMoy)
		print("Ratio moyen LSA = ",(ratioLSA/len(D)))
		print("Ratio moyen LPT = ",(ratioLPT/len(D)))

	print("#################################################################")