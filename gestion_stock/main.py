import pygame
import sys
import mysql.connector

class Data() :
    def __init__(self, nom) :
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "mdp",
            database = "store"
        )
        self.article = nom
        self.cursor = self.conn.cursor()
        request = "select * from product inner join category on product.categoryID = category.ID where product.name = '{}'".format((self.article))
        self.cursor.execute(request)
        self.result = self.cursor.fetchall()
        
    
    def Details(self) :
        print(self.result[0])
        self.noms = self.result[0][1]
        print(self.noms)
        self.desc = self.result[0][2]
        self.price = self.result[0][3]
        self.quantity = self.result[0][4]
        self.category = self.result[0][7]
        
    def quantityTook(self, no) : 
        no = self.quantity - no
        self.cursor = self.conn.cursor()
        query = "update product set quantity = {} where name = '{}'".format(no, self.noms)
        self.cursor.execute(query)
        self.conn.commit()
        self.quantity = no
        p.ShowDetails()
    

    
    def quantityAdded(self, no) : 
        no = self.quantity + no
        self.cursor = self.conn.cursor()
        query = "update product set quantity = {} where name = '{}'".format(no, self.noms)
        self.cursor.execute(query)
        self.conn.commit()
        self.quantity = no
        p.ShowDetails()
    

         
    
    def NewItems(self, nom_article, description, price, quantity, category) :
        self.cursor = self.conn.cursor()
        query = "insert into product (name, description, price, quantity, categoryID) values ('{}','{}',{},{},{})".format(nom_article, description, price, quantity, category)
        self.cursor.execute(query)
        self.conn.commit()
        p.route.append((nom_article,(rf"img/{nom_article}.png"), (415,530)))
        p.ShowArticle()
        
        


class Py() :
    def __init__(self, L, l) :
        self.L = L
        self.l = l
        self.screen = pygame.display.set_mode((self.L,self.l))
        pygame.display.set_caption("Gestion de Stock")
        img = pygame.image.load(r"img/etagere.png")
        self.img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height()*1.5))
        self.route = [
            # 1st row
            ("Bananes",(r"img/banane.png"), (50,47)),
            ("Fraises",(r"img/fraise2.png"), (290,47)),
            ("Petit Ecolier",(r"img/pe.png"), (540,47)),
            # 2nd row
            ("Nutella",(r"img/nutella.png"), (175,218)),
            ("Kinder Bueno",(r"img/bueno.png"), (415,218)),
            # 3rd row
            ("Lots de 50 Feuilles A4",(r"img/feuille.png"), (175,380)),
            ("Lunette anti-lumière bleu",(r"img/lun.png"), (415,380)),
            #4th row
            ("Brosse à dent",(r"img/brosse.png"), (175,680)),
            ("Shampoing",(r"img/shamp.png"), (415,680))
        ]
        self.show = True

    def ShowScreen(self) :
        colorscreen = pygame.Color((255,255,255))
        self.screen.fill(colorscreen)
        self.screen.blit(self.img, (0,0))
    
    def ShowArticle(self) :
        for nom, img, (posx, posy) in self.route :
            try :
                self.create = pygame.transform.scale(pygame.image.load(img), (int(pygame.image.load(img).get_width() * 0.65), int(pygame.image.load(img).get_height() * 0.65)))
            except :
                self.create = pygame.transform.scale(pygame.image.load(r"img/vide.png"), (int(pygame.image.load(r"img/vide.png").get_width() * 0.65), int(pygame.image.load(r"img/vide.png").get_height() * 0.65)))
            self.screen.blit(self.create, (posx, posy))
        if self.show :
            p.DrawAddNewItems()
                    
    def ShowDetails(self) :
        self.show = False
        self.ShowScreen()
        self.cross = pygame.image.load(r"img/cross.png")
        self.screen.blit(self.cross, (1125,20))
        police = pygame.font.Font(None, 35)
        for titre, img, (posx, posy) in self.route :
            if object.noms in titre :
                try :
                    img_pointed = pygame.image.load(img)
                except : 
                    img_pointed = pygame.image.load(r"img/vide.png")
                self.screen.blit(img_pointed, (800, 50))
        lines = [
            f"Nom : {object.noms}",
            f"Prix : {object.price} $",
            f"Quantité : {object.quantity}" if object.quantity > 0 else "Quantité : Rupture",
            f"Categorie : {object.category}",
            f"Description : {object.desc}"
            ]
        position_Y = 300
        for line in lines :
            txt = police.render(line, 3, (1,1,1))
            self.screen.blit(txt, (730, position_Y))
            position_Y += 30 
        if not self.show :
            self.DrawQuantityTook()
            self.DrawAddItems()
    
    def DrawQuantityTook(self) :
        self.num_article = pygame.Rect(730, 500, 120, 60)
        color_button = (255,0,0)
        pygame.draw.rect(self.screen, color_button, self.num_article)
        
    def DrawAddItems(self) :
        self.add = pygame.Rect(730, 580, 120, 60)
        color_button = (0,255,0)
        pygame.draw.rect(self.screen, color_button, self.add)
        
    def DrawAddNewItems(self) :
        self.new = pygame.Rect(730, 660, 120, 60)
        color_button = (0,0,255)
        pygame.draw.rect(self.screen, color_button, self.new)
        
    
pygame.init()
p = Py(1170,830)
running = True
p.ShowScreen()



selected_button = None  # Initialisez avec None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            if p.new.collidepoint(pos_x, pos_y) :
                name = input("Nom?\n")
                desc = input("Description?\n")
                price = input("Prix?\n")
                quant= input("Quantité?\n")
                catego = input("Categorie parmi\n 1 Fruits&Legumes\n 2 Produits Alimentaires\n 3 Bureautiques\n 4 Produits Hygieniques?\n")
                object = Data(name)
                object.NewItems(name, desc, price, quant, catego)
            for nom, img, (posx, posy) in p.route:
                irect = p.create.get_rect(topleft=(posx, posy))
                if irect.collidepoint(pos_x, pos_y):
                    object = Data(nom)
                    object.Details()
                    p.ShowDetails()
                    bouttons = [p.num_article, p.add]
                    selected_button = True 
            icross = p.cross.get_rect(topleft=(1125,20))
            if icross.collidepoint(pos_x, pos_y) :
                p.ShowScreen()
                p.show = True

        if selected_button:
            for button in bouttons:
                if button.collidepoint(pos_x, pos_y):
                    if button == p.num_article:
                        while True :
                            n = int(input("La quantité que vous prenez ?"))
                            if (object.quantity - n) < 0 :
                                print("Pas assez d'article en stock.")
                            else : 
                                break
                        object.quantityTook(n)
                        selected_button = False  
                    elif button == p.add :
                        n = int(input("La quantité que vous ajoutez?"))
                        object.quantityAdded(n)
                        selected_button = False           
    p.ShowArticle()        
    pygame.display.flip()
    
    

pygame.quit()
sys.exit()