N=[]
for i in range (20):
    X = int(input())
    N.append(X)
a = N[::-1]
for j in range(20):
    print('N[{}] = {}'.format(j,a[j]))