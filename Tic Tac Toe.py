board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print("   |   |")
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print("   |   |")
    print("-"*11)
    print("   |   |")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("   |   |")
    print("-"*11)
    print("   |   |")
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print("   |   |")


def isWinner(bo, le):
    rows = (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5]
                                                             == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le)
    columns = (bo[1] == le and bo[4] == le and bo[7] == le) or (
        bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le)
    diagonals = (bo[1] == le and bo[5] == le and bo[9] == le) or (
        bo[3] == le and bo[5] == le and bo[7] == le)
    return rows or columns or diagonals


def playerMove():
    while True:
        move = input("Please select a position to place an X (1-9): ")
        try:
            move = int(move)
            if 0 < move < 10:
                if spaceIsFree(move):
                    insertLetter("X", move)
                    break
                print("This space is occupied, select a free position")
            else:
                print("input number is out of range")
        except:
            print("Please give a number!")


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " "]
    move = 0

    for let in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    return not(board.count(" ") > 1)


def main():
    print("Welcome to HU Tic Tac Toe :)")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, "O")):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O's win this time!")
            break

        if not(isWinner(board, "X")):
            move = compMove()
            if move == 0:
                print("Tie Game!")
            else:
                insertLetter("O", move)
                print(f"Computer placed an O on position {move}")
                printBoard(board)
        else:
            print(
                "That's grape. Next generation Pakistan is going to make Pakistan crazy 100%")
            break

    if isBoardFull(board):
        print("Better Luck Next Time")


main()
