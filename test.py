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

        positions = [(0,0), (9,2), (3,5), (6,8), (2,3)]
        couleur_pos = ['N', 'B', 'N', 'N', 'B']

        for k in range(len(positions)):
            plat[positions[k]] = p.pion(couleur_pos[k])

        self.assertEqual(plat[(0,0)].couleur, 'N')
        self.assertEqual(plat[(2,3)].couleur, 'B')


    def testAffichage(self):
        plat = p.plateau()

        #Choix de là où veux poser les pions et de leur couleur
        #Les positions en dehors du perimètre ie x ou y >= 7 ne s'affichent pas
        positions = [(0,0), (9,2), (3,5), (6,8), (2,3), (2,4)]
        couleur_pos = ['N', 'B', 'N', 'N', 'B', 'B']

        #Pose des pions
        for k in range(len(positions)):
            plat[positions[k]] = p.pion(couleur_pos[k])

        #On fait la représentation à la main
        representation = ' ABCDEFGH\n' + \
                         '1N.......\n' + \
                         '2........\n' + \
                         '3...BB...\n' + \
                         '4...BNN..\n' + \
                         '5...NB...\n' + \
                         '6........\n' + \
                         '7........\n' + \
                         '8........\n'

        representationN = '\nTour du joueur Noir'+'\n' + \
                          ' ABCDEFGH\n' + \
                          '1N.......\n' + \
                          '2..###...\n' + \
                          '3...BB...\n' + \
                          '4..#BNN..\n' + \
                          '5...NB#..\n' + \
                          '6...##...\n' + \
                          '7........\n' + \
                          '8........\n'

        representationB = '\nTour du joueur Blanc'+'\n' + \
                          ' ABCDEFGH\n' + \
                          '1N.......\n' + \
                          '2........\n' + \
                          '3...BB.#.\n' + \
                          '4...BNN#.\n' + \
                          '5..#NB##.\n' + \
                          '6...#....\n' + \
                          '7........\n' + \
                          '8........\n'



        #On regarde que les deux concordes
        self.assertEqual(str(plat), representation)
        self.assertEqual(plat.affichage('N'), representationN)
        self.assertEqual(plat.affichage('B'), representationB)

    def testCoupValide(self):
        plat = p.plateau()

        positions = [(0,0),(0,2),\
                     (1,0),(1,2),(1,3),\
                     (2,0),(2,1),(2,2),(2,3),\
                     (3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),\
                     (4,0),(4,1),(4,2),(4,3),(4,4),(4,5),\
                     (5,0),(5,1),(5,2),(5,3),(5,4),(5,5),\
                     (6,0),(6,1),(6,2),\
                     (7,0),(7,1)]

        couleurs = ['N','B',\
                    'N','B','B',\
                    'N','B','B','B',\
                    'N','B','B','B','B','B','B',\
                    'N','B','B','N','N','B',\
                    'N','N','B','B','B','B',\
                    'N','N','N',\
                    'N','N']
        
        for k in range(len(positions)):
            plat[positions[k]]=p.pion(couleurs[k])

        self.assertEqual((True, [(3,5)]), plat.coupValide((2,6),'N'))
        self.assertEqual((False, []), plat.coupValide((2,7),'N'))

        resultat = plat.coupValide((2,4),'N')
        self.assertEqual((True, {(2,1),(2,2),(2,3),(3,3),(4,2),(3,4)}), \
                         (resultat[0], set(resultat[1])))
                         #on utilise un set pour n'avoir cure de l'ordre
        print(plat.affichage('N'))

        def testJouable(self):
            plat = p.plateau()
    
            positions = [(0,0),(0,2),\
                         (1,0),(1,2),(1,3),\
                         (2,0),(2,1),(2,2),(2,3),\
                         (3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),\
                         (4,0),(4,1),(4,2),(4,3),(4,4),(4,5),\
                         (5,0),(5,1),(5,2),(5,3),(5,4),(5,5),\
                         (6,0),(6,1),(6,2),\
                         (7,0),(7,1)]
    
            couleurs = ['N','B',\
                        'N','B','B',\
                        'N','B','B','B',\
                        'N','B','B','B','B','B','B',\
                        'N','B','B','N','N','B',\
                        'N','N','B','B','B','B',\
                        'N','N','N',\
                        'N','N']
            
            for k in range(len(positions)):
                plat[positions[k]]=p.pion(couleurs[k])
    
            self.assertEqual(plat.jouable('B'), True)
            self.assertEqual(plat.jouable('N'), True)
            
            plat2 = p.plateau()
            for pos in plat2:
                plat2[pos].couleur = 'N'

            self.assertEqual(plat.jouable('B'), False)
            self.assertEqual(plat.jouable('N'), False)

class testFonctions(unittest.TestCase):
    def testIncrement(self):
        #position de départ choisie au hasard
        pos = (2,4)
        
        #test dans toutes les directions (8 directions)
        self.assertEqual(p.increment(0, pos), (1,4))
        self.assertEqual(p.increment(1, pos), (1,5))
        self.assertEqual(p.increment(2, pos), (2,5))
        self.assertEqual(p.increment(3, pos), (3,5))
        self.assertEqual(p.increment(4, pos), (3,4))
        self.assertEqual(p.increment(5, pos), (3,3))
        self.assertEqual(p.increment(6, pos), (2,3))
        self.assertEqual(p.increment(7, pos), (1,3))

    def testInput(self):
        self.assertEqual(p.inputtotuple('d2'),(1,3))
        self.assertEqual(p.inputtotuple('a1'),(0,0))
            
class testJoueur(unittest.TestCase):
    def testInit(self):
        plat = p.plateau()
        jN = p.joueur('N', plat)
        jB = p.joueur('B', plat)

        #Vérification de l'initialisation de couleur
        self.assertEqual(jN.couleur, 'N')
        self.assertEqual(jB.couleur, 'B')
        
        jN.couleur = 'B'
        self.assertEqual(jN.couleur, 'B')

        with self.assertRaises(ValueError):
            jN = p.joueur('Q', plat)

        with self.assertRaises(TypeError):
            jN = p.joueur(2, plat)

        #Vérification des limites
        self.assertEqual(jN.limite, plat.perimetre)
        self.assertEqual(jB.limite, plat.perimetre)

        #Vérification de l'initialisation du score
        self.assertEqual(plat.diff_score(jN.couleur), 0)
        self.assertEqual(plat.diff_score(jB.couleur), 0)
        
        #Vérification qu'un simple objet joueur ne peut pas jouer
        with self.assertRaises(AttributeError):
            jN.jouer((1,1))

    def testRetourner(self):
        plat = p.plateau()
        jN = p.joueur('N', plat)
        
        jN.retourner((3,2), plat, jN.couleur)
        self.assertEqual(plat[(3,2)].couleur,'N') #la case jouée
        self.assertEqual(plat[(3,3)].couleur,'N') #la case retournée
        
    def testSimuler(self):
        plat = p.plateau()
        jN = p.joueur('N', plat)
        table_copie = jN.simuler((3,2), plat, jN.couleur)
        
        #On vérifie que les modifications faites dans le plateau copié
        #n'affecte pas le vrai plateau
        self.assertNotEqual(plat, table_copie)

if __name__ == '__main__' :
    unittest.main()
