class Employe :
    def __init__ (self, nom :str="", salaireMensuel:float=0.0):
        self.nom = nom
        self.salaire = salaireMensuel

    def augmenterSalaire (self, pourcentage:float):
        augmenter_salaire = self.salaire * (pourcentage / 100)
        self.salaire += augmenter_salaire
        return self.salaire
    
    def calcculerSalaireAnnuel (self):
        salaire_annuel = self.salaire * 12
        return salaire_annuel
    
    def afficherDetails (self):
        print("Nom de l'employé:",self.nom)
        print("Salaire mensuel:",self.salaire)
       