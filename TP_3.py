"""
wq«tewzyxe
"""

import random

nombre_vie = 0
nombre_adversaire = 0
nombre_victoire = 0
nombre_defaites = 0
nombre_victoire_suivi = 0
force_adversaire = random. randint(1, 6) + random.randint(1, 6)
boucle_jeu = True


def commcencement():
    """
    fonction qui defenie les valeurs du nombre de vie, force adverdaire, nombre de victoire, nombre de defaite,
    nombre de victoire suivie et le nombre d adervsaire au commencemtn du jeu
    """
    global nombre_vie, force_adversaire, nombre_victoire, nombre_defaites, nombre_victoire_suivi, nombre_adversaire
    nombre_vie = 0
    force_adversaire = 0
    nombre_victoire = 0
    nombre_defaites = 0
    nombre_victoire_suivi = 0
    nombre_adversaire = 0


commcencement()

while boucle_jeu:
    # la génération du monstre doit aller ici!
    if nombre_victoire % 3 == 0 and nombre_victoire != 0:
        force_adversaire = random.randint(10, 11)

    else:
        force_adversaire = random.randint(1, 5) + random.randint(1, 5)

    print(f"""votre niveau de vie est {nombre_vie}, 
      votre adveesaire a une force de{force_adversaire}""")
    choix = int(input(f" que voulez vous faire ? \n 1:combattre cet adversaire \n 2:contourner cet adversaire"
              "et ouvrir une autre porte \n 3:afficher les regles du jeu \n 4:quitter la parti"))
    if choix == 1:
        nombre_adversaire = + 1
        print(f"\n adversaire:{nombre_adversaire}")
        print(f"\n force de l'adversaire {force_adversaire}")
        print(f"\n votre nombre de vie {nombre_vie}")
        print(f"combat{nombre_adversaire}:{nombre_victoire} victoire et {nombre_defaites} defaites")
        lancer_de_1 = random.randint(1, 6)
        lancer_de_2 = random.randint(1, 6)
        score_de = lancer_de_1 + lancer_de_2
        print(f"\n premier lancer de de : {lancer_de_1}"
          f"\n deuxime lancer de de: {lancer_de_2}"
          f"\n totale = {score_de}")
        if score_de > force_adversaire:
            resultat_combat= "victoire"
            nombre_victoire_suivi += 1
            nombre_victoire += 1
            nombre_vie += force_adversaire
            print(f"\n dernier combat : {resultat_combat}"
              f"votre nombre de vie : {nombre_vie}"
              f"nombre de victoire : {nombre_victoire_suivi}")

        else:
            resultat_combat = "defaite!"
            nombre_vie -= force_adversaire
            nombre_victoire_suivi = 0
            nombre_defaites += 1
            print(f"dernier combat : {resultat_combat}")

        if nombre_vie > 0:
            print(f"votre niveau de vie: {nombre_vie}")
            force_adversaire = random.randint(1, 5) + random.randint(1, 5)

        else:
            print(f"\n votre partie est terminee, votre nombre de victoire est {nombre_victoire} monstres"
                  f"A bientot!")

    elif choix == 2:
        nombre_vie -= 1
        print("En contournat le monstre, vous avez perdu une vie. "
              f"\n votre nombre de vie est maintenant : {nombre_vie}")

    elif choix == 3:
        print("\n afin de reussir a gagne un combat, il faut que la valeurt des 2 lancer de de est superieure a"
              "l adversaire"
              "\n lors d une victoire, la vie du joueur augmente par la force de l adversaire"
              "\n une defaite est cree la valeurs des 2 lancer de de est inferieure a l adversaire"
              "\n lors d une defaite, la vie du joueur diminue par la force de l adevrsaire"
              "\n l usager a le choix de combattre ou eviter l adervsaire, si il l evitre, il perd 1 point de vie ")
    else:
        print("Merci, passer une bonne journee!")
        boucle_jeu = False

    if nombre_vie < 1:
        print(f"\n la partie est terminer , votre nombre de victoire est {nombre_victoire} monstre"
              f"bonne journee!")

    elif nombre_victoire_suivi >= 3:
        force_adversaire= random.randint(1, 5) + random.randint(1, 5)

    else:
        force_adversaire = random.randint(1, 5) + random.randint(1, 5)

