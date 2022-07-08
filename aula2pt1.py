#versione 1, nao usar init
#1
class lista():
    x1=[]
nomevariable = lista()
#nomevariable.x1.append(2)
#nomeio a classe criada depois a variavel criada depois o que quero fazer
#print(nomevariable.x1)

#2
class lista2():
    x2 = []
    nome = "nome"
    cognome = "cognome"
    eta = 1
    lavoro = "lavoro"
    
dati = lista2()
#conectando a classe com a minha lista, criando a minha classe

dati.nome = input("Qual'è il nome? ")
if (type(dati.nome) == str):
    dati.x2.append(dati.nome)
dati.cognome = input("Qual'è il cognome? ")
if (type(dati.cognome) == str):
    dati.x2.append(dati.cognome)
dati.eta = int(input("Qual'è la eta? "))
if (type(int(dati.eta)) == int):
    dati.x2.append(dati.eta)
dati.lavoro = input("Qual'è la professione? ")
if (type(dati.lavoro) == str):
    dati.x2.append(dati.lavoro)

print(dati.x2)




