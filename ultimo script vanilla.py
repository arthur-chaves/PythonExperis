
from turtle import pos
import json
import pickle

#ex1 
# x1 = int(input("Valore 1: "))
# x2 = int(input("Valore 2: "))
# class conta():
#     def __init__(self, entrada, plus):
#         self.entrada = entrada
#         self.plus = plus
    
#     def criaconta(self):
#             self.entrada = x1
#             self.plus = x2
#             s = self.entrada - self.plus
#             if s >= 0:
#                 a1 = figliop(self.entrada, self.plus)
#                 a1.printpos()
#             elif s < 0:
#                 a2 = figlion(self.entrada, self.plus)
#                 a2.printneg() 
#             else:
#                 print("error")

# class positivo(conta):
#     def __init__(self, entrada, plus):
#         conta.__init__(self, entrada, plus) 
#         self.totale = entrada-plus

# class figliop(positivo):
#     def __init__(self, entrada, plus):
#         positivo.__init__(self,entrada, plus)
#     def printpos(self):
#         print("Diff. positiva, distanza uguale a")    
#         print(self.totale)
        

# class negativo(conta):
#     def __init__(self, entrada, plus):
#         conta.__init__(self, entrada, plus)
#         self.totale = plus-entrada

# class figlion(negativo):
#     def __init__(self, entrada, plus):
#         negativo.__init__(self,entrada, plus)
#     def printneg(self):
#         print("Diff. negativa, distanza uguale a")    
#         print(self.totale)   

# f = conta(x1,x2)
# f.criaconta()


#ex2 
msgpos = "Diff. positiva, distanza uguale a"
msgneg = "Diff. negativa, distanza uguale a"
class conta():
    list1=[]

    def __init__(self, entrada, plus):
        self.entrada = entrada
        self.plus = plus
        self.list1=[entrada,plus]
    def criaconta(self):
            s = x1-x2
            if s >= 0:
                a1 = figliop(self.entrada, self.plus)
                a1.printpos()
            elif s < 0:
                a2 = figlion(self.entrada, self.plus)
                a2.printneg() 
            else:
                print("error")

class positivo(conta):
    def __init__(self, entrada, plus):
        conta.__init__(self, entrada, plus) 
        self.totale = entrada-plus

class figliop(positivo):
    def __init__(self, entrada, plus):
        positivo.__init__(self,entrada, plus)
    def printpos(self):
        msgpos = "Diff. positiva, distanza uguale a"
        print(msgpos)    
        print(self.totale)
        

class negativo(conta):
    def __init__(self, entrada, plus):
        conta.__init__(self, entrada, plus)
        self.totale = plus-entrada

class figlion(negativo):
    def __init__(self, entrada, plus):
        negativo.__init__(self,entrada, plus)
    def printneg(self):
        print(msgneg)    
        print(self.totale)

class pck(conta):
    def __init__(self):
        y=pickle.dumps(f.list1)
        z1=pickle.loads(y)
        print(z1)

class js(conta):
    def __init__(self):
        y=json.dumps(f.list1)
        z2=json.loads(y)
        print(z2)

g = int(input("Quante volte? "))
for g in range(g):
    x1 = int(input("Valore 1: "))
    x2 = int(input("Valore 2: "))
    f = conta(x1,x2)
    f.criaconta()
    x_conv = int(input("Qual è il tipo di conversione? 1.Pickle, 2.Json "))
    if x_conv == 1:
        pck()
    elif x_conv == 2:
        js()
    else:
        print("Error")

# #3 devo mettere il print fuori ma sono bloccato
# class dict():
#     def __init__(self):
#         self.dict1={}


# class Riempidict(dict):
#     def __init__(self):
#         dict.__init__(self)
#         p = input("Quante volte? ")
#         for i in range(int(p)):
#             k1 = input ("Qual'è la chiave? ")
#             l1 = input ("Qual'è il valore? ")
#             self.dict1.update({k1:l1})
#             # print(self.dict1)
            

# class printdict(dict):
#     def __init__(self):
#         dict.__init__(self)
    




