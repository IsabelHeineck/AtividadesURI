C = 0
while C<1:
    X, Y = map(int,input().split()) 
    if X>Y:
        print("Decrescente")
    if Y>X:
        print("Crescente")
    if X==Y: 
        C+=1

    

