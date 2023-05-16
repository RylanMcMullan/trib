board = [
    [' , ',' , ',' , ',' , ',' , ',' , ',' , '],
    [' , ',' , ',' , ',' , ',' , ',' , ',' , '],
    [' , ',' , ',' , ',' , ',' , ',' , ',' , '],
    [' , ',' , ',' , ',' , ',' , ',' , ',' , '],
    [' , ',' , ',' , ',' , ',' , ',' , ',' , '],
    [' , ',' , ',' , ',' , ',' , ',' , ',' , '],
]
turn = " X "
game = True
#displays the board
def display_board():
    print(" 1, 2, 3, 4, 5, 6, 7")
    print("|", end = "")
    for i in range(len(board)):
        for j in range(7):
            print(board[i][j], end="")
        print("|")
        print("_______________________")
        if i==5:
            print(f"It is now {turn}'s turn")
        else:
            print("|", end = "")
#runs the turns foor each player. Puts the piece at the bottom of the board
def player_turn():
    global turn
    try:
        player_input = int(input("What column do you choose? "))
    except:
        print("Select a number between 1 & 8")
        player_input = int(input("What column do you choose? "))
    if player_input > 7 or player_input < 1:
        print("Please enter a number betwen 1 & 7, if you don't the program will break")
        player_input = int(input("What column do you choose? "))
    if board[5][player_input-1] == ' , ':
        board[5][player_input-1] = turn
    elif board[4][player_input-1] == ' , ':
        board[4][player_input-1] = turn
    elif board[3][player_input-1] == ' , ':
        board[3][player_input-1] = turn
    elif board[2][player_input-1] == ' , ':
        board[2][player_input-1] = turn
    elif board[1][player_input-1] == ' , ':
        board[1][player_input-1] = turn
    elif board[0][player_input-1] == ' , ':
        board[0][player_input-1] = turn
    else:
        print("Choose another spot")
    #Next players turn
    if(turn == " X "):
        turn = " 0 "
    else:
        turn = " X "
    """
    This funtion needs updated. It should check for horizontal, vertical,
    and diagonal. Once one player has 4 in a row, update game to false.
    You can earn 90% of the points if you can get vertical and horizontal.
    """
def check_win():
    game = True #This is here to allow the program to run, it needs removed
    #This function prints the board, runs each player, and checks for win
    #if game is false, the game should stop and the player should be pronounced
    connect = []
    for i, row in enumerate(board): # get data from every row
        for j, value in enumerate(board[i]): # get data from each object in row
            # check for a vertical set of 4
            # for x
            if board[i][j] == " X " and board[i+1][j] == " X " and board[i+2][j] == " X " and board[i+3][j] == " X ": 
                game = False
            # for 0
            if board[i][j] == " 0 " and board[i+1][j] == " 0 " and board[i+2][j] == " 0 " and board[i+3][j] == " 0 ":
                game = False
            # check for a horizontal set of 4
            # for x
            if value == " X ":
                if j > 0 and board[i][j-1] != " X ":
                    connect.clear
                else:
                    connect.append(j)
                    print(f"X: {connect}")
            # for 0
            elif value == " 0 ":
                if j > 0 and board[i][j-1] != " 0 ":
                    connect.clear
                else:
                    connect.append(j)
                    print(f"0: {connect}")

def run_game():
    global game
    while(game == True):
        display_board()
        player_turn()
        check_win()
        if game == False:
            break
            print("A player won the game? I wonder who...?")
#MAIN BODY OF THE PROGRAM
run_game()