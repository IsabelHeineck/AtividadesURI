i = 0 
contador = 0 
addiction = 0
while i<6: 
    valor = float(input())
    if valor>=0: 
        addiction = addiction +valor
        contador+=1
    i+=1
addiction = addiction/contador   
print(f"{contador} valores positivos") 
print(f"{addiction:.1f}")

