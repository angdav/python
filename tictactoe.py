# tic tac toe

board = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
        ]

def over():
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != "-":
        return True
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != "-":
        return True
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != "-":
        return True
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != "-":
        return True
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != "-":
        return True
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != "-":
        return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return True
    return False

def printboard():
    for lst in board:
        for val in lst:
            print(str(val)+" ", end="")
        print()
    

while not over():

    printboard()

    xrow = -1
    xcol = -1
    orow = -1
    ocol = -1

    while True:
        while xrow < 0 or xrow > 3:
            try:
                xrow = int(input("enter row for X: "))
                if xrow > 3 or xrow < 1:
                    print("invalid input!")
                    continue
            except:
                print("invalid input!")
        while xcol < 0 or xcol > 3:
            try:
                xcol = int(input("enter col for X: "))
                if xcol > 3 or xcol < 1:
                    print("invalid input!")
                    continue
            except:
                print("invalid input!")
        if board[xrow-1][xcol-1] == "-":
            break
        print("that spot is already occupied, try again")
        xrow = -1
        xcol = -1
       
    board[xrow-1][xcol-1] = 'X'
    if over():
        break

    printboard()

    while True:
        while orow < 0 or orow > 3:
            try:
                orow = int(input("enter row for O: "))
                if orow > 3 or orow < 1:
                    print("invalid input!")
                    continue
            except:
                print("invalid input!")
        while ocol < 0 or ocol > 3:
            try:
                ocol = int(input("enter col for O: "))
                if ocol > 3 or ocol < 1:
                    print("invalid input!")
                    continue
            except:
                print("invalid input!")
        if board[orow-1][ocol-1] == "-":
            break
        print("that spot is already occupied, try again")
        orow = -1
        ocol = -1

       
    board[orow-1][ocol-1] = 'O'

print("game over!")
printboard()