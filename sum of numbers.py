number = int(input())
i=0
while number>0:
    account = number%10 
    number=(number)//10
    i+=account
print("A soma é:",i)
