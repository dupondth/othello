#!/usr/bin/python3
#coding:utf8

import plateau as p
import time

def tour(num_tour, plateau, j1, j2):
    '''Fonction qui fait avancer le jeu d'un tour, affiche l'état actuel du
    jeu dans le terminal et qui renvoie True s'il faut arrêter le jeu et False
    sinon.

    Entrées
    -------
    num_tour (int) : numéro du tour
    plateau (objet plateau) : plateau sur lequel le jeu se déroule
    j1 (objet joueur) : premier joueur
    j2 (objet joueur) : second joueur 

    Sortie
    ------
    booléen : True s'il faut continuer le jeu, False sinon
    '''

    print("\n-- Tour " + str(num_tour) + " --")
    #\n au début pour avoir une ligne vide entre les tours

    #print(plateau.affichage(j1.couleur)) #affichage du plateau

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
    
    #print(plateau.affichage(j2.couleur))
    
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
        return False #Arrêter le jeu
    else :
        return True #Continuer le jeu
    
    
def gagnant(plateau):
    '''Fonction qui renvoie la couleur du gagnant et le score final
    Entrée
    ------
    plateau (objet plateau)
    
    Sortie
    ------
    dictionnaire de la forme {'N':score, 'B':score}
    '''

    score_n = 0
    score_b = 0
    for pion in list(plateau.values()):
        if pion.couleur == 'N':
            score_n += 1
        else :
            score_b += 1
    return {'N':score_n, 'B':score_b}
        

def jeu(plateau, joueur1, joueur2):
    '''Fonction qui exécute le jeu jusqu'à ce que les deux joueurs ne puissent
    plus jouer.

    Entrées
    -------
    plateau (objet plateau) : Plateau sur lequel se déroule le jeu
    joueur1 (objet joueur) : Premier joueur 
    joueur2 (objet joueur) : Second joueur 
    '''
    
    no_tour = 0 #numéro du tour courant
    flag = True
    while flag:
        no_tour += 1
        flag = tour(no_tour, plateau, joueur1, joueur2)

def stats_jeux(num_jeux, J1, J2):
    '''Fonction qui joue N=num_jeux de jeux et qui renvoie le nombre de parties
    gagnées par chaque joueur'''
    
    dict_scores = {'joueurNoir':0, 'joueurBlanc':0, 'Egalite': 0}
    
    for _ in range(num_jeux):

        plat = p.plateau()
        types_joueurs = {'0':p.humain, '1':p.IAalea, '2':p.IAminmax, '3':p.IAminmax2}
        joueurN = types_joueurs[J1]('N', plat)
        joueurB = types_joueurs[J2]('B', plat)
        jeu(plat, joueurN, joueurB)
        scores = gagnant(plat)

        if scores['N'] > scores['B']:
            dict_scores['joueurNoir'] += 1
        elif scores['B'] > scores['N']:
            dict_scores['joueurBlanc'] += 1
        else: dict_scores['Egalite'] += 1

    return dict_scores


if __name__ == '__main__':
    
    mode = input("Choisissez un mode de jeu (0:partie simple, 1:simuler)  : ")
    
    #mode partie simple
    if mode == '0':
        types_joueurs = {'0':p.humain, '1':p.IAalea, '2':p.IAminmax, '3':p.IAminmax2}
        JN = input("Choisissez le joueur noir (0:humain, 1:IAalea, 2:IAmax, 3:IAminmax; 4:IAminmax2)  : ")
        JB = input("Choisissez le joueur blanc (0:humain, 1:IAalea, 2:IAmax, 3:IAminmax; 4:IAminmax2)  : ")
        plateau_jeu = p.plateau()
        joueurN = types_joueurs[JN]('N', plateau_jeu)
        joueurB = types_joueurs[JB]('B', plateau_jeu)
    
        jeu(plateau_jeu, joueurN, joueurB)
    
        print(plateau_jeu)
        print("\n-- Partie terminée --")
        scores = gagnant(plateau_jeu)
        print('Score joueur noir : ' + str(scores['N']))
        print('Score joueur blanc : ' + str(scores['B']))
    
    #mode simulation
    else:
        N = int(input("Nombre de parties à simuler  : "))
        JN = input("Choisissez le joueur noir (0:humain, 1:IAalea, 2:IAmax, 3:IAminmax; 4:IAminmax2)  : ")
        JB = input("Choisissez le joueur blanc (0:humain, 1:IAalea, 2:IAmax, 3:IAminmax; 4:IAminmax2)  : ")
        print(stats_jeux(N, JN, JB))