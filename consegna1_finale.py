#criar um sistema que pegue o input e print depois de controlar se é falso
#criar uma serie de inputs, inserir eles numa lista e print, controlando que nao tenha false
#criar um sistema de perguntas e input que inserem e controlam se os dados que se passarem no if, entram na lista e depois imprimir ela

#1
frase0 = float(input("Qual`è il tuo numero? "))
if frase0 == 0:
    x1= ("False")
else:
    x1= ("True")
print(x1)

#2
lista1=[]
frase1 = float(input("Qual'è il tuo numero 1? "))
lista1.append(frase1)
frase2 = float(input("Qual'è il tuo numero 2? "))
lista1.append(frase2)
frase3 = float(input("Qual'è il tuo numero 3? "))
lista1.append(frase3)
frase4 = float(input("Qual'è il tuo numero 4? "))
lista1.append(frase4)

if frase1 == 0:
    lista1.remove(frase1)
else:
    x2=1

if frase2 == 0:
    lista1.remove(frase2)
else:
    x2=2

if frase3 == 0:
    lista1.remove(frase3)
else:
    x2=3

if frase4 == 0:
    lista1.remove(frase4)
else:
    x2=4
print(lista1)

#3
lista2=[]
domanda1 = input("Qual'è la capitale? ")
if domanda1 == "Roma":
    lista2.append(domanda1)
    print(lista2)
else:
    x1 = "Wrong"
    print(x1)


domanda2 = float(input("2 + 2 è quanto? "))
if domanda2 == 4:
    lista2.append(domanda2)
    print(lista2)
else:
    x1 = "Wrong"
    print(x1)
    print(lista2)

domanda3 = input("CS:GO GOAT? ")
if domanda3 == "FalleN":
    lista2.append(domanda3)
    print(lista2)
else:
    x1 = "Wrong"
    print(x1)
    print(lista2)