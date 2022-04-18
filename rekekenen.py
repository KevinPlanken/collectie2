listone = ['1','2','3','4','5','6','7','8','9','10',]
listtwo = ['2','4','6','8','10','12','14','16','18','20',]

def addAndDisplayLists (listone, listtwo):
    result1 =[]
    for i in range (len(listone)):
        result1.append(int(listone[i]) + int(listtwo[i]))
    return result1

for i in range (len(listone)):
    print(f'{listone[i]} + {listtwo[i]} = {addAndDisplayLists(listone, listtwo)[i]}')

def addAndDisplayLists (listone, listtwo):
    result1 =[]
    for i in range (len(listone)):
        result1.append(int(listone[i]) - int(listtwo[i]))
    return result1

for i in range (len(listone)):
    print(f'{listone[i]} - {listtwo[i]} = {addAndDisplayLists(listone, listtwo)[i]}')

def addAndDisplayLists (listone, listtwo):
    result1 =[]
    for i in range (len(listone)):
        result1.append(int(listone[i]) * int(listtwo[i]))
    return result1

for i in range (len(listone)):
    print(f'{listone[i]} * {listtwo[i]} = {addAndDisplayLists(listone, listtwo)[i]}')

def addAndDisplayLists (listone, listtwo):
    result1 =[]
    for i in range (len(listone)):
        result1.append(int(listone[i]) / int(listtwo[i]))
    return result1

for i in range (len(listone)):
    print(f'{listone[i]} / {listtwo[i]} = {addAndDisplayLists(listone, listtwo)[i]}')