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

# l'approche par héritage simple de la classe QMainWindow (même type de notre
# fenêtre créée avec QT Designer. Nous configurons après l'interface
# utilisateur dans le constructeur (la méthode init()) de notre classe

class MonAppli(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        # Configuration de l'interface utilisateur.
        self.ui = Ui_principale_ihm()
        self.ui.setupUi(self)

        # Liens entre boutons et fonctions
        self.ui.bouton_depart.clicked.connect(self.jeu_graphique)
        self.ui.bouton_reset.clicked.connect(self.generer)
        
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
        self.ui.centralwidget.repaint()

    def drawPlateau(self, qpainter):
        # pour tracer dans le widget
        self.painter.begin(self.ui.conteneur)
        qp = self.painter

        for position in self.plateau_jeu:
            if self.plateau_jeu[position].couleur == 'N':
                # setBrush pour des disques et non des cercles
                qp.setBrush(QtCore.Qt.black)
                qp.drawEllipse(position[1]*50+5, position[0]*50+4, 40, 40)
            else:
                qp.setBrush(QtCore.Qt.white)
                qp.drawEllipse(position[1]*50+5, position[0]*50+4, 40, 40)
        self.painter.end()
        
    def tour_graphique(self, num_tour, plateau, j1, j2):
        '''Fonction tour() qui prend en charge la mise à jour de l'affichage
        graphique après chaque coup joué par un joueur.'''
    
        print("\n-- Tour " + str(num_tour) + " --")
        print(plateau.affichage(j1.couleur))
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
            
        self.ui.conteneur.repaint()
        print(plateau.affichage(j2.couleur))
        time.sleep(1)
        
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
            
        self.ui.conteneur.repaint()
        print(plateau.affichage(j2.couleur))
        time.sleep(1)
        
        if jouable1 == False and jouable2 == False:
            return False #Arrêter le jeu
        else :
            return True #Continuer le jeu
                    
    def jeu_graphique(self):
        no_tour = 0
        flag = True
        while flag:
            no_tour += 1
            flag = self.tour_graphique(no_tour, self.plateau_jeu, self.joueurN, self.joueurB)
        
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
