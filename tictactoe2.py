print("\nWelcome to a game of Tic-Tac-Toe!\n\nSelect your move by entering the number that corresponds with the square you want to play.  You're X and I'm O.")
print("""
0 | 1 | 2
_________
3 | 4 | 5
_________
6 | 7 | 8
""")

#Create list to track which squares are occupied.
occupied_squares = []

#refresh the board with this list
xo_display = [0,1,2,3,4,5,6,7,8]
#print xo_display

#Create lists to store each player's moves
human_moves = []
computer_moves = []

#Establish winning combinations
winning_moves = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

#This is the overall game loop
while len(occupied_squares) < 9:
    #Human's move
    while True:
        move = input("What's your move? ")
        try: 
            move = int(move)
            #break
        except: 
            print("That's not a square.  Try again.")
        
    #while True:
        if move not in occupied_squares:
            occupied_squares.append(move)
            #print occupied_squares
            xo_display[move] = "X"
            #print xo_display
            human_moves.append(move)
            break
        else:
            print("That's not a valid choice. Try again.")
            
    #Print Board with human's move
    print ("\nOK, Here's the board with your move:\n")        
    print xo_display[0], "|", xo_display[1], "|", xo_display[2]
    print("_________")
    print xo_display[3], "|", xo_display[4], "|", xo_display[5]
    print("_________")
    print xo_display[6], "|", xo_display[7], "|", xo_display[8]
        
    #Evaluate human move
    #Reorder human moves to be in ascending order to make comparison against "winning" moves easier.
    human_moves.sort
    #Compare human moves to each list within the winning move "master list."
    x = 0
    while x < 8:
        if winning_moves[x][0] in human_moves and winning_moves[x][1] in human_moves and winning_moves[x][2] in human_moves:
            print("Game over.  You win!")
            winner = "human"
            break
        else:
            x = x + 1
            winner = "no_one"
    #Break out of overall game while loop if the winner is "human."  This ends the game.
    if winner == "human":
        break
         
    #Computer move to win game.  Check to see if computer is one move away from winning, and have computer pick that square if so.
    print("\nIt's the Computer's turn. Here's my move: \n")
    comp_win_move = None
    j = 0
    while j < 8:
        if (winning_moves[j][0] in computer_moves) and (winning_moves[j][1] in computer_moves):
            comp_win_move = winning_moves[j][2]
            break
        elif (winning_moves[j][0] in computer_moves) and (winning_moves[j][2] in computer_moves):
            comp_win_move = winning_moves[j][1]
            break
        elif (winning_moves[j][1] in computer_moves) and (winning_moves[j][2] in computer_moves):
            comp_win_move = winning_moves[j][0]
            break
        else:
            j = j + 1
    #If the program determines there is a winning move and the square hasn't already been occupied, make that move.
    if (comp_win_move != None) and (comp_win_move not in occupied_squares):
        occupied_squares.append(comp_win_move)
        xo_display[comp_win_move] = "O"
        computer_moves.append(comp_win_move)
    else:
        comp_win_move = None

    #Computer Move to block a human win.  Check to see if the human is one one move away from winning by comparing the human moves list against the winning lists.
    comp_block_move = None
    p = 0
    while p < 8:    
        if (winning_moves[p][0] in human_moves) and (winning_moves[p][1] in human_moves):
            comp_block_move = winning_moves[p][2]
            break
        elif (winning_moves[p][0] in human_moves) and (winning_moves[p][2] in human_moves):
            comp_block_move = winning_moves[p][1]
            break
        elif (winning_moves[p][1] in human_moves) and (winning_moves[p][2] in human_moves):
            comp_block_move = winning_moves[p][0]
            break
        else:
            p = p + 1
    
    #Have the computer make the blocking move if it hasn't already made a winning move (and the square is open).        
    if (comp_block_move != None) and (comp_win_move == None) and (comp_block_move not in occupied_squares):
        occupied_squares.append(comp_block_move)
        xo_display[comp_block_move] = "O"
        computer_moves.append(comp_block_move)
    else:
        comp_block_move = None
    
    #Computer's Fallback Move (the first four are the "best moves"--center and corners), if computer doesn't make either 1) a winning move or 2) a blocking move.
    best_move = [4, 2, 0, 6, 8, 1, 3, 5, 7]
    y = 0
    while (y < 9) and (comp_win_move == None) and (comp_block_move == None):
        if best_move[y] not in occupied_squares:
            occupied_squares.append(best_move[y])
            #print(occupied_squares)
            xo_display[best_move[y]] = "O"
            #print(xo_display)
            computer_moves.append(best_move[y])
            #print(computer_moves)
            break
        else:
            y = y + 1
    
    #Print Board with computer's move        
    print xo_display[0], "|", xo_display[1], "|", xo_display[2]
    print("_________")
    print xo_display[3], "|", xo_display[4], "|", xo_display[5]
    print("_________")
    print xo_display[6], "|", xo_display[7], "|", xo_display[8]    
    
    #Evaluate computer move
    #Reorder computer moves to be in ascending order to make a comparison against the winning lists easier.
    computer_moves.sort
    #Compare computer moves to each list within the winning move master list
    x = 0
    while x < 8:
        if winning_moves[x][0] in computer_moves and winning_moves[x][1] in computer_moves and winning_moves[x][2] in computer_moves:
            print("Game over.  I win!  You lose!")
            winner = "computer"
            break
        else:
            x = x + 1
            winner = "no_one"
    #Break out of overall game while loop if the winner is "computer."  This ends the game.
    if winner == "computer":
        break

#Declare a draw if winner is "no_one" (i.e., not human or computer).
if winner == "no_one":
    print ("\nIt's a draw.")

    