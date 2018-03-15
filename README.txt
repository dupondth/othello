Projet Othello : comment lancer le jeu

jouer.py contient les fonctions nécessaires au déroulement du jeu alors que
plateau.py contient les objets et méthodes nécessaires au fonctionnement du jeu.

Le jeu se lance en éxecutant le fichier jouer.py qui fait appel au fichier
plateau.py.

Pour jouer humain contre IA : 
    Dans jouer.py : décommenter les lignes 131 à 141. Dans la ligne 133, p.IAmax
    peut être remplacé par p.IAalea pour jouer contre une IA qui joue au hasard.
    Le jeu peut être stoppé à tout moment par l'humain lors de son choix de case
    en entrant la lettre q.

Pour jouer N parties IA contre IA:
    Dans jouer.py : décommenter les lignes 147 et 148 puis changer la valeur de
    N ligne 147 pour jouer N parties. Le choix des IA qui s'affrontent se fait
    dans la fonction stats_jeux dans le même fichier : lignes 112 et 113. p.IAlea
    peut être remplacé par p.IAmax et inversement.
