#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2018

@author: toumiab
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from interface import Ui_principale_ihm
import jouer as j
import plateau as p

# l'approche par héritage simple de la classe QMainWindow (même type de notre
# fenêtre créée avec QT Designer. Nous configurons après l'interface
# utilisateur dans le constructeur (la méthode init()) de notre classe

class MonAppli(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        # Configuration de l'interface utilisateur.
        self.ui = Ui_principale_ihm()
        self.ui.setupUi(self)
        
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("plateau.png")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.ui.conteneur.lower()
        self.ui.conteneur.stackUnder(self)
        self.ui.conteneur.setAutoFillBackground(True)
        self.ui.conteneur.setPalette(palette)
        
        self.generer()

    def generer(self):
        self.plateau_jeu = p.plateau()
        self.joueurN = p.IAalea('N', self.plateau_jeu)
        self.JoueurB = p.IAalea('B', self.plateau_jeu)
        self.ui.centralwidget.update()

    def paintEvent(self, j):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPlateau(qp) # une méthode à définir
        qp.end()
              
    def drawPlateau(self, qpainter):

        for couple in self.plateau_jeu:
            if couple[1].couleur == 'N':
                qpainter.setPen(QtCore.Qt.black)
                qpainter.drawEllipse(
                
    def jeu_graphique(self, j):
        pass        
            
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
