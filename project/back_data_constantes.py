# Ici nous aurons tous les variables, constantes et les donnees des tableaux excel
import sqlite3

TYPE_PROFILE = ['IPE', 'IPN', 'HE', 'HL', 'HD', 'HP']
TYPE_ACIER = ['S 235', 'S 275', 'S 355']
N0 = 150 or 200
PI = 3.14
E = 2.1 * (10^5)
G = 0.81 * (10^5)
COEFF_POISSON = 0.3
DILATATION_LINEAIRE = 11 * (10^-6)
POIDS_VOLUMIQUE = 78.50
GAMA_M0 = 1
GAMA_M1 = 1.1

RESULTATS_UTILE = {
    'a': "Travée du platelage",
    'H': "Force de poussée",
    'Type acier': "Caracteristique du matériaux",
    'Profilé': "Type de section",
    'Classe section': "Classe de la section",
    'Msd': "Moment flechissant",
    'Vsd': "Effort tranchant",
    'Mr': "Moment resistant",
    'Av': "Aire de cisaillement",
    'f': "Fleche",
    'Mb,rd': "Moment ultime au deversement",
    'Mcr': "Moment critique",
    'lambdaBar_w': "Elancement de l'ame",
    'Nsd': "Effort axial",
}

DB_NAME = "project/data_base.db"

def get_database_connection():
    con = sqlite3.connect(DB_NAME)
    return con

def create_tables():
    table_resultat_calcul = """ CREATE TABLE IF NOT EXISTS resultatCalcul(
            label      TEXT    PRIMARY KEY    NOT NULL,
            data       REAL                   NOT NULL
        )   
        """
    table_resultat_verification = """ CREATE TABLE IF NOT EXISTS resultatVerification(
            label      TEXT    PRIMARY KEY    NOT NULL,
            data       TEXT                   NOT NULL
        )   
        """
    conn = get_database_connection()
    conn.execute(table_resultat_calcul)
    conn.execute(table_resultat_verification)
    conn.close()

create_tables()

def add_data_to_db_resultat_calcul(resultat):
    try:
        conn = get_database_connection()
        add_resultat = ''' INSERT INTO resultatCalcul(label,data) VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(add_resultat, resultat)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erreur: {e}")
        
def add_data_to_db_resultat_verification(resultat):
    try:
        conn = get_database_connection()
        add_resultat = ''' INSERT INTO resultatVerification(label,data) VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(add_resultat, resultat)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erreur: {e}")
    
def read_resultat_calcul():
    conn = get_database_connection()
    reader = ''' SELECT * FROM resultatCalcul; '''
    cur = conn.cursor()

    cur.execute(reader)
    resultats_calcul = cur.fetchall()
    
    data_resultats = []
    for data in resultats_calcul:
        data_resultats.insert(0 , data)

    cur.close()
    conn.close()  

    return data_resultats

def read_resultat_verification():
    conn = get_database_connection()
    reader = ''' SELECT * FROM resultatVerification; '''
    cur = conn.cursor()

    cur.execute(reader)
    resultats_calcul = cur.fetchall()
    
    data_resultats = []
    for data in resultats_calcul:
        data_resultats.insert(0 , data)

    cur.close()
    conn.close()

    return data_resultats

def delete_all_data():
    conn = get_database_connection()
    c = conn.cursor()
    
    c.execute('DELETE FROM resultatCalcul;')
    c.execute('DELETE FROM resultatVerification;')

    conn.commit()
    conn.close()

def get_resultat_calcul(label):
    conn = get_database_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM resultatCalcul WHERE label=?", (label,))

    element = cur.fetchone()
    
    cur.close()
    conn.close()
    
    return element

def delete_partial_data():
    data_getting = ['Pn', 'E1', 'a', 't', 'Q', 'G', 'H']
    data_storage = {}
    for data_get in data_getting:
        data = get_resultat_calcul(data_get)
        label = data[0]
        value = data[1]
        
        data_storage[label] = value
        
    delete_all_data()
    
    for key, valeur in data_storage.items():
        resultat = (key, valeur)
        add_data_to_db_resultat_calcul(resultat)
    

