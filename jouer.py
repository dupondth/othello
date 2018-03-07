#!/usr/bin/python3
#coding:utf8

import plateau as p

def inputtotuple(chaine):
    '''But de cette fonction est de renvoyer
    un couple (a,b) en ayant récupéré "a,b"

    Entree
    ------
    chaine de la forme "a,b"

    Sortie
    ------
    Couple (a,b)
    '''
    liste = list(chaine)
    return (int(liste[0]), int(liste[2]))


def tour(num_tour, plateau, j1, j2):
    print("---- Tour " + str(num_tour) + "----")

    print(plateau.affichage(j1.couleur))
    case_j1 = inputtotuple(input("Case où j1 veut jouer : "))
    j1.jouer(case_j1)
    
    print(plateau.affichage(j2.couleur))
    case_j2 = inputtotuple(input("Case où j2 veut jouer : "))
    j2.jouer(case_j2)

   
def jeu(plateau, joueur1, joueur2):
    no_tour = 0 #numéro du tour courant
    tour(no_tour, plateau, joueur1, joueur2)

    while plateau.jouable(joueur1.couleur) \
        or plateau.jouable(joueur2.couleur):
        
        no_tour += 1
        tour(no_tour, plateau, joueur1, joueur2)


if __name__ == '__main__':
    plateau_jeu = p.plateau()
    joueurN = p.joueur('N', plateau_jeu)
    joueurB = p.joueur('B', plateau_jeu)

    jeu(plateau_jeu, joueurB, joueurN)
