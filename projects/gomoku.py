def is_empty(board):
    for i in range(len(board)-1):
        for j in range(len(board[i])-1):
            if board[i][j] != " ":
                return False
    return True

def on_edge(board,y,x):
    if y == len(board)-1 or x == len(board[y])-1 or y == 0 or x == 0:
        return True
    else:
        return False

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    y_start = y_end - length * d_y + d_y
    x_start = x_end - length * d_x + d_x
    y_pbs = y_end - length * d_y
    x_pbs = x_end - length * d_x         # position_before_start
    y_pae = y_end + d_y
    x_pae = x_end + d_x                  # position_after_end

    start_on_edge = on_edge(board,y_start,x_start)
    end_on_edge = on_edge(board,y_end,x_end)

    if start_on_edge == True:
        if end_on_edge == True:
            return 'CLOSED'
        elif end_on_edge == False:
            if board[y_pae][x_pae] == " ":
                return 'SEMIOPEN'
            else:
                return 'CLOSED'

    elif start_on_edge == False:
        if end_on_edge == True:
            if board[y_pbs][x_pbs] == " ":
                return 'SEMIOPEN'
            else:
                return 'CLOSED'

        elif end_on_edge == False:
            if board[y_pbs][x_pbs] == " ":
                if board[y_pae][x_pae] == " ":
                    return 'OPEN'
                else:
                    return 'SEMIOPEN'
            else:
                if board[y_pae][x_pae] == " ":
                    return 'SEMIOPEN'
                else:
                    return 'CLOSED'

def sequence_is_valid(board, col, y_start, x_start, length, d_y, d_x):
    if x_start<0 or x_start>7 or x_start+(length-1)*d_x<0 or \
    x_start+(length-1)*d_x>7 or y_start<0 or y_start>7 \
    or y_start+(length-1)*d_y>7 or y_start+(length-1)*d_y<0:
        return False

    for i in range(length):
        if board[y_start+i*d_y][x_start+i*d_x] != col:
            return False
    return True


def sequence_is_complete(board, col, y_start, x_start, length, d_y, d_x):
    if sequence_is_valid(board, col, y_start, x_start, length, d_y, d_x)\
    == False:
        return False

    elif sequence_is_valid(board, col, y_start, x_start, length, d_y, d_x)\
    == True:
        if on_edge(board,y_start,x_start) == False:
            if on_edge(board,y_start+(length-1)*d_y,\
            x_start+(length-1)*d_x) == False:
                if board[y_start-d_y][x_start-d_x] == col or \
                board[y_start+length*d_y][x_start+length*d_x] == col:
                    return False
                else:
                    return True

            elif on_edge(board,y_start+(length-1)*d_y,\
            x_start+(length-1)*d_x) == True:

                if board[y_start-d_y][x_start-d_x] == col:
                    return False
                else:
                    return True

        if on_edge(board,y_start,x_start) == True:
            if on_edge(board,y_start+(length-1)*d_y,\
            x_start+(length-1)*d_x) == False:
                if board[y_start+length*d_y][x_start+length*d_x] == col:
                    return False
                else:
                    return True
            else:
                return True

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0
    for i in range(len(board)-length+1):
        y_i = y_start + i * d_y
        x_i = x_start + i * d_x
        if sequence_is_complete(board, col, y_i, x_i,length,\
        d_y, d_x) == True:
            y_end_i = y_i + (length-1) *d_y
            x_end_i = x_i + (length-1) *d_x
            if is_bounded(board,y_end_i,x_end_i,length,d_y,d_x) == 'OPEN':
                open_seq_count += 1
            elif is_bounded(board,y_end_i,x_end_i,length,d_y,d_x) == \
            'SEMIOPEN':
                semi_open_seq_count += 1
    return open_seq_count, semi_open_seq_count



def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(len(board)):
        v_open,v_semi = detect_row(board,col,0,i,length,1,0) #vertical
        h_open,h_semi = detect_row(board,col,i,0,length,0,1) #horizontal
        open_seq_count += v_open
        open_seq_count += h_open
        semi_open_seq_count += v_semi
        semi_open_seq_count += h_semi

    for i in range(len(board)):
    # diagonal to the right, search from (0,0) to (0,7)
        dia_r_open1,dia_r_semi1 = detect_row(board,col,0,i,length,1,1)
        open_seq_count += dia_r_open1
        semi_open_seq_count += dia_r_semi1

    for i in range(len(board)-1):
    # diagonal to the right, search from (1,0) to (7,0)
        dia_r_open2,dia_r_semi2 = detect_row(board,col,i+1,0,length,1,1)
        open_seq_count += dia_r_open2
        semi_open_seq_count += dia_r_semi2


    for i in range(len(board)):
    # diagonal to the left, search from (0,0) to (0,7)
        dia_l_open1,dia_l_semi1 = detect_row(board,col,0,i,length,1,-1)
        open_seq_count += dia_l_open1
        semi_open_seq_count += dia_l_semi1

    for i in range(len(board)-1):
    # diagonal to the left, search from (1,7) to (7,7)
        dia_l_open2,dia_l_semi2 = detect_row(board,col,i+1,7,length,1,-1)
        open_seq_count += dia_l_open2
        semi_open_seq_count += dia_l_semi2

    return open_seq_count, semi_open_seq_count


def search_empty(board):
    empty_block = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                empty_block.append([i,j])
    return empty_block



def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def search_max(board):
    score_initial= -1000000
    List_empty_postion = search_empty(board)
    for i in range(len(List_empty_postion)):
        board[List_empty_postion[i][0]][List_empty_postion[i][1]]\
        = "b"
        score_final = score(board)
        board[List_empty_postion[i][0]][List_empty_postion[i][1]]\
        = " "
        if score_final >= score_initial:
            score_initial = score_final
            move_y = List_empty_postion[i][0]
            move_x = List_empty_postion[i][1]
    return move_y, move_x

def is_win(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if sequence_is_complete(board,'w',i,j,5,0,1) == True or \
            sequence_is_complete(board,'w',i,j,5,1,1) == True or \
            sequence_is_complete(board,'w',i,j,5,1,0) == True or \
            sequence_is_complete(board,'w',i,j,5,1,-1) == True:
                return "White won"

            elif sequence_is_complete(board,'b',i,j,5,0,1) == True or \
            sequence_is_complete(board,'b',i,j,5,1,1) == True or \
            sequence_is_complete(board,'b',i,j,5,1,0) == True or \
            sequence_is_complete(board,'b',i,j,5,1,-1) == True:
                return "Black won"

    L = search_empty(board)
    if len(L) == 0:
        return "Draw"
    else:
        return "Continue playing"






def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))



def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    play_gomoku(8)
