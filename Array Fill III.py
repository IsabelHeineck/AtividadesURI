N=[]
X = float(input())
for i in range (100):
    N.append(X)
    print('N[{}] = {:.4f}'.format(i,N[i]))
    X = X/2