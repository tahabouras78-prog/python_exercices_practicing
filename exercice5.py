#class dyal lpoint 

class Point :
    def __init__(self, x:float=0 ,y:float=0):
        self.__x=x
        self.__y=y

#getters

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

#methode bach ndeplaciw no9taa 

    def deplacer(self,dx:float,dy:float):
        self.__x+=dx
        self.__y+=dy

#methode bach nafficher no9ta

    def afficher(self):
        print(f"{self.__x},{self.__y}") 

#methode pour saisir no9ta

    def saisir(self):
        self.__x=float(input("donner x: "))
        self.__y=float(input("donner y: "))        

#methode  distance bin no9ta w no9ta akhra

    def distance(self,point):
        return ((self.__x - point.getX())**2 + (self.__y - point.getY())**2)**0.5   
        
#methode bach n7esbo lwest bin no9ta w no9ta akhra
     
    def milieu(self,point):
        mx=(self.__x + point.getX())/2
        my=(self.__y + point.getY())/2
        return Point(mx,my)

#methode principale :
if __name__=="__main__": 
        p1=Point()
        p2=Point()
        p1.saisir()
        p2.saisir()
        print("les points saisis sont:")
        p1.afficher()
        p2.afficher()
        print("la distance entre p1 et p2 est:",p1.distance(p2))
        p3=p1.milieu(p2)
        print("le milieu entre p1 et p2 est:")
        p3.afficher()    