import copy

def disp_board(board):
    for i in board:
        print(" ")
        for j in i:
            if j == "X" or j == "O":
                print(j, end="    ")
            else:
                print("#", end="    ")
        print("")

def make_move(board, move, player):
    idx = 0
    for i in range(3):
        for j in range(3):
            if idx == move:
                board[i][j] = player
                pass
            idx += 1
    return board

def eval_victory(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True, board[1][1]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True, board[1][1]

    for i in range(3):
        temp_lstx, temp_lsty = [], []
        for j in range(3):
            temp_lstx.append(board[i][j])
            temp_lsty.append(board[j][i])
        if (temp_lstx[0] == temp_lstx[1] and temp_lstx[1] == temp_lstx[2]) or (temp_lsty[0] == temp_lsty[1] and temp_lsty[1] == temp_lsty[2]):
            return True, board[i][i]
            break
    return False, None

def get_moves(board):
    ret_lst = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                ret_lst.append((i, j))
    return ret_lst

def get_pos(board, player):
    ret_lst = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == player:
                ret_lst.append((i, j))
    return  ret_lst

def check_win(board, player, moves_lst):
    win_moves = []
    for move in moves_lst:
        temp_board = copy.deepcopy(board)
        temp_board[move[0]][move[1]] = player
        result, _ = eval_victory(temp_board)
        if result:
            win_moves.append((move[0], move[1]))

    return win_moves

def max_utility(moves_lst):
    util_1, util_2, util_3 = [(1, 1)], [(0, 0), (0, 2), (2, 0), (2, 2)], [(0, 1), (1, 0), (1, 2), (2, 1)]
    ret_1, ret_2, ret_3 = [], [], []

    for move in moves_lst:
        if move in util_1:
            ret_1.append(move)
        if move in util_2:
            ret_2.append(move)
        if move in util_3:
            ret_3.append(move)

    ret = [ret_1, ret_2, ret_3]
    for r in ret:
        if len(r) > 0:
            return r[0]

def ask_ai(board, player, opponent):
    moves_lst = get_moves(board)
    player_pos = get_pos(board, player)
    opponent_pos = get_pos(board, opponent)

    win_pos = check_win(board, player, moves_lst)
    opp_win_pos = check_win(board, opponent, moves_lst)
    utility_pos = max_utility(moves_lst)

    if len(win_pos) > 0:
        return win_pos[0]
    else:
        if len(opp_win_pos) > 0:
            return opp_win_pos[0]
        else:
            return utility_pos

def start_match(user="X", ai="O", player="X"):
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

    for i in range(9):
        if player == user:
            move = int(input("enter position: "))
            board = make_move(board, move, user)
            disp_board(board)
            result, winner = eval_victory(board)
            if result:
                print("THE WINNER IS: " + player)
                break
            if i == 8:
                print("THE GAME IS A DRAW")
            player = ai
        elif player == ai:
            move = ask_ai(board, ai, user)

            print(move)
            # move = int(input("enter position: "))
            board = make_move(board, (3*move[0])+move[1], ai)
            disp_board(board)
            result, winner = eval_victory(board)
            if result:
                print("THE WINNER IS: " + player)
                break
            if i == 8:
                print("THE GAME IS A DRAW")
            player = user

start_match()
