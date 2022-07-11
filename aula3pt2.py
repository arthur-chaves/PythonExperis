class Zoo():
    def __init__ (self, animale):
        self.anml = animale

class Animale(Zoo):
    def __init__ (self, nome):
        self.n_anml = nome

class mammiferi(Animale):
    listamm = []
    def __init__(self, nome, tipo):
        Animale.__init__(self, nome)
        self.t = tipo

class pesce(Animale):
    listaps = []
    def __init__(self, nome, tipo):
        Animale.__init__(self, nome)
        self.t = tipo


i=1
while i <= 6:
    print ("Tipi di animale: Cane, Gatto, Zebra, Lupo, Acciuga, Cefalo")
    selezionaAnimale = input("Qual è l'animale? ")
    if selezionaAnimale == "Cane":
        x1=mammiferi("Cane", "sì")
        x1.listamm.append("Cane")
    elif selezionaAnimale == "Gatto":
        x1=mammiferi("Gatto", "sì")
        x1.listamm.append("Gatto")
    elif selezionaAnimale == "Zebra":
        x1=mammiferi("Zebra", "sì")
        x1.listamm.append("Zebra")
    elif selezionaAnimale == "Lupo":
        x1=mammiferi("Lupo", "sì")
        x1.listamm.append("Lupo")
    elif selezionaAnimale == "Acciuga":
        x1=pesce("Acciuga", "sì")
        x1.listaps.append("Acciuga")
    elif selezionaAnimale == "Cefalo":
        x1=pesce("Cefalo", "sì")
        x1.listaps.append("Cefalo")
    else:
        print("Error")
    print(mammiferi.listamm)
    print(pesce.listaps)
    i+=1

#2
class login_pass():
    def __init__(self):
        self.__log__ = None
        self.__pas__ = None
    def log (self, login):
        self.__log__ = login
    def passw (self, passw):
        self.__pas__ = passw
username = input("username: ")
password = input("password: ")

user = login_pass()
login_pass.log(username)
login_pass.passw(password)