boodschappenlijst = {}
meerbestellen = "ja"

def zakkenvuller(naam, aantal):
    if naam in boodschappenlijst:
        aantal1 = boodschappenlijst.get(naam)
        boodschappenlijst[naam] = int(aantal)+int(aantal1)
    else:
        boodschappenlijst[naam] =  int(aantal)

while meerbestellen == "ja":
    naam = (input("Welk artikel wilt u toevoegen?: "))
    aantal = (input("Hoeveel wilt u van dit artikel?: "))
    meerbestellen = (input("Wilt u nog meer bestellen? (ja of nee): "))
    zakkenvuller(naam, aantal)
    
print(boodschappenlijst)