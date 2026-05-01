class Animal:
    def __init__ (self, nom:str="" , espece:str="" ,age:int=0 ):
        self.nom = nom
        self.espece = espece
        self.age = age
    
    def vieillir (self, annees:int):
        self.age += annees
        return self.age
    def afficherDetails (self):
        print("Nom de l'animal:",self.nom)
        print("Espèce:",self.espece)
        print("Âge:",self.age)
        