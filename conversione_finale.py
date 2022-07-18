import json
import pickle
import pprint

#3 + 4
x_conv = input("Qual è il tipo di conversione? 1.Pickle, 2.Json ")
pyt=pickle
jsn =json
conv = ""
if x_conv=="1":
    conv = pyt
elif x_conv=="2":
    conv=jsn
a = {"a":11, "b":24, "c":11}
b = "siamo la classe migliore di"

# lista
if conv == pyt:
    y=conv.dumps(a)
    z=conv.loads(y)
    z["c"]=input("modifica c ")
    y1 = json.dumps(z)
    z2 = json.loads(y1)
    # print(z)
    # print(y1) sembra che la chiave non è riconosciuta e viene con "" invece di ''
    print(z2)
else:
    y=conv.dumps(a)
    z=conv.loads(y)
    f = input("modifica c ")
    z.update({"c":f})
    y2=pickle.dumps(z)
    z2=pickle.loads(y2)
    # print(z)
    # print(y2) viene una str undecoded, loads necessario
    print(z2)

#frase
j = conv.dumps(b)
k = conv.loads(j)
k = k + " " + input("migliore di dove? ")
print(k)