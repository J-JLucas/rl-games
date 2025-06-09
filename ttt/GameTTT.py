import numpy as np

class GameTTT:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 0 
        self.winner = -1
        self.game_over = False
        self.move = 0

    def play(self):
        self.reset()
        while not self.game_over and self.move < 9:
            self.render_board()
            self.take_turn()
            self.check_winner()
            self.current_player = (self.current_player + 1) % 2
            
        self.render_board()
        if self.winner == -1:
            print("It's a draw!")
        else:
            print("Player", 'X' if self.winner == 0 else 'O', "wins!")
   
    def take_turn(self):
        valid = False
        if self.current_player == 0:
            print("Player X's turn")
            player_value = -1
        else:
            print("Player O's turn")
            player_value = 1
        print("Enter your move (row col) eg: (2 1) ")

        while(not valid):
            move = input().split()
            if (len(move) != 2 or move[0] not in '012' or move[1] not in '012'):
                print("invalid input")
                continue
            elif (self.board[int(move[0]), int(move[1])] != 0):
                print("cell occupied")
                continue
            else:
                self.board[int(move[0]), int(move[1])] = player_value
                valid = True
                self.move += 1

    def reset(self):
        self.board.fill(0)
        self.current_player = 0  # X's go first
        self.winner = -1
        self.game_over= False
        self.move = 0
       
    def check_winner(self):
        target_score = self.board.shape[0]
        lines = []

        lines.extend(np.sum(self.board, axis=0))
        lines.extend(np.sum(self.board, axis=1))
        lines.append(np.trace(self.board))
        lines.append(np.trace(np.fliplr(self.board)))

        # x's negative, o's positive
        if -target_score in lines:
            self.winner = 0
            self.game_over = True
        elif target_score in lines:
            self.winner = 1
            self.game_over = True

    def render_board(self):
        symbols = {-1: 'x', 0: ' ', 1: 'o'}
        print("\n    0   1   2")
        print("  ┌───┬───┬───┐")
        for row in range(3):
            print(f"{row} │ " + " │ ".join(
                symbols[self.board[row, col]] for col in range(3)
            ) + " │")
            if row < 2:
                print("  ├───┼───┼───┤")
        print("  └───┴───┴───┘\n")
 

