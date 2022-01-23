ticTacToe = ["_","_","_","_","_","_","_","_","_"]
boardPosition = [1,2,3,4,5,6,7,8,9]
print("These are the numbers of the board where your character will be stored:",end = "\n")
print(boardPosition[0], boardPosition[1], boardPosition[2])
print(boardPosition[3], boardPosition[4], boardPosition[5])
print(boardPosition[6], boardPosition[7], boardPosition[8])

temp = 1

def tictacToeBoard():
    print(ticTacToe[0], ticTacToe[1], ticTacToe[2])
    print(ticTacToe[3], ticTacToe[4], ticTacToe[5])
    print(ticTacToe[6], ticTacToe[7], ticTacToe[8])    

tictacToeBoard()

def playerOne():
    player1 = int(input("Enter the position to insert 'O':"))
    if ticTacToe[player1-1] == "_":
        ticTacToe[player1-1] = "O"
        tictacToeBoard()
    else:
        print("position  is already filled, try another one")
        playerOne()
        

def playerTwo():
   
    player2 = int(input("Enter position to insert 'X': "))
    if ticTacToe[player2-1] == "_":
        ticTacToe[player2-1] = "X"
        tictacToeBoard()
    else:
        print("position  is already filled, try another one")
        playerTwo()


def winOne():

   
    if ticTacToe[0] and ticTacToe[1] and ticTacToe[2] == "O":
        print("Player One wins!")
    elif ticTacToe[0] and ticTacToe[3] and ticTacToe[6] == "O":
        print("Player One wins!")
    elif ticTacToe[6] and ticTacToe[7] and ticTacToe[8] == "O":
        print("Player One wins!")
    elif ticTacToe[2] and ticTacToe[5] and ticTacToe[8] == "O":
        print("Player One wins!")

def winTwo():
   
    if ticTacToe[0] and ticTacToe[1] and ticTacToe[2] == "X":
        print("Player Two Wins!")
        temp = 0
    elif ticTacToe[0] and ticTacToe[3] and ticTacToe[6] == "X":
        print("Player Two Wins!")
        temp = 0
    elif ticTacToe[6] and ticTacToe[7] and ticTacToe[8] == "X":
        print("Player Two Wins!")
        temp = 0
    elif ticTacToe[2] and ticTacToe[5] and ticTacToe[8] == "O":
        print("Player Two Wins!")
        temp = 0


for i in range(9):
    playerOne()
    winOne()
    playerTwo()
    winTwo()
       