#ex1 mattina
class animale():
    def __init__(self,tipo, nome):
        self.tipo = tipo
        self.nome = nome

    def creafelino(self):
        self.vel = 45
        print(self.nome,"velocita",self.vel)

    def creacanide(self):
        self.perna = 4
        print(self.nome,self.perna, "pernas")

    def creauccello(self):
        self.col = "grigio"  
        print(self.nome,"colore", self.col)

class Felino(animale):
    def __init__(self,tipo, nome, velocita):
        animale.__init__(self,tipo, nome)
        self.vel = velocita
    
class Canide(animale):
    def __init__(self,tipo, nome, perna):
        animale.__init__(self,tipo, nome)
        self.perna = perna 

class Uccello(animale):
    def __init__(self,tipo, nome, colore):
        animale.__init__(self,tipo, nome)
        self.col = colore


nome = input("Nome animale: ")
tipo = input("Tipo di animale ")
x_animal = animale(tipo, nome)

if tipo == "felino": 
    x_animal.creafelino()
elif tipo == "canide":
    x_animal.creacanide()         
elif tipo == "uccello":
    x_animal.creacanide()
else:
    print("Error")

# ex1 pratico

class lista1():
    x_lista = []
    nome = "nome"
    cognome = "cognome"

dati = lista1()

i=3 
while i<4:
    nome = input("Nome? ")
    if nome == "END":
        print(dati.x_lista)
        break
    else:
        dati.x_lista.append(nome)
    cognome = input("Cognome? ")
    if cognome == "END":
        print(dati.x_lista)
        break
    else:
        dati.x_lista.append(cognome)

#ex2 pratico
class lista():
    def __init__ (self, nome):
        self.Time = [] 
        for i in nome:
            self.Time.append(i)

    def troca_gioc(self, fora, dentro):
        x_troca = input("Vuoi confirmare il cambiamento? ")
        if x_troca == "END":
            self.Time.remove(fora)
            self.Time.append(dentro)    
            self.print()
        else:
            print("Cambiamento non fatto")
            self.print()
    
    def print(self):
        for i in self.Time:
            print(i.nome, i.pos)

class Giocatore(lista):
    def __init__(self, nome, pos):
        lista.__init__(self, nome)
        self.nome=nome
        self.pos = pos

jog1 = Giocatore("Arana", "Terzino")
jog2 = Giocatore("Hulk", "Attacante")
jog3 = Giocatore("Vargas", "Attacante")
jog4 = Giocatore("Nacho", "Trequartista")
jog5 = Giocatore("Diego Costa", "Attacante")

time1 = [jog1,jog2,jog3,jog4]

x_time = lista(time1)

x_time.troca_gioc(jog3,jog5)

# ex3 pratico

class Amazon():
    def __init__(self, prezzo, lista):
        self.prezz = prezzo
        self.vendite = lista
    
    def vendas(self):
        vendas_tot = 0
        for i in self.vendite:
            venda = i * self.prezz
            vendas_tot += venda
        print("Fatturato totale: ", vendas_tot)


class Furgone1(Amazon):
    def __init__(self, prezzo, lista, nome):
        Amazon.__init__(self, prezzo, lista)
        self.nome = nome
        
class Furgone2(Amazon):
    def __init__(self, prezzo, lista, nome):
        Amazon.__init__(self, prezzo, lista)
        self.nome = nome
    
class Furgone3(Amazon):
    def __init__(self, prezzo, lista, nome):
        Amazon.__init__(self, prezzo, lista)
        self.nome = nome

def vendas_furgao(furgone):
        x_vendas = input("Cosa vedere o fare? ")
        if x_vendas == "cambia_furgone":
            print("kill input, cambia furgone")
        elif x_vendas == "vendas":
            print(furgone.vendite)
            furgone.vendas()
        else:
            print("Error")

f1 = Furgone1(4, [3,6,7], "1")
f2 = Furgone2(4, [8,9,1], "2")
f3 = Furgone3(4, [21,4,4], "3")


escolha = int(input("Numero furgone? "))
if escolha == 1:
        vendas_furgao(f1)
elif escolha == 2:
        vendas_furgao(f2)
elif escolha == 3:
        vendas_furgao(f3)
else:
    print("Furgone non incontrato")

# ex4
class Fabrica():  
    def __init__(self):
        self.nome = "Fiat"
        

    def creaFab(self):
        x1 = sport()
        x2 = acciaio()
        x3 = ferro()
    
        p=input("Quante volte? ")
        for i in range(int(p)):
            x_i = input("Qual'è la classe? ")
            if x_i == "sport":
                x_i=x1.__init__()
                x1.printarea()
            elif x_i == "acciaio":
                x_i=x2.__init__()
                x2.printarea()
            elif x_i == "ferro":
                x_i=x3.__init__()
                x3.printarea()
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

x10 = Fabrica()
x10.creaFab()
