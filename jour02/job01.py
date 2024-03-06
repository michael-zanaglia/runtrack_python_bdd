import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mdp",
    database = "Laplateforme"
)

cursor = mydb.cursor()
requete = "SELECT * from etudiant"
cursor.execute(requete)

for x in cursor :
    print(x)