import random

#print dashboard
def display_board(board):
    j = 8
    m = 9
    for i in range(1,4):
        number = [ 1,2,3,4,5,6,7,8,9]
        print('+---------------------------+')
        print('|'+str(number[j-2])+'        |'+str(number[j-1])+'       |'+str(number[j])+'       |')
	print('|    '+str(board[m-2])+'    '+'|    '+str(board[m-1])+'   '+'|   '+str(board[m])+'    |' )
	print('|         |        |        |')
        j -=3
        m -=3
    print('+---------------------------+\n')

def place_marker(board, marker, position):
      board[position] = str(marker)

def win(board,mark):
    check = False
    #horizontal
    test1 = board[1]+board[2]+board[3]
    test2 = board[4]+board[5]+board[6]
    test3 = board[7]+board[8]+board[9]
    if test1 == mark+mark+mark:
        check = True
    elif test2 == mark+mark+mark:
        check = True
    elif test3 == mark+mark+mark:
        check = True
    #vertical
    test4 = board[1]+board[4]+board[7]
    test5 = board[2]+board[5]+board[8]
    test6 = board[3]+board[6]+board[9]
    if test4 == mark+mark+mark:
        check = True
    elif test5 == mark+mark+mark:
        check = True
    elif test6 == mark+mark+mark:
        check = True
    #diagonal
    test7 = board[1]+board[5]+board[9]
    test8 = board[7]+board[5]+board[3]
    if test7 == mark+mark+mark:
        check = True
    elif test8 == mark+mark+mark:
        check = True

    return check

#check boar
def board_check(board):
    check = True
    for i in range(1,10):
        if board[i] is ' ':
            check = False
            break
    return check


#player choise
def player_choice(board, turn):

    while True:
        choice = raw_input("choose a position from 1 to 9")
        if choice.isalpha() is True:
                print("You made a mistake \n")
        elif choice.isdigit() is True:
            c = int(choice)
            if c in range(1,10) and board[c] == ' ':
                break
            else:
                print("You made a mistake\n")

        else:
            continue
    return c

#players name
name = raw_input("Whats your name\n")
decision = True
while decision:
    #start first
    print ("Who is gonna start first?")
    x = random.randint(0,1)
    if x is 0:
        print (name + " play first")
        turn = name
        marker = {name: 'X', 'computer': 'O', }
    elif x is 1:
        print("Computer play first")
        turn = "computer"
        marker = {name: 'O', 'computer': 'X', }
    decision = True
    theBoard = [' '] * 10
    game_on = True
    while game_on:
        if turn == name:
            display_board(theBoard)
            position = player_choice(theBoard, turn)
            place_marker(theBoard, marker[turn], position)
            if win(theBoard, marker[turn]):
                display_board(theBoard)
                print(turn + " You Win")
                game_on = False
            elif board_check(theBoard):
                 display_board(theBoard)
                 print('Isopalia!')
                 game_on = False
            else:
                turn = "computer"
        elif turn == "computer":
            epilogh = True
            while epilogh:
                x = random.randint(1,9)
                if theBoard[x] == ' ':
                    epilogh = False
            position = x
            place_marker(theBoard, marker[turn], position)
            if win(theBoard, marker[turn]):
                display_board(theBoard)
                print(name + " you lose!!")
                game_on = False
            elif board_check(theBoard):
                 display_board(theBoard)
                 print('Its a draw!')
                 game_on = False
            else:
                turn = name

        if game_on == False:
            stop = True
            while stop:
                y = raw_input("Wanna play again?(yes/no)\n")
                if y == "yes":
                    stop = False
                    decision = True
                elif y == "no":
                    decision = False
                    stop = False
