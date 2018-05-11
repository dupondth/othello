# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './interface.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_principale_ihm(object):
    def setupUi(self, principale_ihm):
        principale_ihm.setObjectName("principale_ihm")
        principale_ihm.resize(557, 489)
        self.centralwidget = QtWidgets.QWidget(principale_ihm)
        self.centralwidget.setObjectName("centralwidget")
        self.conteneur = QtWidgets.QWidget(self.centralwidget)
        self.conteneur.setGeometry(QtCore.QRect(10, 30, 400, 400))
        self.conteneur.setObjectName("conteneur")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(420, 30, 131, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mode_jeu = QtWidgets.QComboBox(self.layoutWidget)
        self.mode_jeu.setObjectName("mode_jeu")
        self.mode_jeu.addItem("")
        self.mode_jeu.addItem("")
        self.mode_jeu.addItem("")
        self.verticalLayout.addWidget(self.mode_jeu)
        self.bouton_depart = QtWidgets.QPushButton(self.layoutWidget)
        self.bouton_depart.setObjectName("bouton_depart")
        self.verticalLayout.addWidget(self.bouton_depart)
        self.bouton_reset = QtWidgets.QPushButton(self.layoutWidget)
        self.bouton_reset.setObjectName("bouton_reset")
        self.verticalLayout.addWidget(self.bouton_reset)
        spacerItem = QtWidgets.QSpacerItem(68, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.bouton_quit = QtWidgets.QPushButton(self.layoutWidget)
        self.bouton_quit.setObjectName("bouton_quit")
        self.verticalLayout.addWidget(self.bouton_quit)
        principale_ihm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(principale_ihm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 19))
        self.menubar.setObjectName("menubar")
        self.menuFIchiers = QtWidgets.QMenu(self.menubar)
        self.menuFIchiers.setObjectName("menuFIchiers")
        principale_ihm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(principale_ihm)
        self.statusbar.setObjectName("statusbar")
        principale_ihm.setStatusBar(self.statusbar)
        self.actionQuitter = QtWidgets.QAction(principale_ihm)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuFIchiers.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFIchiers.menuAction())

        self.retranslateUi(principale_ihm)
        self.actionQuitter.triggered.connect(principale_ihm.close)
        self.bouton_quit.clicked.connect(principale_ihm.close)
        QtCore.QMetaObject.connectSlotsByName(principale_ihm)

    def retranslateUi(self, principale_ihm):
        _translate = QtCore.QCoreApplication.translate
        principale_ihm.setWindowTitle(_translate("principale_ihm", "Othello"))
        self.mode_jeu.setItemText(0, _translate("principale_ihm", "IA vs IA"))
        self.mode_jeu.setItemText(1, _translate("principale_ihm", "Joueur vs IA"))
        self.mode_jeu.setItemText(2, _translate("principale_ihm", "Joueur vs Joueur"))
        self.bouton_depart.setText(_translate("principale_ihm", "Départ"))
        self.bouton_reset.setText(_translate("principale_ihm", "Recommencer"))
        self.bouton_quit.setText(_translate("principale_ihm", "Quitter"))
        self.menuFIchiers.setTitle(_translate("principale_ihm", "Fichiers"))
        self.actionQuitter.setText(_translate("principale_ihm", "Quitter"))
        self.actionQuitter.setShortcut(_translate("principale_ihm", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    principale_ihm = QtWidgets.QMainWindow()
    ui = Ui_principale_ihm()
    ui.setupUi(principale_ihm)
    principale_ihm.show()
    sys.exit(app.exec_())

