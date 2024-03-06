mysql> use laplateforme
Database changed
mysql> create table etage (ID int not null primary key auto_increment, nom varchar(255), numero int, superficie int);
Query OK, 0 rows affected (0.06 sec)
mysql> show tables;
+------------------------+
| Tables_in_laplateforme |
+------------------------+
| etage                  |
| etudiant               |
+------------------------+
2 rows in set (0.01 sec)

mysql> create table salle (ID int not null primary key auto_increment, nom varchar(255), id_etage int, capacite int);
Query OK, 0 rows affected (0.02 sec)

mysql> show tables;
+------------------------+
| Tables_in_laplateforme |
+------------------------+
| etage                  |
| etudiant               |
| salle                  |
+------------------------+
3 rows in set (0.00 sec)