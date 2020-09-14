import random

class Domino:
    
    def __init__(self,droite,gauche):
        self.droite = droite
        self.gauche = gauche
        self.point = self.point()
    
    def getDroite(self):
        return self.droite
    
    def getGauche(self):
        return self.gauche
    
    def doubleBlancClassique(self):
        if self.gauche == self.droite:
            if self.gauche == 0:
                return("blanc")
            else:
                return("double")
        else:
            return("classique")
     
    def point(self):
        if self.doubleBlancClassique() == "blanc" or self.doubleBlancClassique == "double":
            return(1)
        else:
            return(self.gauche + self.droite)
            
    
    def afficher(self):
        if self.doubleBlancClassique() == "classique":
            print("---------")
            print("|   |   |")
            print("|",self.gauche,"|",self.droite,"|")
            print("|   |   |")
            print("---------")
        
        else:
            print("-----")
            print("|   |")
            print("|",self.gauche,"|")
            print("|   |")
            print("-----")
            print("|   |")
            print("|",self.gauche,"|")
            print("|   |")
            print("-----")
       
class JeuDomino:    
    
    def __init__(self,nombreJoueur):
        self.jeu = self.creeJeu()
        self.jeuMelange = self.melanger()
        self.nombreJoueur = nombreJoueur
        
    def creeJeu(self):
        jeu = []
        for i in range(7):
            for j in range(i,7):
                jeu.append((i,j))
        return(jeu)
      
    def melanger(self):
        jeuMelange = self.creeJeu()
        random.shuffle(jeuMelange)
        return(jeuMelange)
        
    def point(self,gauche,droite):
        if gauche == droite:
            return(1)
        else:
            return(gauche + droite)

    def afficherJeu(self):
        print(self.jeu)        
        
    def afficherJeuMelange(self):
        print(self.jeuMelange)
    
    def distribution(self):        
        if self.nombreJoueur < 2:
            print("Le nombre minimum de joueur est de 2")
            
        elif self.nombreJoueur > 4:
            print("Le nombre maximum de joueur est de 4")
            
        elif self.nombreJoueur == 2:
            j1 , j2 = 0 , 0
            
            for i in range(7):
                j1 += self.point(self.jeuMelange[i][0] , self.jeuMelange[i][1])
            print("Domino du joueur 1: \n", 
                  self.jeuMelange[:7],"\n",
                  "Points du joueur 1:",j1,"\n")
            
            for j in range(7,14):
                j2 += self.point(self.jeuMelange[j][0], self.jeuMelange[j][1])
            print("Domino du joueur 2: \n",
                  self.jeuMelange[7:14],"\n",
                  "Points du joueur 2:",j2,"\n")
            
            print("La pioche: \n",
                  self.jeuMelange[14:])
        
        elif self.nombreJoueur == 3:
            j1 , j2 , j3 = 0 , 0 , 0
            
            for i in range(6):
                j1 += self.point(self.jeuMelange[i][0], self.jeuMelange[i][1])
            print("Domino du joueur 1: \n",
                  self.jeuMelange[:6],"\n",
                  "Points du joueur 1:",j1,"\n")
            
            for j in range(6,12):
                j2 += self.point(self.jeuMelange[j][0], self.jeuMelange[j][1])
            print("Domino du joueur 2: \n",
                  self.jeuMelange[6:12],"\n",
                  "Points du joueur 2:",j2,"\n")
            
            for k in range(12,18):
                j3 += self.point(self.jeuMelange[k][0], self.jeuMelange[k][1])
            print("Domino du joueur 3: \n",
                  self.jeuMelange[12:18],"\n",
                  "Points du joueur 3:",j3,"\n")
            
            print("La pioche: \n",
                  self.jeuMelange[18:])
        
        elif self.nombreJoueur == 4:
            j1 , j2 , j3 , j4 = 0 , 0 , 0 ,0
            
            for i in range(6):
                j1 += self.point(self.jeuMelange[i][0], self.jeuMelange[i][1])
            print("Domino du joueur 1: \n",
                  self.jeuMelange[:6],"\n",
                  "Points du joueur 1:",j1,"\n")
            
            for j in range(6,12):
                j2 += self.point(self.jeuMelange[j][0], self.jeuMelange[j][1])
            print("Domino du joueur 2: \n",
                  self.jeuMelange[6:12],"\n",
                  "Points du joueur 2:",j2,"\n")
            
            for k in range(12,18):
                j3 += self.point(self.jeuMelange[k][0], self.jeuMelange[k][1])
            print("Domino du joueur 3: \n",
                  self.jeuMelange[12:18],"\n",
                  "Points du joueur 3:",j3,"\n")
            
            for l in range(18,24):
                j3 += self.point(self.jeuMelange[l][0], self.jeuMelange[l][1])
            print("Domino du joueur 4: \n",
                  self.jeuMelange[18:24],"\n",
                  "Points du joueur 4:",j4,"\n")
            
            print("La pioche: \n",
                  self.jeuMelange[24:])
            

        
jeuDomino = JeuDomino(2)
jeuDomino.distribution()

