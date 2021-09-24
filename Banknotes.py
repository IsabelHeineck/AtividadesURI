N = int(input())
J=N 
v1 = v2 = v5 = v10 = v20 = v50 = v100 = 0
while N>=100:
    N-=100
    v100+=1
while N>=50:
    N-=50
    v50+=1
while N>=20:
    N-=20
    v20+=1
while N>=10:
    N-=10
    v10+=1
while N>=5:
    N-=5
    v5+=1
while N>=2:
    N-=2
    v2+=1
while N>=1: 
    N-=1
    v1+=1
    
print(J)
print(v100, "nota(s) de R$ 100,00")
print(v50, "nota(s) de R$ 50,00")
print(v20, "nota(s) de R$ 20,00")
print(v10, "nota(s) de R$ 10,00")
print(v5, "nota(s) de R$ 5,00")
print(v2, "nota(s) de R$ 2,00")
print(v1, "nota(s) de R$ 1,00")

