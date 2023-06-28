board =[["_","_","_"], ["_","_","_"], ["_","_","_"]]
for i in range(0,3) :
    for j in range(0,3):
        print(board[i][j], end="\t")
    print("\n")
d = "_"
player = "X"
while True :
    r = int(input("enter the row "))
    c = int(input("enter the col "))
    r -= 1
    c -= 1
    if board[r][c] == "_" :
        board[r][c] = player
    else :
        print("cell is already in use !")
        if player == "X" :
            player = "O"
        else : 
            player = "X"
    for i in range(0,3) :
        for j in range(0,3):
            print(board[i][j], end="\t")
        print("\n")
    for i in range(0,3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player :
            print(f"player {player} wins !")
            exit()
        elif board[i][0] == player and board[i][1] == player and board[i][2] == player :
            print(f"player {player} wins !")
            exit()
        elif board[0][0] == player and board[1][1] == player and board[2][2] == player :
            print(f"player {player} wins !")
            exit()
        elif board[0][2] == player and board[1][1] == player and board[2][0] == player :
            print(f"player {player} wins !")
            exit()
        elif d not in board[0] and d not in board[1] and d not in board[2] :
            print("draw")
            exit()
    if player == "X" :
        player = "O"
    else : 
        player = "X"

