# array in python is called a LIST

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
user = True  # this is x if false then o
turns = 0


def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


def quit(user_input):
    if user_input == 'q':
        print("Thanks for playin")
        return True
    else:
        return False


def check_input(user_input):
    # check if number
    if not is_num(user_input):
        return False
    user_input = int(user_input)
    # check if 1-9
    if not bounds(user_input):
        return False
    return True


def is_num(user_input):
    # since input is always a string we have to change to num
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else:
        return True


def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("number out of bounds ")
        return False
    else:
        return True


def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This place is taken")
        return True
    else:
        return False


def coordinates(user_input):
    row = int(user_input/3)
    col = user_input
    if col > 2:
        col = int(col % 3)
    return (row, col)


def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user


def current_user(user):
    if user:
        return "x"
    else:
        return "o"


def iswin(user, board):
    if check_row(user, board):
        return True
    if check_col(user, board):
        return True
    if check_diag(user, board):
        return True
    return False


def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
    return False


def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False


def check_diag(user, board):
    # only two ways in a square
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False


while turns < 9:
    active_user = current_user(user)
    print_board(board)
    user_input = input("please enter a postion 1 to 9 or \"q\" to quit: ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("please try again")
        continue
    user_input = int(user_input)-1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("try again")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        print_board(board)
        break
    turns += 1
    if turns == 9:
        print("Tie!")
    user = not user
