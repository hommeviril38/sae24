import pymysql
from Request import _requetes
from BDsae23Utils import creer_base, execute_requete

def connexion_mysql():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="sae23"
    )
    return conn

# Fonctions CRUD pour la table "pilotes" :

def ajouter_pilote(conn, id_pilote, nom, statut, instagram, abonnes):
    cursor = conn.cursor()
    requete = _requetes['INSERT_PILOTES']
    donnees = (id_pilote, nom, statut, instagram, abonnes)
    execute_requete(conn, requete, donnees)
    cursor.close()

def supprimer_pilote(conn, id_pilote):
    requete_encherir = "DELETE FROM enchérir WHERE id_enchere IN (SELECT id_enchere FROM encheres WHERE id_moto IN (SELECT id_moto FROM motos WHERE id_pilote = %s))"
    donnees_encherir = (id_pilote,)
    execute_requete(conn, requete_encherir, donnees_encherir)

    requete_encheres = "DELETE FROM encheres WHERE id_moto IN (SELECT id_moto FROM motos WHERE id_pilote = %s)"
    donnees_encheres = (id_pilote,)
    execute_requete(conn, requete_encheres, donnees_encheres)

    requete_motos = "DELETE FROM motos WHERE id_pilote = %s"
    donnees_motos = (id_pilote,)
    execute_requete(conn, requete_motos, donnees_motos)

    requete_pilotes = "DELETE FROM pilotes WHERE id_pilote = %s"
    donnees_pilotes = (id_pilote,)
    execute_requete(conn, requete_pilotes, donnees_pilotes)

def visualiser_pilotes(conn):
    requete = "SELECT * FROM pilotes"
    cursor = conn.cursor()
    cursor.execute(requete)
    resultat = cursor.fetchall()
    cursor.close()
    return resultat

def modifier_pilote(conn, id_pilote, nom, statut, instagram, abonnes):
    requete = "UPDATE pilotes SET nom = %s, statut = %s, instagram = %s, abonnes = %s WHERE id_pilote = %s"
    donnees = (nom, statut, instagram, abonnes, id_pilote)
    execute_requete(conn, requete, donnees)

# Fonctions CRUD pour la table "motos" :

def ajouter_moto(conn, id_moto, marque, modele, annee, cylindree, prix, id_pilote):
    cursor = conn.cursor()
    requete = _requetes['INSERT_MOTOS']
    donnees = (id_moto, marque, modele, annee, cylindree, prix, id_pilote)
    execute_requete(conn, requete, donnees)
    cursor.close()

def supprimer_moto(conn, id_moto):
    requete_encherir = "DELETE FROM enchérir WHERE id_enchere IN (SELECT id_enchere FROM encheres WHERE id_moto = %s)"
    donnees_encherir = (id_moto,)
    execute_requete(conn, requete_encherir, donnees_encherir)

    requete_encheres = "DELETE FROM encheres WHERE id_moto = %s"
    donnees_encheres = (id_moto,)
    execute_requete(conn, requete_encheres, donnees_encheres)

    requete_motos = "DELETE FROM motos WHERE id_moto = %s"
    donnees_motos = (id_moto,)
    execute_requete(conn, requete_motos, donnees_motos)

def visualiser_motos(conn):
    requete = "SELECT * FROM motos"
    cursor = conn.cursor()
    cursor.execute(requete)
    resultat = cursor.fetchall()
    cursor.close()
    return resultat

def visualiser_motos_KTM(conn):
    requete = "SELECT * FROM motos WHERE marque LIKE '%ktm%' OR marque LIKE '%KTM%'"
    cursor = conn.cursor()
    cursor.execute(requete)
    resultat = cursor.fetchall()
    cursor.close()
    return resultat

def visualiser_motos_recente(conn):
    requete = "SELECT * FROM motos WHERE annee > 2013"
    cursor = conn.cursor()
    cursor.execute(requete)
    resultat = cursor.fetchall()
    cursor.close()
    return resultat

def visualiser_motos_pas_chere(conn):
    requete = "SELECT * FROM motos WHERE prix < 5000"
    cursor = conn.cursor()
    cursor.execute(requete)
    resultat = cursor.fetchall()
    cursor.close()
    return resultat

def modifier_moto(conn, id_moto, marque, modele, annee, cylindree, prix, id_pilote):
    requete = "UPDATE motos SET marque = %s, modele =%s, annee = %s, cylindree = %s, prix = %s, id_pilote = %s WHERE id_moto = %s"
    donnees = (marque, modele, annee, cylindree, prix, id_pilote, id_moto)
    execute_requete(conn, requete, donnees)


#Les fonctions suivantes ont étés rajoutées pour le bon fonctionnement du rendu final. 
# Elles ne sont pas utilisées dans le CLI !!

def ajouter_enchere(conn, id_enchere, id_utilisateur, montant_enchere, date_enchere):
    requete = "INSERT INTO enchérir (id_enchere, id_utilisateur, montant_enchere, date_enchere) VALUES (%s, %s, %s, %s);"
    donnees = (id_enchere, id_utilisateur, montant_enchere, date_enchere)
    cursor = conn.cursor()
    cursor.execute(requete, donnees)
    conn.commit()
    cursor.close()

def ajouter_utilisateur(conn, id_utilisateur, nom_utilisateur):
    requete = "INSERT INTO utilisateurs (id_utilisateur, nom_utilisateur) VALUES (%s, %s);"
    donnees = (id_utilisateur, nom_utilisateur)
    cursor = conn.cursor()
    cursor.execute(requete, donnees)
    conn.commit()
    cursor.close()

def visualiser_utilisateurs(conn):
    requete = "SELECT * FROM utilisateurs"
    cursor = conn.cursor()
    cursor.execute(requete)
    resultat = cursor.fetchall()
    cursor.close()
    return resultat

def obtenir_montant_enchere(conn, id_enchere):
    cursor = conn.cursor()
    query = "SELECT MAX(montant_enchere) FROM enchérir WHERE id_enchere = %s"
    cursor.execute(query, (id_enchere,))
    result = cursor.fetchone()
    montant_enchere_max = result[0] if result is not None and result[0] is not None else 0
    return montant_enchere_max


# Menu interactif pour les utilisateurs :



def menu():
    print()
    print("------- Menu -------")
    print()
    print("Options pour les pilotes :")
    print("1 - Ajouter un pilote")
    print("2 - Supprimer un pilote")
    print("3 - Visualiser les pilotes")
    print("4 - Modifier un pilote")
    print()
    print("Options pour les motos :")
    print("5 - Ajouter une moto")
    print("6 - Supprimer une moto")
    print("7 - Visualiser toutes les motos")
    print("8 - Visualiser les motos de la marque KTM")
    print("9 - Visualiser les motos récentes (moins de 10 ans)")
    print("10 - Visualiser les motos pas chères (moins de 5000€)")
    print("11 - Modifier une moto")
    print()
    print("0 - Quitter")
    print()
    choix = input("Veuillez choisir une option (0-11) : ")
    return choix

if __name__ == "__main__":
    creer_base()
    conn = connexion_mysql()

    while True:
        choix = menu()

        if choix == "0":
            break

        elif choix == "1":
            print()
            id_pilote = input("ID du nouveau pilote : ")
            nom = input("Nom : ")
            statut = input("Statut : ")
            instagram = input("Instagram : ")
            abonnes = input("Abonnés : ")
            ajouter_pilote(conn, id_pilote, nom, statut, instagram, abonnes)
            print()
            print("Le pilote a été ajouté avec succès.")

        elif choix == "2":
            print()
            id_pilote = input("ID du pilote à supprimer : ")
            supprimer_pilote(conn, id_pilote)
            print()
            print("Le pilote a été supprimé avec succès.")

        elif choix == "3":
            print()
            pilotes = visualiser_pilotes(conn)
            print("{:<5} {:<20} {:<40} {:<20} {:<10}".format("ID", "Nom", "Statut", "Instagram", "Abonnés"))
            print("-" * 105)
            for pilote in pilotes:
                print("{:<5} {:<20} {:<40} {:<20} {:<10}".format(pilote[0], pilote[1], pilote[2], pilote[3], pilote[4]))

        elif choix == "4":
            print()
            id_pilote = input("ID du pilote à modifier : ")
            nom = input("Nouveau nom du pilote : ")
            statut = input("Nouveau statut du pilote : ")
            instagram = input("Nouveau compte instagram du pilote : ")
            abonnes = input("Nouveau nombre d'abonnés du pilote : ")
            modifier_pilote(conn, id_pilote, nom, statut, instagram, abonnes)
            print()
            print("Le pilote a été modifié avec succès.")

        elif choix == "5":
            print()
            id_moto = input("ID Moto : ")
            marque = input("Marque : ")
            modele = input("Modèle : ")
            annee = input("Année : ")
            cylindree = input("Cylindrée : ")
            prix = input("Prix : ")
            id_pilote = input("ID Pilote : ")
            ajouter_moto(conn, id_moto, marque, modele, annee, cylindree, prix, id_pilote)
            print()
            print("La moto a été ajoutée avec succès.")
            
        elif choix == "6":
            print()
            id_moto = input("ID de la Moto à supprimer : ")
            supprimer_moto(conn, id_moto)
            print()
            print("La moto a été supprimée avec succès.")

        elif choix == "7":
            motos = visualiser_motos(conn)
            print()
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("ID Moto", "Marque", "Modèle", "Année", "Cylindrée","Prix","ID Pilote"))
            print("-" * 105)
            for moto in motos:
                print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(moto[0], moto[1], moto[2], moto[3], moto[4], moto[5], moto[6]))

        elif choix == "8":
            motos = visualiser_motos_KTM(conn)
            print()
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("ID Moto", "Marque", "Modèle", "Année", "Cylindrée","Prix","ID Pilote"))
            print("-" * 105)
            for moto in motos:
                print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(moto[0], moto[1], moto[2], moto[3], moto[4], moto[5], moto[6]))

        elif choix == "9":
            motos = visualiser_motos_recente(conn)
            print()
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("ID Moto", "Marque", "Modèle", "Année", "Cylindrée","Prix","ID Pilote"))
            print("-" * 105)
            for moto in motos:
                print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(moto[0], moto[1], moto[2], moto[3], moto[4], moto[5], moto[6]))

        elif choix == "10":
            motos = visualiser_motos_pas_chere(conn)
            print()
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("ID Moto", "Marque", "Modèle", "Année", "Cylindrée","Prix","ID Pilote"))
            print("-" * 105)
            for moto in motos:
                print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(moto[0], moto[1], moto[2], moto[3], moto[4], moto[5], moto[6]))

        elif choix == "11":
            print()
            id_moto = input("ID de la moto à modifier : ")
            marque = input("Nouvelle marque : ")
            modele = input("Nouveau modèle : ")
            annee = input("Nouvelle année de fabrication : ")
            cylindree = input("Nouvelle cylindrée : ")
            prix = input("Nouveau prix : ")
            id_pilote = input("Nouvel ID du Pilote associé : ")
            modifier_moto(conn, id_moto, marque, modele, annee, cylindree, prix, id_pilote)
            print()
            print("La moto a été modifiée avec succès.")

        else:
            print("Option invalide. Veuillez choisir une option entre 0 et 11.")

    conn.close()
    print()
    print("Au revoir !")