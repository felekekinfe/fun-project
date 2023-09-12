
board=['_','_','_',
       '_','_','_',
       '_','_','_']
game_still_going=True
winner=None
current_player='X'

def display_board():
    print(board[0]+' | '+board[1]+' | '+board[2])
    print(board[3]+' | '+board[4]+' | '+board[5])
    print(board[6]+' | '+board[7]+' | '+board[8])

def play_game():
    global winner
    #display initial board
    display_board()
    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()
           
        flip_player()
    # while game_still_going:
    #      handle_turn(current_player)

    #     if check_if_game_over():
    #         break

    #     flip_player()
    if winner=='X' or winner=='O':
        print(winner + ' won. ')
    
    elif winner==None:
        print('Tie')


def handle_turn(player):
    position=int(input('choose a position from 1-9: '))-1

    board[position]=player
    display_board()
    

def check_if_game_over():
    check_win()
    check_tie()

def check_win():
    global winner
    #check rows
    row_winner=check_rows()  
    #check columns
    column_winner=check_columns()
    #check diagonals
    diagonal_winner=check_diagonal()

    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None

    return

def check_rows():
    global game_still_going

    row1=board[0]==board[1]==board[2] !='_'
    row2=board[3]==board[4]==board[5] !='_'
    row3=board[6]==board[7]==board[8] !='_'

    if row1 or row2 or row3:
        game_still_going=False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]

def check_columns():
    global game_still_going

    col1=board[0]==board[3]==board[6] !='_'
    col2=board[1]==board[4]==board[7] !='_'
    col3=board[2]==board[5]==board[8] !='_'
   
    if col1 or col2 or col3:
        game_still_going=False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]

def check_diagonal():
    global game_still_going

    diagonal1=board[0]==board[4]==board[8] !='_'
    diagonal2=board[2]==board[4]==board[6] !='_'

    if diagonal1 or diagonal2:
        game_still_going=False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]

        
    else:
        return False
    

def check_tie():
    global game_still_going,board

    if '_' not in board:
        game_still_going=False


   

def flip_player():
    global current_player
    if current_player=="X":
        current_player='O'
    elif current_player=='O':
        current_player='X'
    return

play_game()