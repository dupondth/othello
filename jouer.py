#!/usr/bin/python3
#coding:utf8

import plateau as p
import time

def tour(num_tour, plateau, j1, j2):
    print("\n-- Tour " + str(num_tour) + " --")
    #\n au début pour avoir une ligne vide entre les tours

    print(plateau.affichage(j1.couleur))

    jouable1, jouable2 = True, True

    #Si le joueur peut jouer, il joue
    if plateau.jouable(j1.couleur):
        flag1 = True
        #Boucle while pour boucler tant que le coup n'est pas valide
        while flag1:
            try:
                j1.jouer()
                flag1 = False
            except ValueError:
                print("Veuillez jouer dans une case valide")
    else:
        jouable1 = False
    
    print(plateau.affichage(j2.couleur))
    
    #Si le joueur peut jouer, il joue
    if plateau.jouable(j2.couleur):
        flag2 = True
        while flag2:
            try:
                j2.jouer()
                flag2 = False
            except ValueError:
                print("Veuillez jouer dans une case valide")
    else:
        jouable2 = False

    if jouable1 == False and jouable2 == False:
        print(plateau)
        print("\n-- Partie terminée --")
        scores = gagnant(plateau)
        print('Score joueur blanc : ' + str(scores['B']))
        print('Score joueur noir : ' + str(scores['N']))

        return False
    else :
        return True
    
    
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
    flag = True
    while flag:
        no_tour += 1
        flag = tour(no_tour, plateau, joueur1, joueur2)

if __name__ == '__main__':
    plateau_jeu = p.plateau()
    joueurN = p.IAalea('N', plateau_jeu)
    joueurB = p.IAalea('B', plateau_jeu)

    jeu(plateau_jeu, joueurB, joueurN)
