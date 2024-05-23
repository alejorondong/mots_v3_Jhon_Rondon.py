import random  # Importe le module random pour sélectionner un mot aléatoire
import unicodedata  # Importe le module unicodedata pour normaliser les accents


# Définit une fonction pour sélectionner un mot aléatoire depuis un fichier
def selectionner_mot_aleatoire(nom_fichier):
    with open(nom_fichier, 'r') as fichier:  # Ouvre le fichier en mode lecture
        mots = fichier.readlines()  # Lit toutes les lignes du fichier et les stocke dans une liste
    return random.choice(mots).strip()  # Sélectionne un mot aléatoire et supprime les espaces blancs


# Définit une fonction pour enlever les accents des lettres
def enlever_accents(texte):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texte)
        if unicodedata.category(c) != 'Mn'
    )


# Définit une fonction pour afficher l'état actuel du mot avec des tirets bas pour les lettres non devinées
def afficher_etat_mot(mot, lettres_devinees):
    etat = ''.join([lettre if enlever_accents(lettre) in lettres_devinees else '_' for lettre in
                    mot])  # Crée une chaîne avec les lettres devinées et des tirets bas
    return etat  # Retourne l'état actuel du mot


# Définit la fonction principale du jeu
def jeu_deviner_mot():
    while True:  # Boucle principale pour permettre de rejouer
        print("Bienvenue au jeu de devinettes de mots !")
        print("Vous devez deviner les lettres d'un mot sélectionné aléatoirement.")
        print("Vous avez 6 tentatives pour deviner le mot complet.")

        choix_fichier = input(
            "Choisissez une option :\n1. Jouer avec le fichier par défaut (mots.txt)\n2. Fournir votre propre fichier\nEntrez 1 ou 2 : ").strip()
        if choix_fichier == '2':
            nom_fichier = input("Veuillez entrer le nom de votre fichier (y compris l'extension .txt et doit être dans le meme dossier) : ").strip()
        else:
            nom_fichier = 'mots.txt'

        mot = selectionner_mot_aleatoire(nom_fichier)  # Sélectionne un mot aléatoire depuis le fichier
        mot_sans_accents = enlever_accents(mot)  # Crée une version du mot sans accents
        tentatives_restantes = 6  # Définit le nombre initial de tentatives
        lettres_devinees = set()  # Crée un ensemble pour stocker les lettres devinées par l'utilisateur
        aide_utilisee = False  # Indicateur pour savoir si l'aide a été utilisée

        print("Le jeu commence maintenant ! Bonne chance !")  # Message de début du jeu

        # Boucle principale du jeu qui s'exécute tant qu'il reste des tentatives
        while tentatives_restantes > 0:
            etat_actuel = afficher_etat_mot(mot, lettres_devinees)  # Obtient l'état actuel du mot
            print(f"État actuel du mot : {etat_actuel}")  # Affiche l'état actuel du mot

            # Vérifie si l'utilisateur a deviné toutes les lettres du mot
            if '_' not in etat_actuel:
                print("Félicitations, vous avez gagné !")  # Message de victoire
                break  # Quitte la boucle car l'utilisateur a gagné

            # Aider l'utilisateur avec une lettre si c'est la dernière tentative et que l'aide n'a pas encore été utilisée
            if tentatives_restantes == 1 and not aide_utilisee:
                lettres_non_devinees = [lettre for lettre in mot_sans_accents if
                                        enlever_accents(lettre) not in lettres_devinees]
                if lettres_non_devinees:
                    lettre_aider = random.choice(lettres_non_devinees)
                    print(f"Aide : Voici une lettre pour vous aider : {lettre_aider}")
                    aide_utilisee = True  # Marque que l'aide a été utilisée

            lettre = input(
                "Entrez une lettre : ").lower().strip()  # Demande à l'utilisateur de saisir une lettre et la convertit en minuscule
            lettre_sans_accents = enlever_accents(lettre)  # Enlève les accents de la lettre saisie

            # Vérifie si la lettre a déjà été devinée
            if lettre_sans_accents in lettres_devinees:
                print(
                    "Vous avez déjà deviné cette lettre. Essayez une autre.")  # Informe l'utilisateur que la lettre a déjà été devinée
                continue  # Continue avec l'itération suivante de la boucle

            lettres_devinees.add(lettre_sans_accents)  # Ajoute la lettre sans accents à l'ensemble des lettres devinées

            # Vérifie si la lettre sans accents est dans le mot sans accents
            if lettre_sans_accents in mot_sans_accents:
                print("Bien joué ! La lettre est dans le mot.")  # Informe l'utilisateur que la lettre est dans le mot
            else:
                tentatives_restantes -= 1  # Réduit le nombre de tentatives restantes de 1
                print(
                    f"Désolé, la lettre n'est pas dans le mot. Il vous reste {tentatives_restantes} tentatives.")  # Informe l'utilisateur que la lettre n'est pas dans le mot et affiche les tentatives restantes

            # Vérifie si l'utilisateur a épuisé toutes les tentatives
            if tentatives_restantes == 0:
                print(f"Vous avez perdu. Le mot était : {mot}")  # Message de défaite avec le mot correct

        # Demande à l'utilisateur s'il veut rejouer
        rejouer = input("Voulez-vous jouer à nouveau ? (oui/non) : ").lower().strip()
        if rejouer != 'oui':
            print("Merci d'avoir joué ! Au revoir.")
            break  # Quitte la boucle principale et termine le jeu


# Exécute la fonction principale du jeu lorsque le script est exécuté directement
if __name__ == "__main__":
    jeu_deviner_mot()  # Appelle la fonction principale du jeu
