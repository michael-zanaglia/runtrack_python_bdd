import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mdp",
    database = "Laplateforme"
)

cursor = conn.cursor()
requete = "select nom, capacite from salle"
cursor.execute(requete)

resultats = cursor.fetchall()

print(resultats)
    

cursor.close()
conn.close()