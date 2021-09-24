lista_par = []
lista_impar = []
for j in range(15):
    value = int(input())
    if (value%2)!=0: 
        lista_impar.append(value)
    else:
        lista_par.append(value)
    if len(lista_impar) == 5: 
        for i in range(5): 
            print("impar[{}] = {}".format(i,lista_impar[i]))
        lista_impar = []
    if len(lista_par) == 5:
        for i in range(5): 
            print("par[{}] = {}".format(i,lista_par[i]))
        lista_par = []
    j+=1
for x in range (len(lista_impar)): 
    print("impar[{}] = {}".format(x,lista_impar[x]))
lsita_impar=[]
for x in range (len(lista_par)): 
    print("par[{}] = {}".format(x,lista_par[x])) 
lista_par=[]


        
  


