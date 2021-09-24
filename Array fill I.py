N=[]
value = int(input())
for i in range (10):
    N.append(value)
    print('N[{}] = {}'.format(i,N[i]))
    value = value*2