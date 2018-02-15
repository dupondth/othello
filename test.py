#!/usr/bin/python3
#coding:utf8

import unittest
import plateau as p

class testPion(unittest.TestCase):
    def testCouleur(self):
        pionN1 = p.pion('N')
        pionN2 = p.pion('N')
        pionB1 = p.pion('B')
        pionB2 = p.pion('B')

        #Vérification que l'initialisation se passe bien
        self.assertEqual(pionN1.couleur, 'N')
        self.assertEqual(pionN2.couleur, 'N')
        self.assertEqual(pionB1.couleur, 'B')
        self.assertEqual(pionB2.couleur, 'B')

        #Vérification de l'affectation d'une couleur par décorateur
        pionN1.couleur = 'B'
        self.assertEqual(pionN1.couleur, 'B')
        pionB1.couleur = 'N'
        self.assertEqual(pionB1.couleur, 'N')

        #Vérification qu'on ne peut avoir que 'N' et 'B' comme couleur
        with self.assertRaises(ValueError):
            p.pion(3)
            p.pion('C')

    def testTourner(self):
        #Vérification que tourner() change bien la couleur des pions
        pionB = p.pion('B')
        pionN = p.pion('N')

        pionB.tourner()
        pionN.tourner()
        self.assertEqual(pionB.couleur, 'N')
        self.assertEqual(pionN.couleur, 'B')


if __name__ == '__main__' :
    unittest.main()
