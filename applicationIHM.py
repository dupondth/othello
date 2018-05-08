#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2018

@author: toumiab
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from interface import Ui_principale_ihm
import jouer
import plateau as p
import time
import ipdb

#les noirs commencent
CLR_JOUEUR = 'N'
POS = (None, None) #position choisie par le joueur

class MonAppli(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        # Configuration de l'interface utilisateur.
        self.ui = Ui_principale_ihm()
        self.ui.setupUi(self)

        # Liens entre boutons et fonctions
        self.ui.bouton_depart.clicked.connect(self.partie)
        self.ui.bouton_reset.clicked.connect(self.generer)
        self.ui.conteneur.mousePressEvent = self.clic
        
        # Image de fond dans le widget principal
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("plateau.png")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.ui.conteneur.lower()
        self.ui.conteneur.stackUnder(self)
        self.ui.conteneur.setAutoFillBackground(True)
        self.ui.conteneur.setPalette(palette)

        # Objet peintre pour les pions
        self.painter = QtGui.QPainter()

        # Mise à jour du widget principal
        self.ui.conteneur.paintEvent = self.drawPlateau
        
        self.generer()

    def generer(self):
        self.plateau_jeu = p.plateau()
        self.joueurN = p.IAalea('N', self.plateau_jeu)
        self.joueurB = p.IAalea('B', self.plateau_jeu)

        CLR_JOUEUR = 'N' # Les noirs commencent
        self.ui.conteneur.repaint()

    def drawPlateau(self, qpainter):
        # pour tracer dans le widget
        self.painter.begin(self.ui.conteneur)
        qp = self.painter

        print(CLR_JOUEUR)

        for position in self.plateau_jeu:
            if self.plateau_jeu[position].couleur == 'N':
                # setBrush pour des disques et non des cercles
                qp.setPen(QtCore.Qt.black)
                qp.setBrush(QtCore.Qt.black)
                qp.drawEllipse(position[1]*50+5, position[0]*50+4, 40, 40)
            else:
                qp.setPen(QtCore.Qt.white)
                qp.setBrush(QtCore.Qt.white)
                qp.drawEllipse(position[1]*50+5, position[0]*50+4, 40, 40)

        for position in self.plateau_jeu.listeValide(CLR_JOUEUR):
            qp.setPen(QtCore.Qt.green)
            qp.setBrush(QtCore.Qt.green)
            qp.drawEllipse(position[1]*50+20, position[0]*50+19, 10, 10)

        self.painter.end()

    def clic(self, event):
        pos = (event.pos().y() // 50, event.pos().x() // 50)
        #faire jouer le tour ICI
        
    def tour(self, num_tour, plateau, j1, j2):
        '''Fonction tour() qui prend en charge la mise à jour de l'affichage
        graphique après chaque coup joué par un joueur.'''
    
        global CLR_JOUEUR

        print("\n-- Tour " + str(num_tour) + " --")
        CLR_JOUEUR = j1.couleur
        self.ui.conteneur.repaint()
        print(plateau.affichage(j1.couleur))
        time.sleep(0.5)

        jouable1, jouable2 = True, True
    
        #Si le joueur peut jouer, il joue

        if plateau.jouable(j1.couleur):
            flag1 = True
            while flag1:
                try:
                    j1.jouer()
                    flag1 = False
                except ValueError:
                    print("Veuillez jouer dans une case valide")
        else:
            jouable1 = False
            
        CLR_JOUEUR = j2.couleur
        self.ui.conteneur.repaint()
        print(plateau.affichage(j2.couleur))
        time.sleep(0.5)
        
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
        else : return True #Continuer le jeu
                    

    def partie(self):
        no_tour = 0
        flag = True
        while flag:
            no_tour += 1
            flag = self.tour(no_tour, self.plateau_jeu, self.joueurN, self.joueurB)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
