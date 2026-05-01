class rectangle:
    def __init__(self, longeur:float, hauteur:float):
        self.longeur = longeur
        self.largeur = hauteur

    def surface(self):
        return self.longeur * self.hauteur
    def perimetre (self):
        return 2 * (self.longeur + self.hauteur)
    def afficher(self):
        print("Longeur:",self.longeur)
        print("Largeur:",self.hauteur)
        print("Surface:",self.surface())
        print("Perimetre:",self.perimetre())
if __name__== "_main_":
    print("Création d'un rectangle")
    l = float(input("Entrez la longeur du rectangle: "))
    h = float(input("Entrez la hauteur du rectangle: "))
    r = rectangle (l,h)
    r.afficher()
    
     
     