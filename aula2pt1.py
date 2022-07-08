#versione 1, nao usar init
#1
class lista():
    x1=[]
nomevariable = lista()

#2
class lista2():
    x2 = []
    nome = "nome"
    cognome = "cognome"
    eta = 1
    lavoro = "lavoro"
    
dati = lista2()

dati.nome = input("Qual'è il nome? ")
if type(dati.nome) == str:
    dati.x2.append(dati.nome)
dati.cognome = input("Qual'è il cognome? ")
if type(dati.cognome) == str:
    dati.x2.append(dati.cognome)
dati.eta = int(input("Qual'è la eta? "))
if dati.eta != 0:
    dati.x2.append(dati.eta)
dati.lavoro = input("Qual'è la professione? ")
if type(dati.lavoro) == str:
    dati.x2.append(dati.lavoro)

print(dati.x2)



