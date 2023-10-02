def testCamelCase(text):
    variable_names = [
        "prenomUtilisateur",
        "nomUtilisateur",
        "adresseEmail",
        "numeroTelephone",
        "montantTotalPaye",
        "utilisateurConnecte",
        "catalogueProduits",
        "listeAdressesClients",
        "estDonneesValides",
        "temperatureActuelle",
        "nombreArticlesVendus",
        "estUtilisateurAdmin",
        "contenuPanierAchats",
        "numeroConfirmationCommande",
        "soldeCompte",
        "estNouvelUtilisateur",
        "tailleFichierMaximum",
        "salaireEmploye",
        "codeReductionApplique",
        "coordonneesAdresseLivraison"
    ]

    array = text.split("\n")

    
    countBad = 0
    countTotal = 0
    for i in array:
        if i != "":
            countTotal += 1
            if ( not i in variable_names):
                countBad += 1
    affichage = "Vous avez réussi " + str(countTotal - countBad) + "/" +  str(countTotal) 

    titre = "Test pour l'écriture de variables"
    print("="*len(titre))
    print(titre)
    print("="*len(titre))
    print("-"*len(affichage))
    print("\n\n" + affichage + "\n\n")
    print("-"*len(affichage))

def testUnderScore(text):
    variable_names = [
        "prenom_utilisateur",
        "nom_utilisateur",
        "adresse_email",
        "numero_telephone",
        "montant_total_paye",
        "utilisateur_connecte",
        "catalogue_produits",
        "liste_adresses_clients",
        "est_donnees_valides",
        "temperature_actuelle",
        "nombre_articles_vendus",
        "est_utilisateur_admin",
        "contenu_panier_achats",
        "numero_confirmation_commande",
        "solde_compte",
        "est_nouvel_utilisateur",
        "taille_fichier_maximum",
        "salaire_employe",
        "code_reduction_applique",
        "coordonnees_adresse_livraison"
    ]

    array = text.split("\n")

    
    countBad = 0
    countTotal = 0
    for i in array:
        if i != "":
            countTotal += 1
            if ( not i in variable_names):
                countBad += 1
    affichage = "Vous avez réussi " + str(countTotal - countBad) + "/" +  str(countTotal) 

    titre = "Test pour l'écriture de variables"
    print("="*len(titre))
    print(titre)
    print("="*len(titre))
    print("-"*len(affichage))
    print("\n\n" + affichage + "\n\n")
    print("-"*len(affichage))