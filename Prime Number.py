N = int(input())
N+=1
for j in range(1,N):
    value = int(input())
    sum = 0
    for i in range(1, value+1): # Para i em uma distância de 1 a num + 1.
        if value % i == 0: # Se houver divisores sem resto, entre neste bloco e adicione +1 na variável sum.
            sum += 1
    if sum == 2: # Ao sair do laço for, verifique se sum é igual a 2. (Número divisivel por 1 e por ele mesmo).
        print(value,"eh primo")
    else: # Se for maior ou menor que 2, diga que não é primo.
        print(value,"nao eh primo")

    
                
      
           

                

