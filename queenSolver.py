from queenchessboard import QueenChessBoard

class Solver_Queen:
    def __init__(self, size):
        self.size=size
        self.number_of_solutions=0
        self.row=0
        self.column=0


    def solve_queen(self):
        """Display a chessboard for each possible configuration of placing n queens
        on an n x n chessboard and print the number of such configurations."""
        #chessBoard=QueenChessBoard(size)
        board = QueenChessBoard(self.size)
        # number_of_solutions = 0
    
        # row = 0
        # column = 0
        # iterate over rows of board
        while True:
            # place queen in next row
            while self.column < self.size:
                if board.is_this_column_safe_in_next_row(self.column):
                    board.place_in_next_row(self.column)
                    self.row += 1
                    self.column = 0
                    break
                else:
                    self.column += 1
    
            # if could not find column to place in or if board is full
            if (self.column == self.size or self.row == self.size):
                # if board is full, we have a solution
                if self.row == self.size:
                    board.display()
                    print()
                    self.number_of_solutions += 1
    
                    # small optimization:
                    # In a board that already has queens placed in all rows except
                    # the last, we know there can only be at most one position in
                    # the last row where a queen can be placed. In this case, there
                    # is a valid position in the last row. Thus we can backtrack two
                    # times to reach the second last row.
                    board.remove_in_current_row()
                    self.row -= 1
    
                # now backtrack
                try:
                    prev_column = board.remove_in_current_row()
                except IndexError:
                    # all queens removed
                    # thus no more possible configurations
                    break
                # try previous row again
                self.row -= 1
                # start checking at column = (1 + value of column in previous row)
                self.column = 1 + prev_column
    
        print('Number of solutions:', self.number_of_solutions)

