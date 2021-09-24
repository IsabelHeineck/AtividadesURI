N = int(input())
N+=1
fem = masc = sumExp = sum = media = sumAge = 0
for i in range(1,N):
    age = int(input())
    sex = input()
    experience = input()
    if experience == "s":
        sum+=1
        sumAge+=age
        media = sumAge/sum
        if sex == "f": 
            fem+=1
        else: 
            masc+=1
        if (age<35) and (experience =="s"): 
            sumExp+=1
print("feminino: ",fem)
print("masculino: ",masc)
print("Número de candidatos com idade inferior a 35 anos e com experiência: ",sumExp)
print("Idade média dos candidatos que já têm experiência no serviço: ",media)
    
    


