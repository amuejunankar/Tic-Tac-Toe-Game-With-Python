import os
clear = lambda: os.system('cls')
clear()

#above code is used to clear the terminal
#--------------------------------------
gameOn = True  
board = ['empty',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display_board():
    
    print(board[7]+'|'+ board[8]+'|'+board[9])
    print(board[4]+'|'+ board[5]+'|'+board[6])
    print(board[1]+'|'+ board[2]+'|'+board[3])

Player1 = ""
Player2 = ""

def playerChoice():
    global Player1, Player2
    selection = True
    
    while ( selection == True):
        Player1 = input("Player 1: X or O = ")
        if ( Player1.lower() == 'x'):
            Player1 = "X"
            Player2 = "O"
            selection = False
        elif (Player1.lower() == 'o'):
            Player1 = "O"
            Player2 = "X"
            selection = False
        else:
            print("Please Enter Either X or O")

def position_choice(PlayerName):
    LoopRun = True
    while LoopRun:
        
        choice = input(f"{PlayerName}, pick a position (1-9) ")
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("<> Sorry, invalid choice! ")
        else:
            if board[int(choice)] == " ":
                return int(choice)
            else:
                clear()
                print("Already marked!, Choose Another Available Position")
                display_board()

def player_input():
    
    for i in range(1,6):
        #Player 1
        P1 = position_choice("Player 1")
        board[P1] = "X"  # Update Board and Display
        display_board()
        if checkGame(Player1): ## check if win or not 
            break
        
        
        # Player 2
        P2 = position_choice("Player 2")
        board[P2] = "O" # Update Board and Display
        display_board()
    
        if checkGame(Player2): ## check if win or not
            break

def checkGame(PlayerValueXorO):
    global gameOn
    
    # Check horizontal lines
    if ((board[1] == board[2] == board[3] == PlayerValueXorO) or
        (board[4] == board[5] == board[6] == PlayerValueXorO) or
        (board[7] == board[8] == board[9] == PlayerValueXorO)):
        print("\n----------------------------------")
        print(f"{PlayerValueXorO} Won The Game")
        print("----------------------------------")
        gameOn = False
        return True
    
    # Check vertical lines
    elif ((board[1] == board[4] == board[7] == PlayerValueXorO) or
          (board[2] == board[5] == board[8] == PlayerValueXorO) or
          (board[3] == board[6] == board[9] == PlayerValueXorO)):
        
        print("\n----------------------------------")
        print(f"{PlayerValueXorO} Won The Game")
        print("----------------------------------")        
        gameOn = False
        return True
        
    # Check diagonals
    elif ((board[1] == board[5] == board[9] == PlayerValueXorO) or
          (board[3] == board[5] == board[7] == PlayerValueXorO)):
        
        print("\n----------------------------------")
        print(f"{PlayerValueXorO} Won The Game")
        print("----------------------------------")        
        gameOn = False
        return True
      
## Function calling
playerChoice()
clear()

while gameOn:
    display_board()
    player_input()
    
        
        




