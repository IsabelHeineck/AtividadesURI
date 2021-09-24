i = 0 
N = int(input())
while i<=N: 
    if (i%2)==0:
        exp = 2**i
        print(f"{i}^2 = {exp}")
    i+=1

