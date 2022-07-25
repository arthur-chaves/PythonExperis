import json
import pickle
from pydoc import cli

# ex1 pratico
class conta():
    def __init__(self, entrada, plus):
        self.entrada = entrada
        self.plus = plus
    
    def criaconta(self):  
            s = int(input("Operazione? 1.Soma, 2.Sott, 3.Molt., 4.Div "))
            if s == 1:
                soma(self.entrada, self.plus)
            elif s==2:
                sottrazione(self.entrada, self.plus)
            elif s==3:
               moltiplicazione(self.entrada, self.plus)
            elif s==4:
                divisione(self.entrada, self.plus)    
            else:
                print("error")

class soma(conta):
    def __init__(self, entrada, plus):
        conta.__init__(self, entrada, plus) 
        self.totale = entrada+plus
        print(self.totale)

class sottrazione(conta):
    def __init__(self, entrada, plus):
        conta.__init__(self, entrada, plus)
        self.totale = entrada-plus
        print(self.totale)

class moltiplicazione(conta):
    def __init__(self, entrada, plus):
        conta.__init__(self, entrada, plus)
        self.totale = entrada*plus
        print(self.totale)

class divisione(conta):
    def __init__(self, entrada, plus):
        conta.__init__(self, entrada, plus)
        self.totale = entrada/plus
        print(self.totale)
  
p=input("Quante volte? ")
for i in range(int(p)):
    x1 = int(input("Valore 1: "))
    x2 = int(input("Valore 2: "))
    f = conta(x1,x2)
    f.criaconta()

# # ex2 pratico
class madre():
    def __init__(self, valore):
        self.valore = valore
    def tassasione(self):
        print(self.totale)
    
class figlio1(madre):
    def __init__(self, valore, tassa1=0.2):
        madre.__init__(self, valore)
        self.totale = valore*tassa1

class figlio2(madre):
    def __init__(self, valore, tassa2=0.3):
        madre.__init__(self, valore)
        self.totale = valore*tassa2

v = int(input("Quante volte? "))
for i in range(v):
    in1 = int(input("Valore? "))
    fl1 = int(input("Figlio? "))    
    if fl1 == 1:
        x2 = figlio1(in1)
        x2.tassasione()
    elif fl1==2:
        x2 = figlio2(in1)
        x2.tassasione()
    else:
        print("Error")


#3 pratico

class lista():
    list1=[]
    def __init__ (self, in1,in2,in3):
        self.in1 = in1
        self.in2  = in2
        self.in3 = in3
        self.list1 = [in1,in2,in3]
    
    def printlista(self):
        print(self.list1)

class pck(lista):
    def __init__(self):
        y=pickle.dumps(x1.list1)
        z1=pickle.loads(y)
        print(z1)

class js(lista):
    def __init__(self):
        y=json.dumps(x1.list1)
        z2=json.loads(y)
        print(z2)

v = int(input("Quante volte? "))
for i in range(v):
    i1 = input("Valore 1: ")
    i2 = input("Valore 2: ")
    i3 = input("Valore 3: ")
    x_conv = int(input("Qual è il tipo di conversione? 1.Pickle, 2.Json "))
    if x_conv == 1:
        x1 = lista(i1,i2,i3)
        pck()
    elif x_conv == 2:
        x1 = lista(i1,i2,i3)
        js()
    else:
        print("Error")




#ex1 teorico
#ereditarieta lineare è quando una classe è creata derivata di un'altra, come un figlio di un padre
#mentre l'ereditarieta paralela è quando vari figli prendono lo stesso metodo però con output diversi
#esempio lineare

# class Comune():
#     def __init__ (self, nome):
#         self.cit = nome
#     def print(self):
#         print(self.cit)
#     def print_tipo(self):
#         print(self.tipo)
# class ASL(Comune):
#     def __init__(self, nome,tipo):
#         Comune.__init__(self, nome)
#         self.tipo = tipo

#esempio paralelo 
#sottoclassi di Dino devono essere legate a sottoclassi di uova

# class Dino:
#     # codigo per creare dino

# class uova:
#     # codigo per creare uova

# class T-rex(Dino):
#     # codigo per creare un specifico dino

# class T-rexEgg(Uova)
#     # codigo per creare una uova specifica di questo dino specifico




# ex2 teorico
# ereditarieta è l'abilita di un oggetto acquistare una o tutte le proprietà di un'altro, stipulata da programmatore

# class sport():
#     def __init__(self, esporte):
#         self.modalita = esporte
#     def printname(self):
#         print(self.modalita)

# class palla(sport):
#     def __init__ (self, esporte, tipo_p):
#         sport.__init__(self, esporte)
#         self.tipologia = tipo_p
#     def printpalla(self):
#         print("sport con palla")

#incapsulamento significa la capacità di un oggetto, classe o codigo nascondersi dentro di se stesso
#quindi, quando si construisce una classe, con vari metodi dentro, è incapsulamento
#nascondendo la representazione interna di un oggetto del ambiente esterno

#ex1 pratico che ho fatto qui, più avanti, fa un bello esempio


#polimorfismo è un principio in cui ci dà un modo di utilizzare le proprietà di un oggetto in un altro, o lo stesso oggetto potrebbe avere più forme
#così, un oggetto può avere attributi di vari tipi, avere vari forme e permettere di cambiare il tipo del dato
# class Animale:
#     def __init__(self, eta, name):
#         self.eta = eta
#         self.name = name

#     def suono():
#         pass

# class gatto(Animale):
#     def __init__(self, eta, name):
#         Animale.__init__(eta, name)
    
#     def suono():
#         print("miau")

# class cane(Animale):
#     def __init__(self, eta, name):
#         Animale.__init__(eta, name)
    
#     def suono():
#         print("au au")


#ex3 teorico
#try except è una maniera di fare un modello di test e ritorno di resultati
#molto utile per verificare la presenza di errori nel codice
#try prova un codigo per un errore especificato
#except ti dà la possibilita di mettere una azione se succede l'errore 
#finally ti dà la possibilita di esecutare un codigo per qualsiasi resultato
# #else si può attaccare e ti dà la possibilita di mettere una azione se NON succede l'errore dopo l'esecuzione
# try:
#     k=3/0
#     print(k)

# except ZeroDivisionError:
#         print("Divisione per zero")
# else:
#     #esecuzione se k=3/numero differente di zero
#     print("è andato bene")
# finally:
#     print("Esecuzione del test")

#ex4 teorico
#lambda è una funzione senza un nome "ufficiale" in python (senza il def)
#serve per operazione matematiche e logiche senza il bisogno di richiamare la funzione
#buona per l'utilizzo unico, non serve per vari richiami
# list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# print(list(filter(lambda x: x%2==0, list_1)))

#ex5 teorico
#abbiamo due tipi di conversione, implicita ed esplicita
#l'implicita succede già nel interno del richiamo di una funzione, come il input()
#che tiene sempre una uscita in str, anche se si puo mettere int o bool dentro
#è utile per non avere perdita di informazione
#l'esplicita deve essere richiamata dell'utente, con il rischio di perdita di informazione
#pero con l'uscita nel modo che l'utente vuole, così lo aiutando per un codigo specifico
# s= "44"
# print(type(s))
# si = int(s)
# print(type(si))

#ex6 teorico
# LOOP: ci sono i loop FOR e WHILE, il primo esegue un'iterazione per ogni elemento di un iterabile mentre una dichiarazione è vera e si ferma quando l'iterazione è finita
# #invece il while esecuta una dichiarazione mentre vera fino ad quando la condizione si diventa falsa
# for i in range(3):
#     print(i)
# n = 0
# while n < 5: 
#     print(n) 
#     n += 1
#CONDIZIONI:
#un if è una condizione molto importante in python che esegue un codigo solo se la dichiarazione è vera
#else è eseguito se questa dichiarazione non è vera
# a = 5
# b = 20
# if b > a:
#   print("b maggiore di a")
# else:
#     ("b non maggiore di a")
#CLASSE
#classe è un modello definito per l'utente per la creazione di un oggetto
#è un modo di mettere insieme metodi e funzionalita, in un modo in cui
#una nuova classe crea un nuovo tipo di oggetto, con attributi e metodi per 
#definire e modificare questo oggetto
# class persona:
#   def __init__(self, nome, eta):
#     self.nome = nome
#     self.eta= eta

# p1 = persona("Boris", 30)

# print(p1.nome)
# print(p1.eta)
