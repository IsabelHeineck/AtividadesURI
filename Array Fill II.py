N = []
T = int(input())
for i in range(1000): 
    x = 0
    while x<T:
        N.append(x)
        x+=1
    print("N[{}] = {}".format(i,N[i]))
        