import mysql.connector


conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mdp",
    database = "LaPlateforme"
)

cursor = conn.cursor()
request = "select sum(capacite) from salle"
cursor.execute(request)

result = cursor.fetchall()

print(f"La capacité de toutes les salles est de : {result[0][0]}")
