
Area =[
    [' * ', ' * ', ' * '],
    [' * ', ' * ', ' * '],
    [' * ', ' * ', ' * ']
      ]
Win = False
def WinnerCheck(win):
    for i in range(3):
        ShotColumn = 0
        ShotString = 0

        for g in range(3):
            if Area[i][g] == ' 0 ':
                ShotColumn += 1
            if Area[i][g] == ' X ':
                ShotColumn -= 1
            if Area[g][i] == ' 0 ':
                ShotString += 1
            if Area[g][i] == ' X ':
                ShotString -= 1
        if ShotColumn == -3 or ShotColumn == 3:
            print('     конец игры ')
            return True
        if ShotString == -3 or ShotString == 3:
            print('     конец игры ')
            return True
    if  Area[0][0] == ' X ' and Area [1][1] == ' X ' and Area [2][2] == ' X ' :
        print('конец игры ')
        return True
    elif Area[0][2] == ' X ' and Area [1][1] == ' X ' and Area [2][0] == ' X ' :
        print('конец игры ')
        return True
    elif Area[0][0] == ' O ' and Area[1][1] == ' O ' and Area[2][2] == ' O ':
        print('конец игры ')
        return True
    elif Area[0][2] == ' O ' and Area[1][1] == ' O ' and Area[2][0] == ' O ':
        print('конец игры ')
        return True
def Drow_Area(Area):
    for i in Area:
        print ('  ' , *i, '  ')
        print(' ')
    print('################################')
def Tern( tern  , win  ):
    if tern % 2 == 0:
        print('Ходят крестики')

    else:
        print('Ходят  нолики  ')

    if tern >=9:
        return True
def InP_Tern( tern , Str_ = 0 , Col_ = 0 ):
    Tern(tern , Win)
    Str_ = int(input('Выберете строку(1-3)')) - 1
    Col_ = int(input('Выберете колонку(1-3)'))  - 1
    if Area[Str_][ Col_] != ' * ':
        print(' Уже занятая ячейка ')
        print('################################')
        return
    elif tern % 2 == 0:
        Area[Str_][Col_]= ' X '
    else:
        Area[Str_][Col_] = ' O '
    tern += 1
    print('################################')
tern = 0
while True:

    InP_Tern(tern)
    Win = WinnerCheck(Win)
    tern += 1
    Drow_Area(Area)
    if Win == True:
        break

