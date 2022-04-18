import random
list = ['oranje', 'blauw', 'groen', 'bruin']
def menm(mennmaantal):
    zakMM=[]
    for i in range(mennmaantal):
        zakMM.append(random.choice(list))
    zakMM.sort()
    return zakMM

menmaantal=int(input('hoeveel kleure M&M wilt u toevoegen aan de zak '))
zakMM = menm(menmaantal)
print(zakMM)
