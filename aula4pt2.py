
from mailbox import NotEmptyError
from telnetlib import DO


# class Comune():
#     def __init__ (self, nome):
#         self.cit = nome


# class ASL(Comune):
#     def __init__(self, nome):
#         Comune.__init__(self, nome)
        
#     def stampa(self):
#         print(budget_asl)
    

# class Proloco(Comune):
#     def __init__(self, nome):
#         Comune.__init__(self,nome)
        
#     def stampa(self):
#         print(budget_pro)
    



# budget_asl = float(x)*0.3
# budget_pro = float(x)*0.2
# budget_cit = float(x) - budget_asl - budget_pro
# print(budget_asl)
# print(budget_pro)
# print(budget_cit)


# lista1=[]  
# x=0  
# for i in range(2):
#     budget = input("Qual è il budget? ")
#     lista1.append(float(budget))
#     for j in lista1:
#         x += j

#2

class Ospedale():
    def __init__(self):
        self.dipendenti = []
    
    def add_dipend(self, dipend):
        self.dipendenti.append(dipend)
    
    def clear_ore(self):
        for dip in self.dipendenti:
            dip.conto += dip.ore_lavoro * dip.stipendio_ora
            dip.ore_lavoro = 0

class Dottore(Ospedale):
    def __init__(self, nome):
        self.nome = nome
        self.conto = 0
        self.ore_lavoro = 0
    def ins_ore(self, horas):
        self.ore_lavoro += horas
        
class Spec(Dottore):
    def __init__(self, nome):
        Dottore.__init__(self, nome)
        self.stipendio_ora = 30

osp = Ospedale()
#criou variavel
dot_1 = Spec("Brato")
dot_2 = Spec("Frac")
#especificou
osp.add_dipend(dot_1)
osp.add_dipend(dot_2)
#adicionou
dot_1.ins_ore(horas=8)
dot_2.ins_ore(horas=10)
#inseriu
osp.clear_ore()
for dottore in osp.dipendenti:
    print(dottore.nome, dottore.conto)

#3
a="Fiat"
x1 = "sport"
x2 = "acciaio"
x3 = "ferro"


class Fabrica():    
    def __init__(self, nome):
        self.fab = nome
    
    def printarea(self):
        print("Fabbrica di nome", self.tipo)
    
    def richiamo(self): 
        p=input("volte? ")
        for i in range(int(p)):
            x_i = input("Qual'è la classe? ")
            if x_i == "sport":
                x_i=y1
                y1.printarea()
            elif x_i == "acciaio":
                x_i=y2
                y2.printarea()
            elif x_i == "ferro":
                x_i=y3
                y3.printarea()
            else:
                print("error")
            
class sport(Fabrica):
    def __init__(self, nome, tipo):
        Fabrica.__init__(self, nome)
        self.tipo = tipo  

class acciaio(Fabrica):
    def __init__(self, nome, tipo):
        Fabrica.__init__(self, nome)
        self.tipo = tipo  

class ferro(Fabrica):
    def __init__(self, nome, tipo):
        Fabrica.__init__(self, nome)
        self.tipo = tipo  


y1 = sport(a, x1)
y2 = acciaio(a, x2)
y3 = ferro(a, x3)
Fabrica.richiamo(a)
