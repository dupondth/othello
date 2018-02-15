#!/usr/bin/python3
#coding:utf8

import unittest
import plateau as p
import random as rn

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
            p.pion('C')

        #Notamment pas quelque chose d'autre qu'une str
        with self.assertRaises(TypeError):
            p.pion(3)

    def testTourner(self):
        #Vérification que tourner() change bien la couleur des pions
        pionB = p.pion('B')
        pionN = p.pion('N')

        pionB.tourner()
        pionN.tourner()
        self.assertEqual(pionB.couleur, 'N')
        self.assertEqual(pionN.couleur, 'B')


class testPlateau(unittest.TestCase):
    def testInit(self):
        plat = p.plateau()
        self.assertEqual(plat.perimetre, 8)

    def testAffichage(self):
        plat1 = p.plateau()

        #Choix de là où veux poser les pions et de leur couleur
        #Les positions en dehors du perimètre ie x ou y >= 7 ne s'affichent pas
        positions = [(0,0), (9,2), (3,5), (6,8), (2,3)]
        couleur_pos = ['N', 'B', 'N', 'N', 'B']

        #Pose des pions
        for k in range(len(positions)):
            plat1[positions[k]] = p.pion(couleur_pos[k])

        #On fait la représentation à la main
        representation = 'N.......\n' + \
                         '........\n' + \
                         '...B....\n' + \
                         '.....N..\n' + \
                         '........\n' + \
                         '........\n' + \
                         '........\n' + \
                         '........\n'

        #On regarde que les deux concordes
        self.assertEqual(str(plat1), representation)


class testFonctions(unittest.TestCase):
    def testIncrement(self):
        #position de départ choisie au hasard
        pos = (2,4)

        self.assertEqual(p.increment(0, pos), (1,4))
        self.assertEqual(p.increment(1, pos), (1,5))
        self.assertEqual(p.increment(2, pos), (2,5))
        self.assertEqual(p.increment(3, pos), (3,5))
        self.assertEqual(p.increment(4, pos), (3,4))
        self.assertEqual(p.increment(5, pos), (3,3))
        self.assertEqual(p.increment(6, pos), (2,3))
        self.assertEqual(p.increment(7, pos), (1,3))
            



if __name__ == '__main__' :
    unittest.main()
