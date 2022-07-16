# part 1
class lista():
    x2=[]
dati = lista()

x_v = input("Quante volte? ")
for i in range(int(x_v)):
    dati.nome = input("Qual'è il nome? ")
    if type(dati.nome) == str:
        dati.x2.append(dati.nome)
    dati.cognome = input("Qual'è il cognome? ")
    if type(dati.cognome) == str:
        dati.x2.append(dati.cognome)
    dati.eta = int(input("Qual'è la eta? "))
    if (type(int(dati.eta)) == int):
        dati.x2.append(dati.eta)
    dati.lavoro = input("Qual'è la professione? ")
    if type(dati.lavoro) == str:
        dati.x2.append(dati.lavoro)

    print(dati.x2)

#part 2
class sport():
    listapalla = []
    listaatl=[]  
    def __init__(self):
        self.modalita = "esporte"
    def printname(self):
        print(self.tipologia)
    

class palla(sport):
    def __init__ (self, tipo_p):
        sport.__init__(self)
        self.tipologia = tipo_p
    
    def pallaappend(self):
        self.listapalla.append(self.tipologia)

class atletismo(sport):
    def __init__(self, tipo_a):
        sport.__init__(self)  
        self.tipologia = tipo_a
    
    def atlappend(self):
        self.listaatl.append(self.tipologia)


x_v = input("Quante volte? ")
for i in range(int(x_v)):
    nome = input("Cosa stiamo parlando? ")
    
    if nome == "palla":
            modalita1 = input("Nome del sport con palla? ")
            x1 = palla(modalita1)
            palla.pallaappend(x1)
    elif nome == "atletismo":
            modalita2 = input("Qual attivita nel atletismo? ")
            x2 = atletismo(modalita2)
            atletismo.atlappend(x2)
    else:
            print("Error")
    
    if len(palla.listapalla)>0:
        print("numero di sport con palla:",len(palla.listapalla), "Sport con palla:", palla.listapalla,)   
    
    if len(atletismo.listaatl)>0:
        print("numero di attivita in atletismo:",len(atletismo.listaatl), "Attivita in atletismo: ", atletismo.listaatl)