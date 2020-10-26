import random

#Defining global varibales

board=[[' ',' ',' '],
       [' ',' ',' '],
       [' ',' ',' ']]

player1='X'
player2='O'
player=1

def display_board():
    for i in range(3):
        for j in range(3):
            print(" {} ".format(board[i][j]),end='')
            if j < 2:
                print("|",end='')
        print()
        if i < 2:
            print("___________")
    print()


#Taking user input for the choice of character from both users

def user_character_choice():
    allowed_inputs=['X','O']
    print('Player 1 : Enter your character choice (X or O) : ',end='')
    choice=input()

    while choice not in allowed_inputs:
        print('Player 1 : Please enter a valid character choice (X or O) : ',end='')
        choice=input()

    return choice


#This function takes user input for the position to fill

def user_input():
    allowed_inputs=list(map(lambda num: str(num),range(1,10)))
    #allowed_inputs=list(range(1,10))
    #print(allowed_inputs)
    print('Player {} : Enter your position (1-9) : '.format(player),end='')
    position=input()

    while position not in allowed_inputs:
        print('Player {} : Please enter a valid position (1-9) : '.format(player),end='')
        position=input()

    return int(position)



#This function updates the board according to user input

def update_board(position):
    #print(player)
    position -= 1
    row=int(position/3)
    col=int(position%3)
    #print("ROW : {}, COL : {}".format(row,col))

    if board[row][col] == 'X' or board[row][col] == 'O':
        return False

    if player == 1:
        board[row][col] = player1
    else:
        board[row][col] = player2


#This function checks winning condition & declares a winner if condition is satisfied

def check_win():

    #check row state
    for i in range(0,3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and (board[i][0]=='X' or board[i][0]=='O'):
            if board[i][0] == player1:
                return player1
            else:
                return player2

    #check column state
    for i in range(0,3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and (board[0][i]=='X' or board[0][i]=='O'):
            if board[0][i] == player1:
                return player1
            else:
                return player2

    #check diagonal 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and (board[1][1]=='X' or board[1][1]=='O'):
        if board[1][1] == player1:
            return player1
        else:
            return player2

    #check diagonal 2
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and (board[1][1]=='X' or board[1][1]=='O'):
        if board[1][1] == player1:
            return player1
        else:
            return player2

    #return false for no winner
    return False



#This function resets the board state before starting the game

def reset_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '


#This function starts the game

def run_game():
    #Reset board state
    reset_board()

    #Define that global variable will be modfied by default
    global player,player1,player2

    #Take character input for player 1
    player1 = user_character_choice()

    #Assign other character to player 2
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print("Player 2 gets {}".format(player2))

    #RESET GLOBAL VARIABLE TO 1
    player = random.randint(1,2)

    print("Starting with player : {}".format(player))

    #Initialise with number of inputs to 0
    inputs=0

    #display initial board
    display_board()

    while check_win() == False and inputs < 9:
        #Take user input for {player}
        position=user_input()

        #Update the board based on user input
        res=update_board(position)

        #check whether the position was already filled
        if res == False:
            print("Position already filled !!!")
            continue

        #Display updated board to user
        display_board()

        #change current player
        if player == 1:
            player=2
        else:
            player = 1

        #Increment input
        inputs += 1

    if check_win() == player1:
        print("We have a winner :  Player1 {}".format(player1))
    elif check_win() == player2:
        print("We have a winner :  Player2 {}".format(player2))
    else:
        print("Match is Draw!!!")

    print()

def start_game():
    print("############ Welcome to Tic-Tac-Toe ################")

    play_again="Y"

    while play_again == "Y" or play_again == "y":
        run_game()
        play_again=input("Do you want to play again : ")

    print("Good Bye!!!")


start_game()
