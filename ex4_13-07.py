
#3 update, best way!!

class Fabrica():    
    def __init__(self, nome = "Fiat"):
        self.fab = nome

    def creaFab(self):
        x1 = sport()
        x2 = acciaio()
        x3 = ferro()
    
        p=input("Quante volte? ")
        for i in range(int(p)):
            x_i = input("Qual'è la classe? ")
            if x_i == "sport":
                x_i=x1.__init__()
                x1.printnome()
            elif x_i == "acciaio":
                x_i=x2.__init__()
                x2.printnome()
            elif x_i == "ferro":
                x_i=x3.__init__()
                x3.printnome()
            else:
                print("error")
    
    def printarea(self):
        print("Fabbrica di nome", self.tipo)
    
            
class sport(Fabrica):
    def __init__(self, tipo = "sport"):
        Fabrica.__init__(self)
        self.tipo = tipo

class acciaio(Fabrica):
    def __init__(self, tipo = "acciaio"):
        Fabrica.__init__(self)
        self.tipo = tipo


class ferro(Fabrica):
    def __init__(self, tipo = "ferro"):
        Fabrica.__init__(self)
        self.tipo = tipo


# x10 = Fabrica()
# x10.creaFab()

#4
#non ho capito se devo mettere TUTTO in fabbrica o no quindi ho messo, la logica sara la stessa
#per gli altri classi
#per capire meglio, c'è il ragionamento commentato dentro degli classi figli
class Fabrica():    
    def __init__(self, nome = "Fiat"):
        self.fab = nome

    def creaFab(self):
        x1 = sport()
        x2 = acciaio()
        x3 = ferro()
        s1 = basket()
        s2 = calcio()  
      
    
        p=input("Quante volte? ")
        for i in range(int(p)):
            x_i = input("Qual'è la classe? ")
            if x_i == "sport":
                x_i=x1.__init__()
                x1.printnome()
                y_i = input("Qual'è la specialità? ")
                if y_i == "basket":
                    y_i=s1.__init__()
                    s1.printnome()
                elif y_i == "calcio":
                    y_i=s2.__init__()
                    s2.printnome()
                else:
                    print("error")
            elif x_i == "acciaio":
                x_i=x2.__init__()
                x2.printnome()
            elif x_i == "ferro":
                x_i=x3.__init__()
                x3.printnome()
            else:
                print("error")
    
    def printnome(self):
        print("Fabbrica di nome", self.tipo)
    
    # def printpalla(self):
    #     print("Palla di nome", self.palla)
    #commentato per utilizzare lo stesso metodo, pero sarebbe più chiaro, un argomento in piu
    #con 'palla', si vede meglio l'eredità    
            
class sport(Fabrica):
    def __init__(self, tipo = "sport"):
        Fabrica.__init__(self)
        self.tipo = tipo
    
    
    # def creaFab(self):
    #     s1 = basket()
    #     s2 = calcio()  
        
    #     p2=input("Quante volte? ")
    #     for i in range(int(p2)):
    #         y_i = input("Qual'è la palla? ")
    #         if y_i == "basket":
    #             y_i=s1.__init__()
    #             s1.printpalla()
    #         elif y_i == "calcio":
    #             y_i=s2.__init__()
    #             s2.printpalla()
    #         else:
    #             print("error")
              

# class basket(sport):
#     def __init__(self, tipo="sport", palla = "basket"):
#         sport.__init__(self, tipo)
#         self.palla = palla
    
class basket(sport):
    def __init__(self, tipo="basket"):
        sport.__init__(self)
        self.tipo = tipo

# class calcio(sport):
#     def __init__(self, tipo="sport", palla = "calcio"):
#         sport.__init__(self, tipo)
#         self.palla = palla

class calcio(sport):
    def __init__(self, tipo="calcio"):
        sport.__init__(self)
        self.tipo = tipo
    
class acciaio(Fabrica):
    def __init__(self, tipo = "acciaio"):
        Fabrica.__init__(self)
        self.tipo = tipo

class ferro(Fabrica):
    def __init__(self, tipo = "ferro"):
        Fabrica.__init__(self)
        self.tipo = tipo
    


# x10 = Fabrica()
# x10.creaFab()
x5 = Fabrica()
x5.creaFab()
# x3 = sport()
# x3.creaFab()