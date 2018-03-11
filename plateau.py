#!/usr/bin/python3
#coding:utf8

import sys
from random import choice

def increment(direction, position):
    # 7 0 1
    # 6   2
    # 5 4 3
    if direction == 0: 
        return (position[0]-1, position[1])
    if direction == 1: 
        return (position[0]-1, position[1]+1)
    if direction == 2: 
        return (position[0], position[1]+1)
    if direction == 3: 
        return (position[0]+1, position[1]+1)
    if direction == 4: 
        return (position[0]+1, position[1])
    if direction == 5: 
        return (position[0]+1, position[1]-1)
    if direction == 6: 
        return (position[0], position[1]-1)
    if direction == 7: 
        return (position[0]-1, position[1]-1)

def inputtotuple(chaine):
    '''Fonction qui renvoie un couple de position style matrice avec
    comme entrée un chaine style plateau.
    ex: d2 -> (1,3)
        a1 -> (0,0)

    Entrée
    ------
    chaine (str) 

    Sortie
    ------
    couple (tuple) 
    '''

    liste = list(chaine)
    return (int(liste[1])-1, ord(liste[0])-97)
   

class plateau(dict): #le plateau est un dictionnaire
    def __init__(self):
        self.perimetre = 8   #plateau carré de 8 par 8

        self[(3,3)] = pion('B')
        self[(4,4)] = pion('B')
        
        self[(3,4)] = pion('N')
        self[(4,3)] = pion('N')

    def coupValide(self, case_depart, couleur_joueur): 
        '''Fonction qui renvoie si une case est valide ou non

        Entrées
        -------
        case à vérifier (couple)
        couleur du joueur ('N' ou 'B')

        Sortie
        ------
        couple fait d'un booléen True si le coup est valide et la liste des
        pions à tourner si on joue sur cette case
        '''

        atourner = list() #Liste des pions à retourner
        valide = False #le coup n'est pas valide par défaut

        if case_depart in self: 
        #Vérification que la position n'est pas déjà occupée
            return (valide, atourner)
        
        for direct in range(8): #on cherche dans les 8 directions
            fini = False
            #on ne s'arrete pas de chercher tant que fini n'est pas vrai
            verif1 = True
            #verif1 pour savoir si c'est une case directement adjacente
            #en effet si on rencontre un pion de la même couleur adjacent, le
            #coup n'est pas valide mais s'il y a des pions différents puis un
            #pions de même couleur alors le coup est valide.
            pos = case_depart

            atourner_temp = list() #Sera ajoutée à atourner si la direction est
                                   #validée

            while not fini:
                pos = increment(direct, pos)
                
                if verif1:
                    if pos in self and self[pos].couleur != couleur_joueur: 
                    #on se sert de l'évaluation paresseuse pour ne pas 
                    #avoir d'erreur
                        verif1 = False 
                        atourner_temp.append(pos)
                        
                    else: #vide ou hors plateau ou case meme couleur
                        fini = True #coup non valide
                
                else: #on n'est plus au 1er tour
                    if pos in self and self[pos].couleur != couleur_joueur:
                        atourner_temp.append(pos)
                        
                    elif pos in self and self[pos].couleur == couleur_joueur:
                        fini = True
                        valide = True
                        for couple in atourner_temp: #on sauvegarde
                            atourner.append(couple)
                    
                    else: #vide ou hors plateau
                        fini = True
                        
        return (valide, atourner) #un couple

                
    def jouable(self, clr):
        '''Fonction qui renvoie True si un joueur de couleur clr peut
        jouer et False sinon.
        
        rq : Cette fonction est celle permettant de ne pas jouer en-dehors
        de plateau
        '''

        for i in range(self.perimetre):
            for j in range(self.perimetre):
                if self.coupValide((i,j), clr)[0]:
                    return True
        return False

    def listeValide(self, clr):
        '''Fonction qui renvoie une liste des case jouables pour un joueur

        Entrée
        ------
        clr (str) : couleur du joueur : 'N' ou 'B'

        Sortie
        ------
        liste de couples qui correspondent au coordonnées jouables
        '''

        cases_jouables = list()

        for i in range(self.perimetre):
            for j in range(self.perimetre):
                if self.coupValide((i,j), clr)[0]:
                    cases_jouables.append((i,j))
                    
        return cases_jouables
                

                
    def __str__(self):

        s = ' ABCDEFGH\n' #première ligne de notre affichage

        for i in range(self.perimetre):
            s += str(i+1)
            for j in range(self.perimetre):
                
                if (i,j) in self: #s'il y a un pion à cette position
                    s += self[(i,j)].couleur #on récupère la couleur du pion
                else :
                    s += '.'
            s += '\n' #passage à la ligne suivante

        return s

    def affichage(self, couleur_joueur):
        
        couleurs = {'N':'Noir', 'B':'Blanc'}
        s = '\nTour du joueur ' + couleurs[couleur_joueur] + '\n'
        #\n au début pour avoir une ligne vide entre les tours des joueurs
        s += ' ABCDEFGH\n' #première ligne de notre affichage
        
        for i in range(self.perimetre):
            s += str(i+1)
            for j in range(self.perimetre):
                
                if (i,j) in self: #s'il y a un pion à cette position
                    s += self[(i,j)].couleur #on récupère la couleur du pion

                #on vérifie que le coup est valide pour savoir où jouer
                elif self.coupValide((i,j), couleur_joueur)[0]:
                    s += '#'
                    #s += str(len(self.coupValide((i,j), couleur_joueur)[1])) 
                else :
                    s += '.'
            s += '\n' #passage à la ligne suivante

        return s


class pion(object):
    
    def __init__(self, clr):
        self.couleur = clr

    @property
    def couleur(self):
        return self.__couleur

    @couleur.setter
    def couleur(self, nvlle_clr):
        if nvlle_clr in ['N', 'B']:
            self.__couleur = nvlle_clr
        elif not isinstance(nvlle_clr, str) : #si la couleur n'est pas une str
            raise TypeError("Un pion doit être Noir : 'N' ou Blanc : 'B'")
        else: #la couleur est une str mais n'est ni 'N' ni 'B'
            raise ValueError("Un pion doit être Noir : 'N' ou Blanc : 'B'")


    def tourner(self):
        if self.couleur == 'N':
            self.couleur = 'B'
        else:
            self.couleur = 'N'


class joueur(object):
    
    def __init__(self, clr, plateau):
        self.couleur = clr
        self.limite = plateau.perimetre
        self.table = plateau
    
    @property
    def couleur(self):
        return self.__couleur

    @couleur.setter
    def couleur(self, nvlle_clr):
        if nvlle_clr in ['N', 'B']:
            self.__couleur = nvlle_clr
        elif not isinstance(nvlle_clr, str) : #si la couleur n'est pas une str
            raise TypeError("Un joueur doit être Noir : 'N' ou Blanc : 'B'")
        else: #la couleur est une str mais n'est ni 'N' ni 'B'
            raise ValueError("Un joueur doit être Noir : 'N' ou Blanc : 'B'")

    def retourner(self, case):
        '''Fonction qui retourne les pions à retourner après avoir joué
        dans une case.

        Entrée
        ------
        case (couple)
        '''

        validite, retournable = self.table.coupValide(case,self.couleur)

        if validite:
            self.table[case] = pion(self.couleur)

            for couple in retournable:
                self.table[couple].tourner() #retourner les pions
        else :
            raise ValueError("La case doit être jouable")


    

class humain(joueur):
    '''Joueur humain auquel on demande où il veut jouer'''

    def jouer(self):
        '''Fonction qui permet à chaque joueur de choisir où jouer'''

        case = input("Case où jouer : ")
        if case == 'q': #afin de pouvoir arrêter le script
            sys.exit("Programme stoppé par l'utilisateur")
        else:
            case = inputtotuple(case)

        self.retourner(case)
   

class IAalea(joueur):
    '''IA qui joue au hasard parmi les cases jouables'''

    def jouer(self):
        coords = self.table.listeValide(self.couleur)
        position = choice(coords)
        
        self.retourner(position)

class IAmax(joueur):
    '''IA qui joue à chaque tour le coup qui va lui rapporter le plus à ce
    tour-ci '''

    def jouer(self):
        coup_maxi = ((None, None), 0)
        for i in range(self.table.perimetre):
            for j in range(self.table.perimetre):
                score = len(self.table.coupValide((i,j),self.couleur)[1])
                if score > coup_maxi[1]:
                    coup_maxi = ((i,j), score)
        self.retourner(coup_maxi[0]) 
