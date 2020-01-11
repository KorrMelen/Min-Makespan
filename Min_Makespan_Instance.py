#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint

def input_file():
	name_file = input("Entrez le nom du fichier :\n")
	file = open(name_file,"r")
	instance = file.read()
	file.close()
	instance = instance.split(":")
	instance = list(map(int,instance))

	M = [0]*instance[0]
	D = [0]*instance[1]

	for i in range(2,len(instance)):
		D[i-2] = instance[i]
	return D,M


def input_keyboard():
	instance = input("Donnez l'instance dans le format m:n:d1:d2:...:dn :\n")
	instance = instance.split(":")
	instance = list(map(int,instance))

	M = [0]*instance[0]
	D = [0]*instance[1]

	for i in range(2,len(instance)):
		D[i-2] = instance[i]
	return D,M


def input_Im():
	m = int(input("Donnez le nombre de machine :\n"))
	M = [0]*m
	D = [0]*(2*m+1)
	D[0] = m
	for i in range(m):
		D[i*2+1] = D[i*2+2] = m+i
	return D,M


def input_Ir():
	m = int(input("Donnez le nombre de machine :\n"))
	n = int(input("Donnez le nombre de tâche :\n"))
	k = int(input("Donnez le nombre d'instance :\n"))
	minv = int(input("Donnez la durée minimum d'une tâche :\n"))
	maxv = int(input("Donnez la durée maximum d'une tâche :\n"))
	Ms = []
	Ds = []
	M = [0]*m
	for i in range(k):
		D = [0]*n
		for j in range(n):
			D[j] = randint(minv,maxv)
		Ms.append(M.copy())
		Ds.append(D)
	return Ds,Ms