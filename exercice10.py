class Produit :
    def __init__ (self, nom:str="", prix:float=0.0, quantiteEnstock:int=0):
        self.nom = nom
        self.prix = prix
        self.stock = quantiteEnstock
#methode katn9es lprix b pourcentage 
    def Reduction (self, pourcentage:float):
        reduction_amount = self.prix * (pourcentage / 100)
        self.prix -= reduction_amount
        return self.prix
#methode fach katbi3 rah katn9es lquantite men stock    
    def vendre (self, quantite:int):
        if quantite >= self.stock:
            self.stock-= quantite
            return self.srock
        else:
            print("Stock insuffisant")

    def afficherDetails (self):
        print("Nom du produit:",self.nom)
        print("Prix:",self.prix)
        print("Quantité en stock:",self.stock)        