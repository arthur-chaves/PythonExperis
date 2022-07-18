import json
import pickle
import pprint

#4
x_conv = input("Qual è il tipo di conversione? 1.Json, 2. Pickle ")
pyt=pickle
jsn =json
conv = ""
if x_conv=="1":
    conv = pyt
elif x_conv=="2":
    conv=jsn
a = {"a":11, "b":24, "c":11}
b = "siamo la classe migliore di"

#lista
if conv == pyt:
    y=conv.dumps(a)
    z=conv.loads(y)
    z["c"]=input("modifica c ")
    pprint.pprint(z)
else:
    y=conv.dumps(a)
    z=conv.loads(y)
    f = input("modifica c ")
    z.update({"c":f})
    print(z)

#frase
j = conv.dumps(b)
k = conv.loads(j)
k = k + " " + input("una frase ")
print(k)
