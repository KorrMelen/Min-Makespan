#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import ceil

def LSA(D, M):
	for i in D:
		tmin = M[0]
		t = 0
		for j in range(len(M)):
			if M[j] < tmin:
				tmin = M[j]
				t = j
		M[t] += i
	return M


def merge(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1<n1 and i2<n2:
        if L1[i1] > L2[i2]:
            L12[i] = L1[i1]
            i1 += 1
        else:
            L12[i] = L2[i2]
            i2 += 1
        i += 1
    if i1<n1:
        while i1<n1:
            L12[i] = L1[i1]
            i1 += 1
            i += 1
    else:
        while i2<n2:
            L12[i] = L2[i2]
            i2 += 1
            i += 1
    return L12

def merge_sort_recur(L):
    n = len(L)
    if n > 1:
        p = int(n/2)
        L1 = L[0:p]
        L2 = L[p:n]
        merge_sort_recur(L1)
        merge_sort_recur(L2)
        L[:] = merge(L1,L2)
        return L
    
def merge_sort(L):
    L = merge_sort_recur(L)
    return L


def LPT(D, M):
	D = merge_sort(D)
	return (LSA(D,M))


def MYALGO(D, M):
	D = merge_sort(D)
	borneInf = max(max(D),ceil(sum(D)/len(M)))
	nonPlace = []
	for i in D:
		place = False
		j = 0
		while j < len(M) and not place :
			if M[j] + i <= borneInf :
				M[j] += i
				place = True
			j+=1
		if not place :
			nonPlace.append(i)
	return (LSA(nonPlace,M))
