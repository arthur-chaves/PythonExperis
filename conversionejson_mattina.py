#3 loops, um geral pra entrar no sistema e dois dentro, faz escrever um dado e insere no json
#se nao inseriu dado nao deixa dar load, se nao fez dump, nao da pra fazer load

#tenho que melhorar a parte do dumps e loads e no print, olhar no script dele
#output é a hora de carregar
#1
import json

lista1 = []
scelta1 = ""
while scelta1 != "END":
    scelta1 = input("cosa vuoi fare, scrivere, caricare? ")
    if scelta1 == "scrivere":
        entrata1 = input("Digita si se vuoi inserire un numero: ")
        while entrata1 == "si":
            entrata_s = input("Scrivi il suo numero: ")
            lista1.append(entrata_s)
            if entrata_s != "":
                y1 = json.dumps(lista1)
                entrada_p = input("+ un numero? ") 
                if entrada_p == "END":
                        break
                elif entrada_p == "si":
                        pass
                else:
                        print("Error")
                        break
            else:
                print("Deve inserire un dato")
                lista1.remove(entrata_s)
                continue
        
    elif scelta1 == "caricare":
        if len(lista1) !=0:
            entrata2 = input("Digita si se vuoi caricare la lista: ")
            while entrata2 == "si":
                if len(lista1) > 0:
                    y = json.dumps(lista1)
                    z = json.loads(y)
                    escolha_pos = input("posizione lista per print: ")
                    if escolha_pos == "END":
                        break
                    else:
                        print(z[int(escolha_pos)])
                else:
                    break
        else:
            print("Deve inserire un dato")
            break
                
        
#2 non ancora fatto

# dict1 = {}
# entrata1 = input("Digita scrivere se vuoi inserire una persona: ")

# while entrata1 == "si":
#     scelta1 = input("cosa vuoi fare, scrivere, caricare? ")
#     if scelta1 == "scrivere":
#         entrata_s = input("Scrivi il suo nome: ")
#         entrada_c = input("Scrivi il suo cognome")
#         dict1.update(entrata_s:entrada_c)
#         if entrata_s != "":
#         y1 = json.dumps(lista1)
#         y2 = json.loads(y1)
        
#         entrada_p = input("+ un numero? ") 
#         if entrada_p == "END":
#                 print(y2)
#                 break
#         elif entrada_p == "si":
#                 pass
#         else:
#                 print("Error")
#                 print(y2)
#                 break
#     else:
#         print("Deve inserire un dato")
#         lista1.remove(entrata_s)
#         continue

        
