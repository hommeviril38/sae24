_requetes = {
    'DROP_DATABASE' : """ DROP DATABASE IF EXISTS sae23; """,

    'CREATE_DATABASE': """ CREATE DATABASE IF NOT EXISTS sae23; """,

    'USE_DATABASE': """ USE sae23; """,

    'CREATE_TABLE_PILOTES': """ CREATE TABLE IF NOT EXISTS pilotes (
        id_pilote int(20) PRIMARY KEY NOT NULL, 
        nom varchar(50) NOT NULL, 
        statut varchar(50) NOT NULL, 
        instagram varchar(50) NOT NULL, 
        abonnes int(7) NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;""",

    'CREATE_TABLE_UTILISATEURS': """ CREATE TABLE IF NOT EXISTS utilisateurs (
        id_utilisateur int(20) PRIMARY KEY NOT NULL, 
        nom_utilisateur varchar(50) NOT NULL 
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1; """,

    'CREATE_TABLE_MOTOS': """ CREATE TABLE IF NOT EXISTS motos (
          id_moto int(20) NOT NULL,
          marque varchar(50) NOT NULL,
          modele varchar(50) NOT NULL,
          annee int(4) NOT NULL,
          cylindree int(6) NOT NULL,
          prix decimal(6,0) NOT NULL,
          id_pilote int(20) NOT NULL,
          FOREIGN KEY (id_pilote) REFERENCES pilotes(id_pilote) ON DELETE CASCADE, 
          INDEX (id_moto)
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1; """,


    'CREATE_TABLE_ENCHERES': """ CREATE TABLE IF NOT EXISTS encheres (
          id_enchere int(20) PRIMARY KEY NOT NULL,
          id_moto int(20) NOT NULL,
          FOREIGN KEY (id_moto) REFERENCES motos(id_moto) ON DELETE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1; """,

# La table suivante n'était pas présente dans le livrable 1, elle a été rajouté pour faire fonctionner la vente aux enchères :

    'CREATE_TABLE_ENCHERIR': """ CREATE TABLE IF NOT EXISTS enchérir (
          id_enchere int(20) NOT NULL,
          id_utilisateur int(20) NOT NULL,
          montant_enchere decimal(6,0) NOT NULL,
          date_enchere datetime NOT NULL,
          FOREIGN KEY (id_enchere) REFERENCES encheres(id_enchere),
          FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id_utilisateur),
          INDEX (id_enchere, id_utilisateur)
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1; """,



    'INSERT_ENCHERES': """INSERT INTO encheres (id_enchere, id_moto) VALUES (%s, %s);""",

    'INSERT_MOTOS': """ INSERT INTO motos (id_moto, marque, modele, annee, cylindree, prix, id_pilote) VALUES (%s, %s, %s, %s, %s, %s, %s); """,

    'INSERT_PILOTES': """ INSERT INTO pilotes (id_pilote, nom, statut, instagram, abonnes) VALUES (%s, %s, %s, %s, %s); """,

    'INSERT_UTILISATEURS': """ INSERT INTO utilisateurs (id_utilisateur, nom_utilisateur) VALUES (%s, %s); """,
    
    'INSERT_ENCHERIR': """ INSERT INTO enchérir (id_enchere, id_utilisateur, montant_enchere, date_enchere) VALUES (%s, %s, %s, %s); """
}


