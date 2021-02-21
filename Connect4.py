# # Connect4.py
#
# # A simple game of Connect 4 with a text interface
#
# print("Let's play Connect 4")
#
#
# def make_board(rows, cols):
#     return [(['-']) * cols for row in range(rows)]
#
#
# def print_board(board):
#     rows = len(board)
#     cols = len(board[0])
#     print()
#
#     # first print the column headers
#     print(' ', end='')
#     for col in range(cols):
#         print(str(col + 1).center(3), ' ', end='')
#     print()
#
#     # now print the board
#     for row in range(rows):
#         print(' ', end='')
#         for col in range(cols):
#             print(board[row][col].center(3), ' ', end='')
#         print()
#
#
# def get_move_col(board, player):
#     cols = len(board[0])
#
#     while True:
#         response = input(f"Enter  player {player}'s move (column number) --> ")
#         # noinspection PyBroadException
#         try:
#             move_col = int(response) - 1  # -1 since user see cols starting at 1
#             if (move_col < 0) or (move_col >= cols):
#                 print(f"Columns must be between 1 and {cols}.", end='')
#             elif (board[0][move_col] != '-'):
#                 print("That column is full!")
#             else:
#                 return move_col
#
#         except:
#             print("Columns must be integer values!", end='')  # if they didn't even enter an integer
#         print("Please try again")
#
#
# def get_move_row(board, move_col):
#     rows = len(board)  # find first open row from bottom
#     for move_row in range(rows - 1, -1, -1):
#         if board[move_row][move_col] == '-':
#             return move_row
#         # should never get here
#         assert False
#
#
# def check_for_win(board, player):
#     winning_word = player * 4
#     return word_search(board, winning_word) is not None
#
#
# def word_search(board, word):
#     (rows, cols) = (len(board), len(board[0]))
#     for row in range(rows):
#         for col in range(cols):
#             result = wordSearchFromCell(board, word, row, col)
#             if result is not None:
#                 return result
#     return None
#
#
# def wordSearchFromCell(board, word, startRow, startCol):
#     for drow in [-1, 0, +1]:
#         for dcol in [-1, 0, +1]:
#             if (drow, dcol) != (0, 0):
#                 result = wordSearchFromCellInDirection(board, word,
#                                                        startRow, startCol,
#                                                        drow, dcol)
#                 if (result != None):
#                     return result
#     return None
#
#
# def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):
#     (rows, cols) = (len(board), len(board[0]))
#     dirNames = [['up-left', 'up', 'up-right'],
#                 ['left', '', 'right'],
#                 ['down-left', 'down', 'down-right']]
#     for i in range(len(word)):
#         row = startRow + i * drow
#         col = startCol + i * dcol
#         if ((row < 0) or (row >= rows) or
#                 (col < 0) or (col >= cols) or
#                 (board[row][col] != word[i])):
#             return None
#     return (word, (startRow, startCol), dirNames[drow + 1][dcol + 1])
#
#
# def play_connect4():
#     rows = 6
#     cols = 5
#
#     board = make_board(rows, cols)
#     player = 'X'
#     move_count = 0
#     print_board(board)
#
#     while move_count < (rows * cols):
#         move_col = get_move_col(board, player)
#         move_row = get_move_row(board, move_col)
#         board[move_row][move_col] = player
#         print_board(board)
#         if check_for_win(board, player):
#             print(f"*** Player {player} Wins!! ***")
#             return
#         move_count += 1
#         player = 'O' if player == 'X' else 'X'
#     print("*** TIE GAME ***")
#
#
#
# play_connect4()

# connect4.py

# A simple game of connect4 with a text interface
# based on the wordSearch code written in class.

def playConnect4():
    rows = 6
    cols = 7
    board = makeBoard(rows, cols)
    player = 'X'
    moveCount = 0
    printBoard(board)
    while (moveCount < rows*cols):
        moveCol = getMoveCol(board, player)
        moveRow = getMoveRow(board, moveCol)
        board[moveRow][moveCol] = player
        printBoard(board)
        if checkForWin(board, player):
            print(f'*** Player {player} Wins!!! ***')
            return
        moveCount += 1
        player = 'O' if (player == 'X') else 'X'
    print('*** Tie Game!!! ***')

def makeBoard(rows, cols):
    return [ (['-'] * cols) for row in range(rows) ]

def printBoard(board):
    rows = len(board)
    cols = len(board[0])
    print()
    # first print the column headers
    print('    ', end='')
    for col in range(cols):
        print(str(col+1).center(3), ' ', end='')
    print()
    # now print the board
    for row in range(rows):
        print('    ', end='')
        for col in range(cols):
            print(board[row][col].center(3), ' ', end='')
        print()

def getMoveCol(board, player):
    cols = len(board[0])
    while True:
        response = input(f"Enter player {player}'s move (column number) --> ")
        try:
            moveCol = int(response)-1  # -1 since user sees cols starting at 1
            if ((moveCol < 0) or (moveCol >= cols)):
                print(f'Columns must be between 1 and {cols}.', end='')
            elif (board[0][moveCol] != '-'):
                print('That column is full! ', end='')
            else:
                return moveCol
        except:
            # they did not even enter an integer!
            print('Columns must be integer values! ', end='')
        print('Please try again.')

def getMoveRow(board, moveCol):
    # find first open row from bottom
    rows = len(board)
    for moveRow in range(rows-1, -1, -1):
        if (board[moveRow][moveCol] == '-'):
            return moveRow
    # should never get here!
    assert(False)

def checkForWin(board, player):
    winningWord = player * 4
    return (wordSearch(board, winningWord) != None) # that was easy!

##############################################
# taken from wordSearch.py
##############################################

def wordSearch(board, word):
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != None):
                return result
    return None

def wordSearchFromCell(board, word, startRow, startCol):
    for drow in [-1, 0, +1]:
        for dcol in [-1, 0, +1]:
            if (drow, dcol) != (0, 0):
                result = wordSearchFromCellInDirection(board, word,
                                                       startRow, startCol,
                                                       drow, dcol)
                if (result != None):
                    return result
    return None

def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):
    (rows, cols) = (len(board), len(board[0]))
    dirNames = [ ['up-left'  ,   'up', 'up-right'],
                 ['left'     ,   ''  , 'right'   ],
                 ['down-left', 'down', 'down-right' ] ]
    for i in range(len(word)):
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols) or
            (board[row][col] != word[i])):
            return None
    return (word, (startRow, startCol), dirNames[drow+1][dcol+1])

playConnect4()
