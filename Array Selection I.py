A=[]
for i in range (100):
    value = float(input())
    A.append(value)
    if value <=10: 
        print('A[{}] = {}'.format(i,value))