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
            row, col = self.get_player_input()
            self.take_turn(row, col)
            
        self.render_board()
        if self.winner == -1:
            print("It's a draw!")
        else:
            print("Player", 'X' if self.winner == 0 else 'O', "wins!")


    def get_player_input(self):
        while True:
            try:
                move = input("Enter your move (row col): ").split()
                if len(move) != 2:
                    print("Invalid format.")
                    continue
                row, col = map(int, move)
                if row not in range(3) or col not in range(3):
                    print("Invalid coordinates.")
                    continue
                return row, col
            except ValueError:
                print("Invalid input.")

  
    def take_turn(self, row, col):
        player_value = -1 if self.current_player == 0 else 1
        if self.board[row, col] != 0:
            print("Cell occupied. Try again.")
            return False
            
        self.board[row, col] = player_value
        self.move += 1
        player_won = self.check_winner()
        if player_won:
            self.winner = self.current_player
            self.game_over = True
            return True
        
        self.current_player = 1 - self.current_player # flip-flop w/o mod 
        return True

      
    def check_winner(self):
        target_score = self.board.shape[0]
        lines = []

        lines.extend(np.sum(self.board, axis=0))
        lines.extend(np.sum(self.board, axis=1))
        lines.append(np.trace(self.board))
        lines.append(np.trace(np.fliplr(self.board)))

        if target_score in lines or -target_score in lines:
            return True

        return False


    def reset(self):
        self.board.fill(0)
        self.current_player = 0  # X's go first
        self.winner = -1
        self.game_over = False
        self.move = 0

 
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
 

