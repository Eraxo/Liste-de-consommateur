
LISTE = []

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un consommateur à la liste
2: Retirer un consommateur à la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """

MENU_CHOIX = ["1", "2", "3", "4", "5"]



while True:
    choix_utilisateur = input(MENU)
    if choix_utilisateur not in MENU_CHOIX:
        print("Entrez une option valide")
        continue

    if choix_utilisateur == "1":  # Ajouter
        item = input("Entrez le nom et prénom du consommateur à ajouter de la liste : ")
        LISTE.append(item)
        print(f"Le consommateur {item} a bien été ajouté à la liste.")
    elif choix_utilisateur == "2":  # Retirer
        item = input("Entrez le prénom et nom du consommateur à supprimer de la liste : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"Le consommateur {item} a bien été supprimé de la liste.")
        else:
            print(f"Le consommateur {item} n'est pas dans la liste.")
    elif choix_utilisateur == "3":  # Afficher la liste
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun consommateur.")
    elif choix_utilisateur == "4":  # Vider la liste
        LISTE.clear()
        print("La liste a été vidée de son contenu.")
    elif choix_utilisateur == "5":  # Quitter
        print("Ciao !")
        sys.exit()