import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mdp",
    database = "Laplateforme"
)

cursor = conn.cursor()
requete = "select sum(superficie) from etage"
cursor.execute(requete)

result = cursor.fetchall()
print(f"La superficie de LaPlateforme est de {result[0][0]} m2.")