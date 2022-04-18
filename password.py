import random

list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list3 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
list4 = ["@", "#", "$", "%", "&", "_", "?","."]
wachtwoord = []

def password():
    for i in range(6):
        wachtwoord.append(random.choice(list1))
    for i in range(8):
        wachtwoord.append(random.choice(list2))
    for i in range(7):
        wachtwoord.append(random.choice(list3))
    for i in range(3):
        wachtwoord.append(random.choice(list4))
    
    random.shuffle(wachtwoord)
    while (wachtwoord[0] in list4 or wachtwoord[0] in list3 or wachtwoord[1] in list3 or wachtwoord[2] in list3 or wachtwoord[23] in list4):
        random.shuffle(wachtwoord)
    
    return ''.join(wachtwoord)
    
print(password())
