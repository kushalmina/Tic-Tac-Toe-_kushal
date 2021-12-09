board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
AI = "O"
Player = "X"
utility_value = {AI: 1,
                 "Draw": 0,
                 Player: -1}
winningPositions = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                    [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]

def isWin(_board):
    for position in winningPositions:
        if _board[position[0][0]][position[0][1]] != "-" and\
                _board[position[0][0]][position[0][1]] == _board[position[1][0]][position[1][1]] and\
                _board[position[1][0]][position[1][1]] == _board[position[2][0]][position[2][1]]:
            return _board[position[0][0]][position[0][1]]
    return False

def isDraw(_board):
    for i in _board:
        if "-" in i:
            return False
    return True

def tic_tac_toe_game(_board):
    validInput = False
    print("Enter space-separated row and column location for a human player")

    while not validInput:
        i, j = input().split()
        i, j = int(i), int(j)
        if i > 2 or i < 0 or j > 2 or j < 0 or _board[i][j] != "-":
            print("Please Enter Valid Input")
        else:
            validInput = True
            _board[i][j] = Player

    print("After the human player move - Current State of the board")
    show_board_state(_board)

    if state_game(_board, "Player"):
        next_move_AI(_board)

def state_game(_board, activePlayer):
    if isWin(_board):
        print(activePlayer + " has won!!!")
        return False

    if isDraw(_board):
        print("Tie!")
        return False

    return True

def show_board_state(_board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(_board[i][j], end=" ")
        print()
    print()

def next_move_AI(_board):
    bestScore = -float("infinity")

    for i in range(3):
        for j in range(3):
            if _board[i][j] == "-":
                _board[i][j] = AI
                myScore = minimax_algo(_board, False)
                _board[i][j] = "-"
                if myScore > bestScore:
                    bestScore = myScore
                    nextMove = (i, j)
            if bestScore == utility_value[AI]:
                break
        if bestScore == utility_value[AI]:
            break

    i, j = nextMove
    _board[i][j] = AI
    print("AI Plays " + str(nextMove))
    print("After the AI agent  move - Current State of the board")
    show_board_state(_board)

    if state_game(_board, "AI"):
        tic_tac_toe_game(_board)

def minimax_algo(_board, agent_turn):
    if isWin(_board) == AI:
        return utility_value[AI]
    if isWin(_board) == Player:
        return utility_value[Player]
    if isDraw(_board):
        return utility_value["Draw"]

    if agent_turn:
        maxScore = -float("infinity")
        for i in range(3):
            for j in range(3):
                if _board[i][j] == "-":
                    _board[i][j] = AI
                    childScore = minimax_algo(_board, False)
                    _board[i][j] = "-"
                    maxScore = max(childScore, maxScore)
                if maxScore == utility_value[AI]:
                    break
            if maxScore == utility_value[AI]:
                break
        return maxScore

    else:
        minScore = float("infinity")
        for i in range(3):
            for j in range(3):
                if _board[i][j] == "-":
                    _board[i][j] = Player
                    childScore = minimax_algo(_board, True)
                    _board[i][j] = "-"
                    minScore = min(childScore, minScore)
                if minScore == utility_value[Player]:
                    break
            if minScore == utility_value[Player]:
                break
        return minScore


show_board_state(board)
tic_tac_toe_game(board)