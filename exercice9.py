class Voiture:
    def __init__(self, marque:str="", modele:str="",kilometrage:float=0.0):
        self.marque = marque
        self.modele = modele
        self.kilometrage = kilometrage
        
    def rouler(self,km:float):
        return self.kilometrage + km
    def afficher(self):
        print("Marque:",self.marque)
        print("Modèle:",self.modele)
        print("Kilométrage:",self.kilometrage)