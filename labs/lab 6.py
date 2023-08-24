import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")



def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board


if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    print("\n\n")

    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]

    print_board_and_legend(board)


#Part (a)

def put_X(square_num):
    if square_num >= 1 and square_num <= 9:
        row_number = (square_num-1)//3
        colomn_number = square_num - 3 * row_number - 1
        board[row_number][colomn_number] = "X"
    else:
        return "Index square_num out of range"


'''
if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)
    print("\n\n")
    square_num = 2
    put_X(square_num)
    print_board_and_legend(board)
'''

#Part (b)

def put_in_board(board,mark,square_num):
    if square_num >= 1 and square_num <= 9:
        board = board
        row_number = (square_num-1)//3
        colomn_number = square_num - 3 * row_number - 1
        if mark == "X":
            board[row_number][colomn_number] = "X"
        if mark == "O":
            board[row_number][colomn_number] = "O"
        else:
            return "Index mark out of range"
    else:
        return "Index square_num out of range"

'''
if __name__ == '__main__':
    board1 = make_empty_board()
    print_board_and_legend(board1)
    print("\n\n")
    put_in_board(board1,"X",6)
    print_board_and_legend(board1)
    put_in_board(board1,"O",5)
    print_board_and_legend(board1)
'''


#Part (c)

def ask_users_to_enter(board):
    global count
    if count % 2 == 0:
        input_X = input("Please enter coordinates for X: ",)
        input_X = int(input_X)
        put_in_board(board,"X",input_X)
        count += 1
    elif count % 2 == 1:
        input_O = input("Please enter coordinates for O: ",)
        input_O = int(input_O)
        put_in_board(board,"O",input_O)
        count += 1
'''
if __name__ == '__main__':
    board2 = make_empty_board()
    count = 0
    print_board_and_legend(board2)
    print("\n\n")
    ask_users_to_enter(board2)
    print_board_and_legend(board2)
    ask_users_to_enter(board2)
    print_board_and_legend(board2)
    ask_users_to_enter(board2)
    print_board_and_legend(board2)
'''

# 2 a

def get_free_squares(board):
    k = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" or board[i][j] == "O":
                continue
            else:
                k.append([i,j])
    return k

'''
if __name__ == '__main__':
    board3 = make_empty_board()
    count = 0
    print_board_and_legend(board3)
    put_in_board(board3,"X",1)
    put_in_board(board3,"X",4)
    put_in_board(board3,"X",8)
    put_in_board(board3,"O",2)
    put_in_board(board3,"O",5)
    print_board_and_legend(board3)
    print(get_free_squares(board3))
'''


# 2 b
import random

def make_random_move(board,mark):
    global count
    free_squares = get_free_squares(board)

    random_number = int(len(free_squares) * random.random())
    random_put = free_squares[random_number]
    row_number = random_put[0]
    colomn_number = random_put[1]

    board[row_number][colomn_number] = mark
    count += 1


'''

if __name__ == '__main__':
    make_random_move(board3,"O")
    print_board_and_legend(board3)
    make_random_move(board3,"O")
    print_board_and_legend(board3)
'''

# 2 c
'''
def computer_against_user(board):
    global count
    count = 0
    while count <= 9:
        if count <=6:
            ask_users_to_enter(board)
            print("\n\n")
            print_board_and_legend(board)
            print("\n\n")
            make_random_move(board,"O")
            print_board_and_legend(board)
            print("\n\n")
        if count == 8:
            ask_users_to_enter(board)
            print("\n\n")
            stop_game_when_win(board)
    return None


if __name__ == '__main__':
    board4 = make_empty_board()
    print_board_and_legend(board4)
    print("\n\n")
    computer_against_user(board4)
'''


# 3 a
def is_row_all_marks(board, row_i, mark):
    if board[row_i][0] == board[row_i][1] == board[row_i][2] == mark:
        return True
    else:
        return False
'''
if __name__ == '__main__':
    board = [["X", " ", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]
    print(is_row_all_marks(board, 0,"X"))
'''


# 3 b
def is_col_all_marks(board, col_i, mark):
    if board[0][col_i] == board[1][col_i] == board[2][col_i] == mark:
        return True
    else:
        return False

'''
if __name__ == '__main__':
    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "X", " "]]
    print(is_col_all_marks(board, 1,"X"))

'''


# 3 c
def is_dia_all_marks(board,mark):
    if board[0][0] == board[1][1] == board[2][2] == mark or \
    board[2][0] == board[1][1] == board[2][0] == mark:
        return True
    else:
        return False

def is_win(board,mark):
    for i in range(3):
        if is_col_all_marks(board,i,mark) == True or \
         is_row_all_marks(board,i,mark) == True or \
         is_dia_all_marks(board,mark) == True:
             return True
    else:
        return False

'''
if __name__ == '__main__':
    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "X", " "]]
    print(is_win(board,"X"))
'''

# 3 d
def stop_game_when_win(board):
    global count
    if is_win(board,"X") == True or is_win(board,"O") == True:
        count = 10
    return None
'''
def computer_against_user(board):
    global count
    count = 0
    while count <= 9:
        if count <=6:
            ask_users_to_enter(board)
            print("\n\n")
            print_board_and_legend(board)
            stop_game_when_win(board)
            print("\n\n")
            make_random_move(board,"O")
            print_board_and_legend(board)
            stop_game_when_win(board)
            print("\n\n")
        if count == 8:
            ask_users_to_enter(board)
            print("\n\n")
            stop_game_when_win(board)
    return None


if __name__ == '__main__':
    board4 = make_empty_board()
    print_board_and_legend(board4)
    print("\n\n")
    computer_against_user(board4)
'''

# 4 a
def try_win(board,mark):
    global count
    free_squares = get_free_squares(board)
    for i in range(len(free_squares)):
        test_put = free_squares[i]
        row_number = test_put[0]
        colomn_number = test_put[1]
        board[row_number][colomn_number] = mark
        if is_win(board,mark) == True:
            count += 1
            return None
        else:
            board[row_number][colomn_number] = " "
    if count % 2 == 1:
        make_random_move(board,mark)
        count

def computer_against_user(board):
    global count
    count = 0
    while count <= 9:
        print(count)




        if count % 2 == 0:
            ask_users_to_enter(board)

            stop_game_when_win(board)
            try_win(board,"O")


        print_board_and_legend(board)
        stop_game_when_win(board)
        print("\n\n")




    return None


if __name__ == '__main__':
    board5 = make_empty_board()
    print_board_and_legend(board5)
    print("\n\n")
    computer_against_user(board5)