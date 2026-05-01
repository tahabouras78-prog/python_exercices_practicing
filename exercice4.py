# Exercice 4 : Class Temps
class Temps:
    def __init__(self, h: int = 0, m: int = 0, s: int = 0):
        self.__h = h       #kandiro private attributes bach may9ed mychoufhoum ghir l methods dyal lclass
        self.__m = m
        self.__s = s

    # Méthode pour afficher le temps
    def afficher(self):                       #had afficher hiya li tprinti resultat 
        print(f"{self.__h}h {self.__m}min {self.__s}s")

    # Méthodes pour obtenir les heures, minutes et secondes
    def getheurs(self):                          #bach na3ti lpublic lvalue dyal private attribute
        return self.__h

    def getmin(self):
        return self.__m

    def getsec(self):
        return self.__s

    # Méthode bach njem3ou zouj temps matnsach self.calc_temps() bach na3ti resultat majusti
    def ajouter(self, t1, t2):
        self.__h = t1.__h + t2.__h
        self.__m = t1.__m + t2.__m
        self.__s = t1.__s + t2.__s
        self.calc_temps()  

    # Méthode bach najustiw l temps
    def calc_temps(self):
        if self.__s >= 60:
            self.__m += self.__s // 60
            self.__s = self.__s % 60

        if self.__m >= 60:
            self.__h += self.__m // 60
            self.__m = self.__m % 60


# Programme principal
if __name__ == "__main__":
    print("Entrée du premier temps :")
    h1 = int(input("Heures : "))
    m1 = int(input("Minutes : "))
    s1 = int(input("Secondes : "))
    t1 = Temps(h1, m1, s1)

    print("\nEntrée du deuxième temps :")
    h2 = int(input("Heures : "))
    m2 = int(input("Minutes : "))
    s2 = int(input("Secondes : "))
    t2 = Temps(h2, m2, s2)

    # Calcul de la somme

    t3 = Temps()    #objet vide kan3mroh bresulta final
    t3.ajouter(t1, t2)  #mn mouraha kan3tiha t1 w t2 bach tjma3hom deja derna lmethod ajouter 

    print("Résultat de l’addition des deux temps :")
    t3.afficher()

  



              
    

         



   



      
      