Présentation du code

Ce code est un jeu de devinettes de mots dans lequel l'utilisateur doit deviner un mot sélectionné au hasard dans un fichier texte. Le jeu commence par 6 tentatives pour deviner toutes les lettres du mot. L'utilisateur peut choisir de jouer avec le fichier par défaut (mots.txt) ou de fournir son propre fichier Word. Si rutilasteis a une dernière chance de deviner et n'a pas encore utilisé l'aide, il recevra une lettre pour l'aider. A la fin du jeu, l'utilisateur a la possibilité de rejouer.

Sources de mots à deviner

Fichier par défaut (mots.txt) : Il s'agit du fichier par défaut qui contient une liste de mots, chacun sur une ligne distincte.
Fichier fourni par l'utilisateur : l'utilisateur peut choisir de fournir son propre fichier texte contenant une liste de mots.

Objectif de chaque procédure

selectionner\_mot\_aleatoire(nom du fichier)
Objectif : Sélectionner un mot aléatoire dans un fichier texte.
Comment ça marche : ouvrez le fichier, lisez toutes les lignes d'une liste, choisissez une ligne au hasard et supprimez les espaces de début et de fin.

enlever\_accents(texte)
Objectif : Normaliser une chaîne de texte en supprimant les accents des lettres.
Comment ça marche : utilise la normalisation Unicode pour décomposer les caractères accentués et supprime les composants accentués.

afficher\_etat\_mot(mot, lettres\_devinees)
Objectif : Afficher l'état actuel du mot avec des traits de soulignement pour les lettres non devinées.
Comment ça marche : Il parcourt chaque lettre du mot et affiche la lettre si elle a été devinée, sinon il affiche un trait de soulignement.

jeu\_deviner\_mot()
Objectif : Exécuter la logique principale du jeu.
Fonctionnement :
Accueille l'utilisateur et donne une brève description du jeu.
Permet à l'utilisateur de choisir entre le fichier par défaut ou de fournir son propre fichier.
Sélectionnez un mot aléatoire dans le fichier choisi.
Initialise les variables pour le nombre d'essais restants et les lettres devinées.
Exécutez une boucle principale où :
Affiche l'état actuel du mot.
Permet à l'utilisateur de saisir une lettre.
Vérifiez si la lettre a déjà été devinée.
Met à jour les lettres devinées et le nombre de tentatives restantes.
Fournit une lettre d'aide si l'utilisateur a encore une dernière chance et n'a pas utilisé l'aide.
Détermine si l'utilisateur a gagné ou perdu et affiche le message correspondant.
Demandez à l'utilisateur s'il souhaite rejouer.
