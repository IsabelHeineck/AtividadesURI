a = 1
b = 0 
lista = [0,1]
T = int(input())
for i in range(60):
    c = a+b
    b = a 
    a = c 
    lista.append(c)
for i in range (T): 
    value = int(input())
    print('Fib({}) = {}'.format(value,lista[value]))
    
