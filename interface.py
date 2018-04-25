#! /usr/bin/python3
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
        principale_ihm.resize(900, 900)
        self.centralwidget = QtWidgets.QWidget(principale_ihm)
        self.centralwidget.setObjectName("centralwidget")
        self.conteneur = QtWidgets.QWidget(self.centralwidget)
        self.conteneur.setGeometry(QtCore.QRect(10, 30, 800, 800))
        self.conteneur.setObjectName("conteneur")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(820, 30, 77, 120))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bouton_dep = QtWidgets.QPushButton(self.widget)
        self.bouton_dep.setObjectName("bouton_dep")
        self.verticalLayout.addWidget(self.bouton_dep)
        spacerItem = QtWidgets.QSpacerItem(68, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.bouton_quit = QtWidgets.QPushButton(self.widget)
        self.bouton_quit.setObjectName("bouton_quit")
        self.verticalLayout.addWidget(self.bouton_quit)
        principale_ihm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(principale_ihm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 19))
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
        self.bouton_dep.setText(_translate("principale_ihm", "Départ"))
        self.bouton_quit.setText(_translate("principale_ihm", "Quitter"))
        self.menuFIchiers.setTitle(_translate("principale_ihm", "Fichiers"))
        self.actionQuitter.setText(_translate("principale_ihm", "Quitter"))
        self.actionQuitter.setShortcut(_translate("principale_ihm", "Ctrl+Q"))

