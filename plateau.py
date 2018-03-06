#!/usr/bin/python3
#coding:utf8

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
   

class plateau(dict): #le plateau est un dictionnaire
    def __init__(self):
        self.perimetre = 8   #plateau carré de 8 par 8
   
    def coupValide(self, case_depart, couleur_joueur): 
        atourner = list() #Liste des pions à retourner
        valide = False #le coup n'est pas valide par défaut
        
        for direct in range(8): #on cherche dans les 8 directions
            fini = False
            #on ne s'arrete pas de chercher tant que fini n'est pas vrai
            tour1 = True #pour savoir si on est au 1er tour ou pas
            pos = case_depart

            atourner_temp = list() #Sera ajoutée à atourner si la direction est
                                   #validée

            while not fini:
                pos = increment(direct, pos)
                
                if tour1:
                    if pos in self and self[pos].couleur != couleur_joueur: 
                    #on se sert de l'évaluation paresseuse pour ne pas 
                    #avoir d'erreur
                        tour1 = False 
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
                
            
    def __str__(self):
        
        s = str() #la chaîne de caractères que l'on affichera

        for i in range(self.perimetre):
            for j in range(self.perimetre):
                
                if (i,j) in self: #s'il y a un pion à cette position
                    s += self[(i,j)].couleur #on récupère la couleur du pion
                else :
                    s += '.'
            s += '\n' #passage à la ligne suivante

        return s

    def affichage(self, couleur_joueur):
        
        s = str() #la chaîne de caractères que l'on affichera

        for i in range(self.perimetre):
            for j in range(self.perimetre):
                
                if (i,j) in self: #s'il y a un pion à cette position
                    s += self[(i,j)].couleur #on récupère la couleur du pion

                #on vérifie que le coup est valide pour savoir où jouer
                elif self.coupValide((i,j), couleur_joueur)[0]:
                    s += str(len(self.coupValide((i,j), couleur_joueur)[1])) 
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
        self.score = 0
        self.limite = plateau.perimetre
    
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

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, nv_score):
        if nv_score >= 0:
            self.__score = nv_score
        else:
            raise ValueError('Le score doit être positif')

    def jouer(self, case):
        plateau.coupValide(case, self.couleur)
