#class dyal compte bancaire 
class CompteBancaire : 
    def __init__(self, numeroCompte:float=0.0,nom:str="",solde:float=0.0):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde


    
#methode dyal lversement 
    def versement(self,montant:float):
        if montant < 0 :
            raise ValueError ("\"le montant doit etre strictement positive\"")
        self.solde += montant
        return self.solde
 #methode de retrait
    def retrait(self,montant:float):
        if montant < 0 :
            raise ValueError ("\"le montant doit etre strictement positive\"")
        if montant > self.solde :
            raise ValueError ("\"solde insuffisant\"")
        self.solde -= montant
        return self.solde
#methode de afficher solde
    def afficher (self):
        print ("Le solde du compte de",self.nom,"est:",self.solde)
        