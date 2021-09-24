X=int(input())
Y=int(input())
j=0
if X>Y:
    Y+=1
    for i in range(Y,X):
        if(i%2)!=0:
            j+=i
else:
    X+=1
    for i in range(X,Y):
         if(i%2)!=0:
            j+=i
print(j)