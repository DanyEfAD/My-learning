tern = 0
Area =[
    [' * ', ' * ', ' * '],
    [' * ', ' * ', ' * '],
    [' * ', ' * ', ' * ']
      ]
Win = False
def WinnerCheck(win = False):
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
        if ShotColumn == -2 or ShotColumn == 2:
            Print('конец игры ')
            win = True
        if ShotString == -2 or ShotString == 2:
            Print('конец игры ')
            win = True
    if  Area[0][0] == ' X ' and Area [1][1] == ' X ' and Area [2][2] == ' X ' :
        Print('конец игры ')
        win = True
    elif Area[0][2] == ' X ' and Area [1][1] == ' X ' and Area [2][0] == ' X ' :
        Print('конец игры ')
        win = True
    elif Area[0][0] == ' O ' and Area[1][1] == ' O ' and Area[2][2] == ' O ':
        Print('конец игры ')
        win = True
    elif Area[0][2] == ' O ' and Area[1][1] == ' O ' and Area[2][0] == ' O ':
        Print('конец игры ')
        win = True
def Drow_Area():
    for i in area:
        print (*i)
def Tern( tern , win ):
    if tern % 2 == 0:
        Print('Ходят крестики')
        tern += 1
    else:
        Print('Ходят  нолики  ')
        tern += 1
    if tern >=9:
        win = True
def InP_Tern(Str_, Col_, tern):
    Input('Выберете строку(1-3)', Str_)
    Input('Выберете колонку(1-3)', Col_)
    Str_ = Str - 1
    Col_ = Col - 1
    if Area(Str_, Col_) != ' * ':
        Print(' Уже занятая ячейка ')
    elif tern % 2 == 0:
        Area[Str_][Col_]= ' X '
    else:
        Area[StnerCheck(r_][Col_] = ' O '
while Win == False:
    Drow_Area()
    Tern()
    InP_Tern()
    Win = WinnerCheck()

