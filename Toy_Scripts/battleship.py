import random

#Game setup
board = []
x = int(input("What size do you want the board to be: "))
#x = int(x)
for item in range(x):
    board.append(["O"] * x)

#Gives ship a random location and saves it to memory
def row_location(x):
    return random.randint(0,x-1)
def col_location(x):
    return random.randint(0,x-1)
ship_row = row_location(x)
ship_col = col_location(x)


#prints ship location for debugging... debugging honest.
#print (ship_row +1)
#print (ship_col +1)



#prints board so user can see scale and once guesses have been made targets aimed for in the past
def print_board(board):
    for row in board:
        print ("|".join(row))

print ("x is " + str(x))
print (print_board(board))


turn = 0
while turn < 3:
    row_guess = int(input("What row do you want to aim for: "))
    col_guess = int(input("What Column do you want to aim for: "))
    row_shot = row_guess - 1
    col_shot = col_guess - 1

    if row_shot == ship_row and col_shot == ship_col:
        print ("Congratulations! You sank my battleship!")
        board[row_shot][col_shot] = "X"
        break
    elif row_guess not in range(1,x + 1) or col_guess not in range(1,x + 1):
        print ("You need to aim for the board")
    elif board[row_shot][col_shot] == "X":
        print ("You aimed here already")
    else:
        board[row_shot][col_shot] = "X"
        print("You missed")
    turn += 1
    print(print_board(board))
