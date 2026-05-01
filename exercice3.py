class Rectangle :
    def __init__ (self,a,b) :
        self.a = a
        self.b = b
    def surface (self):
        return self.a * self.b
if __name__ == "__main__" :
        a = float (input ("enter the length of the rectangle : "))
        b = float (input ("enter the width of the rectangle : "))
        s = Rectangle (a,b)
        print (f"the surface of the rectangle is : {s.surface()} ")