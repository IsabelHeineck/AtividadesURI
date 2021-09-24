i=1
biggerNum = 0
fat=1
for j in range(5):
  N = int(input())
  if N > biggerNum:
    biggerNum = N
while i<=biggerNum:
  fat=fat*i
  i+=1
print(f"{biggerNum}! = {fat}")






