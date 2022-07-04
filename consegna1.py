#criar um sistema que pegue o input e print depois de controlar se é falso
#criar uma serie de inputs, inserir eles numa lista e print, controlando que nao tenha false
#criar um sistema de perguntas e input que inserem e controlam se os dados que se passarem no if, entram na lista e depois imprimir ela

#1
frase0 = input("Qual`è il tuo input? ")
if frase0 == 0:
    x1= ("Falso")
else:
    x1= ("True")
print(x1)

#2
lista1=[]
frase1 = input("Qual'è il tuo input 1? ")
lista1.append(frase1)
frase2 = input("Qual'è il tuo input 2? ")
lista1.append(frase2)
frase3 = input("Qual'è il tuo input 3? ")
lista1.append(frase3)
frase4 = input("Qual'è il tuo input 4? ")
lista1.append(frase4)
print(lista1)

#3
lista2=[]
domanda1 = input("Qual'è la capitale? ")
if domanda1 == "Roma":
    lista2.append(domanda1)
else:
    print = ("No")
print(lista2)

domanda2 = input("2 + 2 è quanto? ")
if domanda2 == 4:
    lista2.append(domanda2)
else:
    print = ("No")
print(lista2)

