N = int(input())
i = 0
j = 0
while i !=N:
    if i <= N: 
        valor1, valor2, valor3 = map(float,input().split())
        valor1 = valor1*2
        valor2 = valor2*3
        valor3 = valor3*5
        media = (valor1+valor2+valor3)/10
        print(f"{media:.1f}")
        j+=1
    i+=1



