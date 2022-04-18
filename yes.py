import random 

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']
def spelProgramma(spelList, minimum, maximum):
    rondom=random.choice(range(minimum, maximum))
    for i in range (rondom):
        print(random.choice(spelList))

spelProgramma(spelList, 3, 7)