#!/usr/bin/python3
#coding:utf8

import plateau as p
import time

def tour(num_tour, plateau, j1, j2):
    print("\n-- Tour " + str(num_tour) + " --")
    #\n au début pour avoir une ligne vide entre les tours

    print(plateau.affichage(j1.couleur))

    #Boucle while pour boucler tant que le coup n'est pas valide
    flag1 = True
    while flag1:
        try:
            j1.jouer()
            flag1 = False
        except ValueError:
            print("Veuillez jouer dans une case valide")
    
    print(plateau.affichage(j2.couleur))

    flag2 = True
    while flag2:
        try:
            j2.jouer()
            flag2 = False
        except ValueError:
            print("Veuillez jouer dans une case valide")
    
def gagnant(plateau):
    '''Fonction qui renvoie la couleur du gagnant et le score final
    Entrée
    ------
    plateau (objet plateau)
    
    Sortie
    ------
    dictionnaire de la forme {'B':score, 'N':score}
    '''

    score_b = 0
    score_n = 0
    for pion in list(plateau.values()):
        if pion.couleur == 'B':
            score_b += 1
        else :
            score_n += 1
    return {'B':score_b, 'N':score_n}
        

def jeu(plateau, joueur1, joueur2):
    no_tour = 0 #numéro du tour courant
    tour(no_tour, plateau, joueur1, joueur2)

    while plateau.jouable(joueur1.couleur) \
        or plateau.jouable(joueur2.couleur):
        no_tour += 1
        tour(no_tour, plateau, joueur1, joueur2)

    print("\n-- Partie terminée --")
    scores = gagnant(plateau)
    print('Score joueur blanc : ' + str(scores['B']))
    print('Score joueur noir : ' + str(scores['N']))
    

if __name__ == '__main__':
    plateau_jeu = p.plateau()
    joueurN = p.IAalea('N', plateau_jeu)
    joueurB = p.IAalea('B', plateau_jeu)

    jeu(plateau_jeu, joueurB, joueurN)
