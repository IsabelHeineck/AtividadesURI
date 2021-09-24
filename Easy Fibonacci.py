N = int(input())
value = 0
i = 0
cont = 0
j = 0
frase = ""
while cont<N:
    if(value<1) :
        value = value + i
        i=1
        frase += str(value) + " "
        cont+=1
    if(j>1):
        frase += str(value) + " "
        aux = value
        value = value+i
        i=aux
        cont+=1
    if cont==N:
        break
    j+=1
print(frase.rstrip(" "))

    
    
    
