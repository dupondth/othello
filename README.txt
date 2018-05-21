    ___  _   _        _ _     
   / _ \| |_| |_  ___| | |___ 
  | (_) |  _| ' \/ -_) | / _ \
   \___/ \__|_||_\___|_|_\___/

Projet Othello : comment lancer le jeu

* applicationIHM.py lance l'interface graphique générée sous QtDesigner où l'on peut choisir le mode de jeu et la difficulté de l'IA s'il y a lieu.
* interface.py est le fichier issu de QtDesigner.
* jouer.py contient les fonctions nécessaires au déroulement du jeu en mode console.
* plateau.py contient les objets et méthodes nécessaires au fonctionnement du jeu.


Interface graphique

* Plateau :
    * Pions : Les pions sont représentés par des disques de couleur adéquate.
    * Cases jouables : Ces cases sont mises en valeur par la présence d'un disque vert clair.

* Boutons :
    * Début simulation : Disponible seulement en mode IA vs IA, lance une partie entre les deux IA.
    * Recommencer : Remets à zéro le plateau. Il est nécessaire d'appuyer sur ce bouton après avoir changé de mode de jeu.

* Mode IA vs IA : Ce mode commence par le choix du niveau de chaque IA (Facile : IA aléatoire, Normal : IA maximise ses gains sur un tour, Difficile : IA min max sur un tour, Très difficile : IA min max sur deux tours). Puis la partie se lance avec le bouton "Début simulation".

* Mode Joueur vs IA : Le joueur humain joue toujours les pions noirs. Ce mode commence après un clic de la part du joueur humain sur une des cases jouables.

* Mode Joueur vs Joueur : Chaque joueur appuie sur une des cases jouables, chacun son tour.
