import copy
##Functions for minimax Testing
##############################################################
#Flip Functions
##############################################################
def flip_left(pos, board, player, size):
    x, y = pos
    opo = ''
    toFlip = []
    if player == 'W':
        opo = 'B'
    else:
        opo = 'W'
    x -= 1
    while x > 0:
        if board[y][x] == ' ':
            return board
        elif board[y][x] == opo:
            toFlip.append((x,y))
        elif board[y][x] == player:
            for i in toFlip:
                x, y = i
                board[y][x] = player
            return board
        x -= 1
    return board

def flip_right(pos, board, player, size):
    x, y = pos
    opo = ''
    toFlip = []
    if player == 'W':
        opo = 'B'
    else:
        opo = 'W'
    x += 1
    while x < size:
        if board[y][x] == ' ':
            return board
        elif board[y][x] == opo:
            toFlip.append((x,y))
        elif board[y][x] == player:
            for i in toFlip:
                x, y = i
                board[y][x] = player
            return board
        x += 1
    return board
def flip_up(pos, board, player, size):
    x, y = pos
    opo = ''
    toFlip = []
    if player == 'W':
        opo = 'B'
    else:
        opo = 'W'
    y -= 1
    while y > 0:
        if board[y][x] == ' ':
            return board
        elif board[y][x] == opo:
            toFlip.append((x,y))
        elif board[y][x] == player:
            for i in toFlip:
                x, y = i
                board[y][x] = player
            return board
        y -= 1
    return board

def flip_down(pos, board, player, size):
    x, y = pos
    opo = ''
    toFlip = []
    if player == 'W':
        opo = 'B'
    else:
        opo = 'W'
    y += 1
    while y < size:
        if board[y][x] == ' ':
            return board
        elif board[y][x] == opo:
            toFlip.append((x,y))
        elif board[y][x] == player:
            for i in toFlip:
                x, y = i
                board[y][x] = player
            return board
        y += 1
    return board

def flip_l_diag_down(pos, board, player, size):
    x, y = pos
    opo = ''
    toFlip = []
    if player == 'W':
        opo = 'B'
    else:
        opo = 'W'
    x -= 1
    y += 1
    while x > 0 and y < size:
        if board[y][x] == ' ':
            return board
        elif board[y][x] == opo:
            toFlip.append((x,y))
        elif board[y][x] == player:
            for i in toFlip:
                x, y = i
                board[y][x] = player
            return board
        x -= 1
        y += 1
    return board
        
def flip_r_diag_up(pos, board, player, size):
    x, y = pos
    opo = ''
    toFlip = []
    if player == 'W':
        opo = 'B'
    else:
        opo = 'W'
    x += 1
    y -= 1
    while x < size and y > 0:
        if board[y][x] == ' ':
            return board
        elif board[y][x] == opo:
            toFlip.append((x,y))
        elif board[y][x] == player:
            for i in toFlip:
                x, y = i
                board[y][x] = player
            return board
        x += 1
        y -= 1
    return board
        
def flip_l_diag_up(pos, board, player, size):
    x, y = pos
    opo = ''
    toFlip = []
    if player == 'W':
        opo = 'B'
    else:
        opo = 'W'
    x -= 1
    y -= 1
    while x > 0 and y > 0:
        if board[y][x] == ' ':
            return board
        elif board[y][x] == opo:
            toFlip.append((x,y))
        elif board[y][x] == player:
            for i in toFlip:
                x, y = i
                board[y][x] = player
            return board
        x -= 1
        y -= 1
    return board
def flip_r_diag_down(pos, board, player, size):
    x, y = pos
    opo = ''
    toFlip = []
    if player == 'W':
        opo = 'B'
    else:
        opo = 'W'
    x += 1
    y += 1
    while x < size and y < size:
        if board[y][x] == ' ':
            return board
        elif board[y][x] == opo:
            toFlip.append((x,y))
        elif board[y][x] == player:
            for i in toFlip:
                x, y = i
                board[y][x] = player
            return board
        x += 1
        y += 1
    return board

##################################################
#Makes the Move
##################################################
def apply_action(board_state = None, action = None, turn = None):
    #print(board_state)
    if action == None:
        return board_state
    y, x = action
    size = len(board_state[0])
    action = (x,y)
    board_state[y][x] = turn
    #print_board(board_state)
    #print()
    board_state = flip_left(action, board_state, turn, size)
    #print_board(board_state)
    #print()
    board_state = flip_right(action, board_state, turn, size)
    #print_board(board_state)
    #print()
    board_state = flip_up(action, board_state, turn, size)
    #print_board(board_state)
    #print()
    board_state = flip_down(action, board_state, turn, size)
    #print_board(board_state)
    #print()
    board_state = flip_l_diag_up(action, board_state, turn, size)
    board_state = flip_l_diag_down(action, board_state, turn, size)
    board_state = flip_r_diag_up(action, board_state, turn, size)
    board_state = flip_r_diag_down(action, board_state, turn, size)
    return board_state
#######################################################


def getPlayerPos(board, player, size):
    pos = []
    for r in range(size):
        for col in range(size):
            if board[r][col] == player:
                pos.append((col, r))
    return pos

#Gets Valid Moves
def get_valid_moves(player, board, playerPos, size):
    ret = []
    #For each piece, check all directions for a valid move
    for pos in playerPos:
        flag, col, row = check_left(pos, board, player, size)
        if flag:
            ret.append((row,col))

        flag, col, row = check_right(pos, board, player, size)
        if flag:
            ret.append((row,col))

        flag, col, row = check_up(pos, board, player, size)
        if flag:
            ret.append((row,col))
        
        flag, col, row = check_down(pos, board, player, size)
        if flag:
            ret.append((row,col))

        flag, col, row = check_l_diag_up(pos, board, player, size)
        if flag:
            ret.append((row,col))

        flag, col, row = check_r_diag_up(pos, board, player, size)
        if flag:
            ret.append((row,col))

        flag, col, row = check_l_diag_down(pos, board, player, size)
        if flag: 
            ret.append((row, col))

        flag, col, row = check_r_diag_down(pos, board, player, size)
        if flag:
            ret.append((row, col))
    return ret

##################################################################
#Check Functions
##########################################
def check_left(pos, board, player, size):
    x, y = pos
    opo = ''
    if player == WHITE:
        opo = BLACK
    else:
        opo = WHITE
    if x == 0:
        return (False, x, y)
    if board[y][x - 1] == opo:
        nx = x - 2
        while nx >= 0:
            if board[y][nx] == SPACE:
                return (True, nx, y)
            elif board[y][nx] == player:
                return (False, x, y)
            nx -= 1
        return (False, x,y)
    else: return (False, x,y)

def check_right(pos, board, player, size):
    x, y = pos
    opo = ''
    if player == WHITE:
        opo = BLACK
    else:
        opo = WHITE
    if x == size - 1:
        return (False, x,y)
    if board[y][x + 1] == opo:
        nx = x + 2
        while nx < size:
            if board[y][nx] == SPACE:
                return (True, nx, y)
            elif board[y][nx] == player:
                return (False, x, y)
            nx += 1
        return (False, x,y)
    else: return (False, x,y)

def check_up(pos, board, player, size):
    x, y = pos
    opo = ''
    if player == WHITE:
        opo = BLACK
    else:
        opo = WHITE
    if y == 0:
        return (False, x, y)
    if board[y - 1][x] == opo:
        ny = y - 2
        while ny > -1:
            if board[ny][x] == SPACE:
                return (True, x, ny)
            elif board[ny][x] == player:
                return (False, x, y)
            ny -= 1
        return (False, x,y)
    else: return (False, x,y)

def check_down(pos, board, player, size):
    x, y = pos
    opo = ''
    if player == WHITE:
        opo = BLACK
    else:
        opo = WHITE
    if y == size - 1:
        return (False, x, y)
    if board[y + 1][x] == opo:
        ny = y + 2
        while ny < size:
            if board[ny][x] == SPACE:
                return (True, x, ny)
            elif board[ny][x] == player:
                return (False, x, y)
            ny += 1
        return (False, x,y)
    else: return (False, x,y)

def check_l_diag_down(pos, board, player, size):
    x, y = pos
    opo = ''
    if player == WHITE:
        opo = BLACK
    else:
        opo = WHITE
    if y == size - 1 or x == 0:
        return (False, x, y)
    if board[y + 1][x - 1] == opo:
        ny = y + 2
        nx = x - 2
        while ny < size and nx >= 0:
            if board[ny][nx] == SPACE:
                return (True, nx, ny)
            elif board[ny][nx] == player:
                return (False, x, y)
            ny += 1
            nx -= 1
        return (False, x,y)
    else: return (False, x,y)

def check_r_diag_up(pos, board, player, size):
    x, y = pos
    opo = ''
    if player == WHITE:
        opo = BLACK
    else:
        opo = WHITE
    if y == size - 1 or x == size - 1:
        return (False, x, y)
    if board[y - 1][x + 1] == opo:
        ny = y - 2
        nx = x + 2
        while ny > 0 and nx < size:
            if board[ny][nx] == SPACE:
                return (True, nx, ny)
            elif board[ny][nx] == player:
                return (False, x, y)
            ny -= 1
            nx += 1
        return (False, x,y)
    else: return (False, x,y) 

def check_l_diag_up(pos, board, player, size):
    x, y = pos
    opo = ''
    if player == WHITE:
        opo = BLACK
    else:
        opo = WHITE
    if y == 0 or x == 0:
        return (False, x, y)
    if board[y - 1][x - 1] == opo:
        ny = y - 2
        nx = x - 2
        while ny >= 0 and nx >= 0:
            if board[ny][nx] == SPACE:
                return (True, nx, ny)
            elif board[ny][nx] == player:
                return (False, x, y)
            ny -= 1
            nx -= 1
        return (False, x,y)
    else: return (False, x,y)

def check_r_diag_down(pos, board, player, size):
    x, y = pos
    opo = ''
    if player == WHITE:
        opo = BLACK
    else:
        opo = WHITE
    if y == size - 1 or x == size - 1:
        return (False, x, y)
    if board[y + 1][x + 1] == opo:
        ny = y + 2
        nx = x + 2
        while ny < size and nx < size:
            if board[ny][nx] == SPACE:
                return (True, nx, ny)
            elif board[ny][nx] == player:
                return (False, x, y)
            ny += 1
            nx += 1
        return (False, x,y)
    else: return (False, x,y)

BLACK = 'B'
WHITE = 'W'
SPACE = ' '
def get_weight_sum(board_state, board_weight,board_size, turn):
    score = 0
    for row in range(board_size):
        for col in range(board_size):
            if col == board_state[row][col]:
                score += board_weight[row][col]
    return score
def opponent(turn):
    if turn == 'B':
        return 'W'
    else:
        'B'
def value(board, turn, depth):
    return minimax(opponent(turn), board, depth - 1)[0]

def localMax(moves, board_weight):
    #Get Next Turn
    runningMax = -9999999
    runningMove = None
    for move in moves:
        check =  board_weight[move[0]][move[1]]
        if check > runningMax:
            runningMax = check
            runningMove = move
    return runningMove


############################
#
#Binary Heap
#
############################
class Binary_Heap_Queue:
    def __init__(self):
        self.queue = [] 
        self.__root__ = None
    
    def __str__(self):
        return str(self.queue)
    def __len__(self):
        return len(self.queue)

    def len(self):
        return self.queue.__len__()

    def root(self):
        return self.queue[0][0]

    def left(self, i):
        num = 2 * i + 1
        if num >=  self.queue.__len__():
            return None
        else:
            return self.queue[num][1]

    def right(self, i):
        num = 2 * i + 2
        if num >=  self.queue.__len__():
            return None
        else:
            return self.queue[num][1]

    def parent(self, i):
        num = (i - 1) // 2
        if num < 0:
            return None
        else:
            return self.queue[num][1]

    def reheapify(self, i):
        if i == 0:
            return
        if self.queue[i][1] > self.parent(i):
            x = self.queue[i]
            self.queue[i] = self.queue[(i - 1) // 2]
            self.queue[(i - 1) // 2] = x
            self.reheapify((i - 1) // 2)
        else: return

    def pop_reheapify(self, i):
        if i >= len(self.queue) - 1:
            return

        local_left = self.left(i)
        local_right = self.right(i)
        if local_left is not None and local_right is not None:
            if local_left > local_right:
                branch_max = (2 * i) + 1
            else:
                branch_max = (2 * i) + 2

            if self.queue[i][1] < self.queue[branch_max][1]:
                x = self.queue[i]
                self.queue[i] = self.queue[branch_max]
                self.queue[branch_max] = x
                self.pop_reheapify(branch_max)
        elif local_left is not None:
            if self.queue[i][1] < self.queue[(2 * i) + 1][1]:
                x = self.queue[i]
                self.queue[i] = self.queue[(2 * i) + 1]
                self.queue[(2 * i) + 1] = x
                self.pop_reheapify((2 * i) + 1)
            
    def pop(self):
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        ret = self.queue.pop()
        self.pop_reheapify(0)
        return ret
        

    def insert(self, obj, pri_key):
        self.queue.append((obj, pri_key))
        self.reheapify(self.queue.__len__() - 1)
##################################################################
def minimax(turn, board_state, board_weight, board_size, depth, move, a , b, player):
    #Base Case
    if depth == 0:
        return (None,  get_weight_sum(board_state, board_weight, board_size, turn))
    else:
        bestAction = None
        #Max
        if player == 1:
            maximum = -9999999
            queue = Binary_Heap_Queue()
            playerPos = getPlayerPos(board_state, turn, board_size)
            moves = get_valid_moves(turn, board_state, playerPos, board_size)
            for move in moves:
                state = copy.deepcopy(board_state)
                state = apply_action(state, move, turn)
                queue.insert(move, get_weight_sum(state, board_weight, board_size, turn))
            for action in range(len(queue)):
                act = queue.pop()
                score = act[1]
                state = apply_action(copy.deepcopy(board_state), act[0], turn)

                v = minimax(opponent(turn), state, board_weight, board_size, depth - 1, act, a, b, 0)
                if v[0] == None:
                    maximum = score
                    bestAction = act[0]
                elif v[1] > maximum:
                    maximum = v[1]
                    bestAction = act[0]
                a = max(a, maximum)
                if a >= b:
                    break
            return(bestAction, int(maximum))
        #Max
        if player == 0:
            minimum = 9999999
            queue = Binary_Heap_Queue()
            playerPos = getPlayerPos(board_state, turn, board_size)
            moves = get_valid_moves(turn, board_state, playerPos, board_size)
            for move in moves:
                state = copy.deepcopy(board_state)
                state = apply_action(state, move, turn)
                queue.insert(move, get_weight_sum(state, board_weight, board_size, turn))
            for action in range(len(queue)):
                act = queue.pop()
                score = act[1]
                state = apply_action(copy.deepcopy(board_state), act[0], turn)

                v = minimax(opponent(turn), state, board_weight, board_size, depth - 1, act, a, b, 1)
                if v[0] == None:
                    minimum = score
                    bestAction = act[0]
                elif v[1] < minimum:
                    maximum = v[1]
                    bestAction = act[0]
                b = min(b, minimum)
                if b <= a:
                    break
            return(bestAction, int(minimum))
        
                    
#Get the move for bot
def get_move(board_size, board_state, turn, time_left, opponent_time_left):
    board_weight = []
    #Develop weighted board
    for r in range(board_size):
        col = []
        for c in range(board_size):
            col.append(1)
        board_weight.append(col)
    #Left Top corner
    board_weight[0][0] = 520
    board_weight[0][1] = -250
    board_weight[1][1] = -250
    board_weight[1][0] = -250
    board_weight[0][2] = 50
    board_weight[2][2] = 50
    board_weight[2][0] = 50
    
    board_weight[0][board_size - 1] = 520
    board_weight[0][board_size - 2] = -250
    board_weight[1][board_size - 2] = -250
    board_weight[1][board_size - 1] = -250
    board_weight[0][board_size - 3] = 50
    board_weight[2][board_size - 3] = 50
    board_weight[2][board_size - 1] = 50
    
    board_weight[board_size - 1][0] = 520
    board_weight[board_size - 1][1] = -250
    board_weight[board_size - 2][1] = -250
    board_weight[board_size - 2][0] = -250
    board_weight[board_size - 1][2] = 50
    board_weight[board_size - 3][2] = 50
    board_weight[board_size - 3][0] = 50
    
    board_weight[board_size - 1][board_size - 1] = 520
    board_weight[board_size - 1][board_size - 2] = -250
    board_weight[board_size - 2][board_size - 2] = -250
    board_weight[board_size - 2][board_size - 1] = -250
    board_weight[board_size - 1][board_size - 3] = 50
    board_weight[board_size - 3][board_size - 3] = 50
    board_weight[board_size - 3][board_size - 1] = 50
        
    #for i in board_weight:
    #    print(i)
    
    playerPos = getPlayerPos(board_state, turn, board_size)
    valid = get_valid_moves(turn, board_state, playerPos, board_size)
    if len(valid) == 0:
        return None
    #Checks Corners (Best position)
    if (0, 0) in valid:
        return (0, 0)
    elif (0, board_size - 1) in valid:
        return (0, board_size - 1)
    elif (board_size - 1, 0) in valid:
        return (board_size - 1, 0)
    elif (board_size - 1, board_size - 1) in valid:
        return (board_size - 1, board_size - 1)
    #Minimax Heuristic
    if time_left > 4000:
        return minimax(turn, board_state, board_weight, board_size, 4, None, -999999, 99999999, 1)[0]
    else:
        return minimax(turn, board_state, board_weight, board_size, 2, None, -999999, 99999999, 1)[0]
