import itertools
import numpy
import pandas
import math

def sous_ensembles(tab):
    res = []
    for j in range(len(tab)):
        combinaisons = list(itertools.combinations(tab,j+1))
        taille = len(combinaisons)
        # Modification du style du retour, pour que ce soit un array et non pas un type itertools combinations
        for i in range(taille):
            res.append(list(combinaisons[i]))
    return(res)

def permutations(liste):
    res = []
    for i in range(len(liste)):
        permutations = list(itertools.permutations(liste[i]))
        taille = len(permutations)
        # Modification du style du retour, pour que ce soit un array et non pas un type itertools combinations
        for i in range(taille):
            res.append(list(permutations[i]))
    return(res)

def poids_cycle(liste, monnaie_consideree, tab_monnaies, df):
    # On insère doublement le sommet consiséré, au début et à la fin, pour faciliter le traitement
    liste.insert(0, monnaie_consideree)
    liste.append(monnaie_consideree)
    indice_depart = tab_monnaies.index(monnaie_consideree)
    somme = 1

    for i in range(len(liste)-1):
        nom_arrivee = liste[i+1]
        valeur = df[nom_arrivee][indice_depart]
        somme *= valeur
        indice_depart = tab_monnaies.index(liste[i+1])
    return somme

def programme_principal(df):
    # Données
    tab_monnaies = list(df["Currency"])

    for i in range(len(tab_monnaies)):
        monnaie_consideree = tab_monnaies[i]
        tab_sans_monnaie_consideree = list(df["Currency"])
        del tab_sans_monnaie_consideree[i]

        sousEnsembles = sous_ensembles(tab_sans_monnaie_consideree)
        permutation = permutations(sousEnsembles)
        liste_poids = []
        for j in range(len(permutation)):
            poids = poids_cycle(permutation[j], monnaie_consideree, tab_monnaies, df)
            liste_poids.append(poids)
        print(max(liste_poids))
    
#sousEnsembles = sous_ensembles(["A","B","C","D"], "C")
#permutation = permutations(sousEnsembles)
df = pandas.read_csv("tauxchange.csv")
print(df)
programme_principal(df)
