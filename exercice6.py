#class qui simule la gestion dun simple compte bancaire
class Compte :
    def __init__(self,solde_initial:float=0.0, nom:str = "unknown" ,cin:str="D0000"):
        self.nom = nom
        self.__cin = cin
        if solde_initial < 0 :
            raise ValueError ("\"sold doit etre strictement positive\"")
        self.__solde = solde_initial
    
#getter    
    def getBalance (self):
        return self.__solde 
    
#methode pour deposer un montant specifie
    def deposer (self,montant:float):
        if montant < 0 :
            raise ValueError ("\"le montant doit etre strictement positive\"")
        self.__solde += montant
        return self.__solde
#methode pour retirer un montant specifie
    def retirer (self,montant:float):
        if montant < 0 :
            raise ValueError ("\"le montant doit etre strictement positive\"")
        if montant > self.__solde :
            raise ValueError ("\"solde insuffisant\"")
        self.__solde -= montant
        return self.__solde
    
#Une méthode ajouter Interet pour ajouter de l’intérêt au compte.
    def interet (self, taux:float):
        if taux <= 0 :
            raise ValueError ("\"le taux doit etre positive\"")
        self.__solde = self.__solde * (1 + taux)
        return self.__solde