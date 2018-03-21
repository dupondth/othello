#!/usr/bin/python3
#coding:utf8

import sys
from random import choice
import copy

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

    def evaluation(self, couleur_joueur):
        '''Fonction d'évaluation du jeu pour une couleur de joueur.
        Renvoie le nombre de pions du joueur couleur_joueur auquel on soustrait
        nombre de pions de l'adversaire.

        Entrées
        -------
        couleur ('N' ou 'B') : couleur du joueur

        Sortie
        ------
        valeur (int)
        '''
        valeur = 0

        for pion in self:
            if pion.couleur == couleur_joueur:
                valeur += 1
            else :
                valeur -= 1

        return valeur
                

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

        if not( 0 <= case_depart[0] < self.perimetre) or not( 0 <=
        case_depart[1] < self.perimetre):
        #Vérification que la position est bien dans le plateau
            return(valide, atourner)

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

    def retourner(self, case, plateau):
        '''Fonction qui retourne les pions à retourner après avoir joué
        dans une case.

        Entrée
        ------
        case (couple)
        '''

        validite, retournable = plateau.coupValide(case,self.couleur)

        if validite:
            plateau[case] = pion(self.couleur)

            for couple in retournable:
                plateau[couple].tourner() #retourner les pions
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

        self.retourner(case, self.table)
   

class IAalea(joueur):
    '''IA qui joue au hasard parmi les cases jouables'''

    def jouer(self):
        coords = self.table.listeValide(self.couleur)
        position = choice(coords)
        
        self.retourner(position, self.table)

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
        self.retourner(coup_maxi[0], self.table) 

class IAminmax(joueur):
    '''IA qui applique l'algorithme minmax: elle choisit le gain maximum où
    gain = (pions gagnés au tour 1) - (pions gagnés par l'adversaire au tour 2)
    + (pions gagnés au tour 3)'''
    
    def couleur_adv(self):
        if self.couleur == 'B':
            return 'N'
        else:
            return 'B'
    
    def jouer(self):
        
        coords_gains = dict()
        
        for i in range(self.limite):
            for j in range(self.limite):
                if self.table.coupValide((i,j),self.couleur)[0]:
                #si la case est jouable
                    table_copy = copy.copy(self.table)
                    self.retourner((i,j), table_copy) #on joue sur (i,j)
                    print('case jouable : ', (i,j))
                    print('table copiée : \n', table_copy)
                    print('vraie table : \n', self.table)
                    poids = -float('Inf') #poids de notre coup en (i,j)
                
                    for k in range(self.limite):
                        for l in range(self.limite):
                            if table_copy.coupValide((k,l),self.couleur_adv())[0]:
                                table_copy2 = copy.copy(table_copy)
                                self.retourner((k,l), table_copy2) #l'adversaire joue sur (k,l)
                        
                                score = float('Inf') #poids d'un coup de l'adversaire en (k,l)
                        
                                for m in range(self.limite):
                                    for n in range(self.limite):
                                        if table_copy2.coupValide((m,n),self.couleur)[0]:
                                            table_copy3 = copy.copy(table_copy2)
                                            self.retourner((m,n), table_copy3) #on joue sur (m,n)
                                
                                            evaluation = table_copy3.evaluation()
                                
                                            if evaluation < score:
                                                score = evaluation
                                                #on garde l'évaluation la plus défavorable
                                                #parmi toutes les évaluations possibles.
                                                
                                            #si aucun coup du joueur n'est simulable, 
                                            #score reste à +inf.
                                    
                                if score > poids:
                                    poids = score
                                    
                                #si aucun coup de l'adversaire n'est simulable, 
                                #poids reste à -inf.
                            
                    coords_gains[(i,j)] = poids 
                    #on donne un poids à chacun de nos coup.
                
                    #si aucun coup du joueur n'est valide, le dictionnaire reste vide.
                
        print(coords_gains)
        print(sorted(coords_gains.items(), key=lambda t:t[1], reverse=True))
        print(sorted(coords_gains.items(), key=lambda t:t[1], reverse=True)[0][0])
        print(self.table)
        self.retourner(sorted(coords_gains.items(), key=lambda t:t[1], reverse=True)[0][0], self.table)
        #la commande sorted(...) rend [((case1),poids1),((case2),poids2)] triée selon le poids par ordre décroissant.
                                                      
    """def jouer2(self):
        liste_case = self.table.listeValide(self.couleur)
        ##à quoi sert cette liste ?
        
        #print('cases jouables IA : ', liste_case)
        
        coords_gains_IA =list()
        #liste des listes [case jouable, gain pour la case] pour l'IA
        #gain = nombre de pions adverses retournés
        ##À changer car listeValide parcours une fois la grille en entier et on
        ##recommence avec ce for là donc pas opti
        for coup_jouable in self.table.listeValide(self.couleur):
            coords_gains_IA.append([coup_jouable, len(self.table.coupValide(coup_jouable, self.couleur)[1])])
            #à chaque case jouable on associe le nombre de pions gagnés
            #par l'IA. De la forme [[(a,b),x],[(c,d),y],[(e,f),z]]
        
        #print('coords et gains associés IA : ', coords_gains_IA)
            
        gains_adv = list()
        #liste de sous-listes. Chaque sous-liste correspond à une case jouée
        #par l'IA et contient la liste des gains possibles de l'adversaire.
       
        ##pourquoi ne pas utiliser liste_case ?
        for coup_jouable in self.table.listeValide(self.couleur):
            table_copy = copy.deepcopy(self.table)
            #on copie la table pour y simuler tous les coups possibles de l'IA.
            #on utilise copy pour que les simulations ne se propagent pas
            ##^ ça ne veut rien dire
            table_copy[coup_jouable] = pion(self.couleur)
            retournable = table_copy.coupValide(coup_jouable,self.couleur)[1]
            for pos in retournable:
                table_copy[pos].tourner()
            #on simule un coup de l'IA
            
            #print(table_copy.affichage(self.couleur_adv()))
            
            gains_possibles = list()
            if table_copy.jouable(self.couleur_adv()):
                for coup_jouable_adv in table_copy.listeValide(self.couleur_adv()): 
                    gains_possibles.append(len(table_copy.coupValide(coup_jouable_adv, self.couleur_adv())[1])) 
                    #sous-liste des gains possibles pour l'adversaire
            else:
                gains_possibles.append(0)
                
            #print('gains possibles adv pour le coup : ', gains_possibles)
                
            gains_adv.append(gains_possibles)
            #de la forme [[a,b,c],[d,e],[i,j,k,l,m]]    
       
        #print('gains possibles adversaires : ', gains_adv) 
            
        poids = list()
        for i in range(len(coords_gains_IA)):
            poids_coup_i = list()
            for j in range(len(gains_adv[i])):
                poids_coup_i.append(coords_gains_IA[i][1] - gains_adv[i][j])
                #de la forme [x-a,x-b,x-c]
            poids.append(poids_coup_i)
            #de la forme [[x-a,x-b,x-c],[y-d,y-e],[z-i,z-j,z-k,z-l,z-m]]
            #avec x,y,z les gains possibles selon les coups de l'IA
            
        #print('poids : ', poids)
            
        poids_trie = list()
        for i in range(len(poids)):
            poids_trie.append(sorted(poids[i]))
        #on trie les sous-listes : les gains minimals se retrouvent en 1ere
        #position dans chaque sous-liste. Il faut identifier lequel est le
        #plus grand, et remonter à la position correspondante.
        
        #print('poids triés : ', poids_trie)
         
        indice_pos_opt = 0
        gain_min = poids_trie[0][0]
        for i in range(len(poids_trie)):
            if gain_min < poids_trie[i][0]:
                gain_min = poids_trie[i][0]
                indice_pos_opt = i
        
        #print('indice position optimisée : ', indice_pos_opt)
        
        pos_opt = liste_case[indice_pos_opt]
        
        #print('position optimisée : ', pos_opt)
        
        self.retourner(pos_opt)"""
