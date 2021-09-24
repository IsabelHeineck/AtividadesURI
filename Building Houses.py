i=0
while i==0: 
    valor = input()
    if (valor=='0'): 
        break
    else: 
        A, B, C = map(int,valor.split())
        resultado = (A*B)
        resultado = (resultado*100)/C
        resultado = resultado**0.5
        print(int(resultado))
       

