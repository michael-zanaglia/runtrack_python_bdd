delete from etudiant where nom = "Doe";
mysql> select * from etudiant;
+----+-----------+----------+------+---------------------------------+
| ID | nom       | prenom   | age  | email                           |
+----+-----------+----------+------+---------------------------------+
|  1 | Spaghetti | Betty    |   20 | betty.spaghetti@laplateforme.io |
|  2 | Steak     | Chuck    |   45 | chuck.steak@laplateforme.io     |
|  4 | Binkie    | Barnes   |   16 | barnes.binkie@laplateforme.io   |
|  5 | Dupuis    | Gertrude |   20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis    | Martin   |   18 | martin.dupuis@laplateforme.io   |
+----+-----------+----------+------+---------------------------------+
5 rows in set (0.00 sec)