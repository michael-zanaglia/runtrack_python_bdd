mysql> insert into etage (nom, numero, superficie) values ('RDC', 0, 500);
Query OK, 1 row affected (0.01 sec)

mysql> insert into etage (nom, numero, superficie) values ('R+1', 1, 500);
Query OK, 1 row affected (0.00 sec)

mysql> select * from etage;
+----+------+--------+------------+
| ID | nom  | numero | superficie |
+----+------+--------+------------+
|  1 | RDC  |      0 |        500 |
|  2 | R+1  |      1 |        500 |
+----+------+--------+------------+
2 rows in set (0.00 sec)

mysql> insert into salle (nom, id_etage, capacite) values ('Lounge', 1, 100);
Query OK, 1 row affected (0.01 sec)

mysql> insert into salle (nom, id_etage, capacite) values ('Studio Son', 1, 5);
Query OK, 1 row affected (0.00 sec)

mysql> insert into salle (nom, id_etage, capacite) values ('Broadcasting', 2, 50);
Query OK, 1 row affected (0.00 sec)

mysql> insert into salle (nom, id_etage, capacite) values ('Bocal Peda', 2, 4);
Query OK, 1 row affected (0.00 sec)

mysql> insert into salle (nom, id_etage, capacite) values ('Coworking', 2, 80);
Query OK, 1 row affected (0.00 sec)

mysql> insert into salle (nom, id_etage, capacite) values ('Studio Video', 2, 5);
Query OK, 1 row affected (0.00 sec)

mysql> select * from salle;
+----+--------------+----------+----------+
| ID | nom          | id_etage | capacite |
+----+--------------+----------+----------+
|  1 | Lounge       |        1 |      100 |
|  2 | Studio Son   |        1 |        5 |
|  3 | Broadcasting |        2 |       50 |
|  4 | Bocal Peda   |        2 |        4 |
|  5 | Coworking    |        2 |       80 |
|  6 | Studio Video |        2 |        5 |
+----+--------------+----------+----------+
6 rows in set (0.00 sec)