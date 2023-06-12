import csv
import pymysql
from Request import _requetes

def connexion_mysql():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=""
    )
    return conn

def execute_requete(conn, requete, donnees=None):
    cursor = conn.cursor()
    if donnees:
        cursor.execute(requete, donnees)
    else:
        cursor.execute(requete)
    conn.commit()
    cursor.close()

def inserer_donnees_csv(conn, fichier_csv, nom_table):
    with open(fichier_csv, 'r') as fichier:
        donne_csv = csv.reader(fichier)
        next(donne_csv)  
        for rang in donne_csv:
            requete = _requetes['INSERT_' + nom_table.upper()]
            execute_requete(conn, requete, rang)

def creer_base():
    conn = connexion_mysql()
    execute_requete(conn, _requetes['DROP_DATABASE'])
    execute_requete(conn, _requetes['CREATE_DATABASE'])
    execute_requete(conn, _requetes['USE_DATABASE'])
    execute_requete(conn, _requetes['CREATE_TABLE_PILOTES'])
    execute_requete(conn, _requetes['CREATE_TABLE_UTILISATEURS'])

    inserer_donnees_csv(conn, 'pilotes.csv', 'pilotes')
    inserer_donnees_csv(conn, 'utilisateurs.csv', 'utilisateurs')

    execute_requete(conn, _requetes['CREATE_TABLE_MOTOS'])
    inserer_donnees_csv(conn, 'motos.csv', 'motos')

    execute_requete(conn, _requetes['CREATE_TABLE_ENCHERES'])
    execute_requete(conn, "ALTER TABLE encheres ADD INDEX enchere_index (id_enchere);")
    inserer_donnees_csv(conn, 'encheres.csv', 'encheres')

    execute_requete(conn, _requetes['CREATE_TABLE_ENCHERIR'])
    inserer_donnees_csv(conn, 'encherir.csv', 'encherir')

    conn.close()
    print()
    print("La base de données a été créée avec succès.")

if __name__ == "__main__":
    creer_base()