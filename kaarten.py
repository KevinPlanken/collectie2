import random

deck = []
listone = ['harten', 'klaveren', 'schoppen','ruiten']
listtwo = ['2','3','4','5','6','7','8','9','10','boer','vrouw','heer','aas']
gekozen = []

def maakdeck():
    for color in listone:
        for number in listtwo:
            deck.append(color+' '+number)
    deck.append('joker 1')
    deck.append('joker 2')
    
def randomkaarten(aantal):
    for i in range(int(aantal)):
        kaart = random.choice(deck)
        gekozen.append(kaart)
        deck.remove(kaart)

maakdeck()
randomkaarten(7)
print(gekozen, deck)
