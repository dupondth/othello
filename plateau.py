#!/usr/bin/python3
#coding:utf8


class plateau(dict): #le plateau est un dictionnaire
    
    def __init__(self):
        self.perimetre = 8 #plateau carré de 8 par 8


    def affichage(self):
        
        s = str() #la chaîne de caractères que l'on affichera

        for i in range(self.perimetre):
            for j in range(self.perimetre):
                
                if (i,j) in self: #s'il y a un pion à cette position
                    s += self[(i,j)].couleur #on récupère la couleur du pion
                else :
                    s += '.'
            s += '\n' #passage à la ligne suivante


class pion(object):
    
    def __init__(self, clr):
        self.couleur = clr

    @couleur.setter
    def couleur(self, nvlle_clr):
        if nvlle_clr in ['N', 'B']:
            self.__couleur = nvlle_clr
        else :
            raise ValueError('Un pion doit être [N]oir ou [B]lanc')

    @property
    def couleur(self):
        return self.__couleur

    def tourner(self):
        if self.couleur == 'N':
            self.couleur = 'B'
        else:
            self.couleur = 'N'


class joueur(object):
    
    def __init__(self, clr):
        self.couleur = clr
        self.score = 0
    
    @couleur.setter
    def couleur(self, nvlle_clr):
        if nvlle_clr in ['N', 'B']:
            self.__couleur = nvlle_clr
        else:
            raise ValueError('Un joueur doit être [N]oir ou [B]lanc')

    @score.setter
    def score(self, nv_score):
        if nv_score >= 0:
            self.__score = nv_score
        else:
            raise ValueError('Le score doit être positif')

    @property
    def score(self):
        return self.__score
