#1
class sport():
    def __init__(self, esporte):
        self.modalita = esporte
    def printname(self):
        print(self.modalita)

class palla(sport):
    listapalla = []
    def __init__ (self, esporte, tipo_p):
        sport.__init__(self, esporte)
        self.tipologia = tipo_p
    def printpalla(self):
        print("sport con palla")

class atletismo(sport):
    listaatl=[]  
    def __init__(self, esporte, tipo_a):
        sport.__init__(self,esporte)  
        self.tipologia = tipo_a
    def printatl(self):
        print("sport senza palla")

nome = input("Cosa stiamo parlando? ")
if nome == "palla":
        modalita1 = input("Qual attivita ")
        tipologia1 = input("Qual tipo ")
        x1 = palla(modalita1, tipologia1)
        x1.printpalla()
        palla.listapalla.append(modalita1)
        palla.listapalla.append(tipologia1)
        print(palla.listapalla)
elif nome == "atletismo":
        modalita2 = input("Qual attivita ")
        tipologia2 = input("Qual tipo ")
        x2 = atletismo(modalita2, tipologia2)
        x2.printatl()
        atletismo.listaatl.append(modalita2)
        atletismo.listaatl.append(tipologia2)
        print(atletismo.listaatl)
else:
        print("Error")

#3
i=1
while i <= 3:
    nome = input("Cosa stiamo parlando? ")
    if nome == "palla":
        modalita1 = input("Qual attivita ")
        tipologia1 = input("Qual tipo ")
        x1 = palla(modalita1, tipologia1)
        x1.printpalla()
        palla.listapalla.append(modalita1)
        palla.listapalla.append(tipologia1)
        #print(palla.listapalla)
    elif nome == "atletismo":
        modalita2 = input("Qual attivita ")
        tipologia2 = input("Qual tipo ")
        x2 = atletismo(modalita2, tipologia2)
        x2.printatl()
        atletismo.listaatl.append(modalita2)
        atletismo.listaatl.append(tipologia2)
        #print(atletismo.listaatl)
    else:
        print("Error")
    lista_finale = palla.listapalla + atletismo.listaatl
    print(lista_finale)
    i+=1




