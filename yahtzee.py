import random

def rollen(dice):
    print('de nummers zijn ', end = '')
    for d in dice:
        print(str(d) + ' ',end='')

score = 0
score_lijst =[]
    

game_over = False 
while not game_over:
    dice = []
    for d in range(5):
        dice.append(random.randint(1,6)) 
    
    rollen(dice)
    for x in range (3):
        reroll = input('wat wil je opnieuw rollen? ')
        reroll = reroll.split()
        for index, ch in enumerate(reroll):
            reroll[index] = int(ch) - 1
    
        for index in reroll:
           dice[index] = random.randint(1,6)
    
        rollen(dice)

    number = False 
    while not number:
        nummer_score = int(input('welk nummer wil je scoren? '))

        if number not in score_lijst:
            number = True  
        else:
            print('je hebt dat al gegooid. ')

    score_lijst.append(nummer_score)

    for d in dice:
        if d == nummer_score: 
            score += d
    print('jou score is ' + str(score))
 
    if len (score_lijst) == 6:
        game_over = True 
        
