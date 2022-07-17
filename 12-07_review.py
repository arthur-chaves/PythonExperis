# 1
class Riempidict():
    dict1={}
    
    def __init__(self):
        i=1
        while i <= 3:
            k1 = input ("Qual'è la chiave? ")
            l1 = input ("Qual'è il valore? ")
            self.dict1.update({k1:l1})
            print(self.dict1)
            i+=1

x1 = Riempidict()   
        
# 2
dict2 = {"a":23, "b":35, "c":43}
print(dict2)

class del_dict:
    dict2 = {"a":23, "b":35, "c": 43}
    def deld (self,x):
        self.dict2.pop(x)
dictn = del_dict()

domanda = input("Cosa vuoi? ")
if domanda == "keys":
    print(dictn.dict2.keys())
elif domanda == "values":
    print(dictn.dict2.values())
else:
    x3 = input("Cosa vuoi eliminare? ")
    dictn.deld(x3)
    print(dictn.dict2)

# 3 ancora non va 
class principal():
    def __init__ (self, user, passw):
        self.__usern = user
        self.__password = passw
    
    def troca_user(self, olduser, passw, newuser):
        if (olduser == self.__usern):
            if(passw == self.__password):
                self.__usern = newuser
        else: 
            print("Error")
    
    def troca_password(self, user, oldpassw, newpassw):
        if (user == self.__usern):
            if(oldpassw == self.__password):
                self.__password = newpassw
        else: 
            print("Error")

    def checkUser(self, usr, pwd):
        if(usr == self.__usern and pwd == self.__password):
            return "OK"
        else:
            print("permesso negato")
            exit(1)

class user(principal):
    def __init__ (self, user, passw):
        principal.__init__(self, user, passw)
        
    def troca_user(self, olduser, passw, newuser):
        principal.troca_user(olduser, passw, newuser)
    
    def getInfo(self):
        usr = input("inserisci username: ")
        pwd = input("inserisci password: ")
        return principal.checkUser(self, usr, pwd)
    
    def getInfo(self, usr, pwd):
        return principal.checkUser(self, usr, pwd)
        


# # 5
listan = ["Francesco", "Giorgia"]
listac = ["Ferrari", "Rossi"]
for i in listan:
    for j in listac:
        print(i,j)
    
# 6
class Squadra:
    def __init__ (self, nome):
        self.lsquadra = []
        if len(nome) == 5:
            for i in nome:
                self.lsquadra.append(i)

    def troca_gioc(self, fora, dentro):
        self.lsquadra.remove(fora)
        self.lsquadra.append(dentro)       
    
    def print(self):
        for i in self.lsquadra:
            print(i.nome, i.giocat)
    

class Giocatore(Squadra):
    def __init__(self, nome, pos):
        Squadra.__init__(self, nome)
        self.giocat = pos
        self.nome=nome

jog1 = Giocatore("Arana", "Terzino")
jog2 = Giocatore("Hulk", "Attacante")
jog3 = Giocatore("Keno", "Attacante")
jog4 = Giocatore("Allan", "Medio")
jog5 = Giocatore("Nacho", "Trequartista")
jog6 = Giocatore("Diego Costa", "Attacante")

squadra1 = [jog1,jog2,jog3,jog4,jog5]
squadra = Squadra(squadra1)
squadra.print()
squadra.troca_gioc(jog3, jog6)
squadra.print()

# 7
class Comune():
    lista1=[] 
    def __init__ (self, nome):
        self.cit = nome

    def splitbudget(self):
        x=0  
        for i in range(2):
            budget = input("Qual è il budget? ")
            Comune.lista1.append(float(budget))
            for j in Comune.lista1:
                x += j
            y = sum(Comune.lista1)
        self.budget_asl = float(y)*0.3
        self.budget_pro = float(y)*0.2
        self.budget_cit = float(y) - self.budget_asl - self.budget_pro

    def printbudget(self):    
        print(self.budget_asl)
        print(self.budget_pro)
        print(self.budget_cit)

class ASL(Comune):
    def __init__(self, nome):
        Comune.__init__(self, nome)

    
class Proloco(Comune):
    def __init__(self, nome):
        Comune.__init__(self,nome)
        

citta = "Roma"    
a= Comune(citta)
a.splitbudget()
a.printbudget()

#8
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





