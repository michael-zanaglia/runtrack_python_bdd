import mysql.connector



class Salarie() :
    def __init__(self, request) :
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "mdp",
            database = "Laplateforme"
        )
        self.cursor = self.conn.cursor()
        self.request = request

    
    def Create(self) :
        self.cursor.execute(self.request)
        self.conn.commit()
        print("done")
        
    def Read(self) :
        self.cursor.execute(self.request)
        result = self.cursor.fetchall()
        for x in result :
            print(x)
            
    def Update(self) :
        self.cursor.execute(self.request)
        self.conn.commit()
        print("done")
        
    def Delete(self) :
        self.cursor.execute(self.request)
        self.conn.commit()
        print("done")


#req = "insert into employe (nom,prenom,salaire,id_service) values ('Oncle','Ben',0,4)"
#createSalarie = Salarie(req)
#createSalarie.Create()

#ru = "update employe set ID = 6 where prenom = 'Paul'"
#updatesalarie = Salarie(ru)
#updatesalarie.Update()

#rd = "delete from employe where nom = 'Oncle'"
#deletesalarie = Salarie(rd)
#deletesalarie.Delete()

r = "select * from employe"
readsalarie = Salarie(r)
readsalarie.Read()