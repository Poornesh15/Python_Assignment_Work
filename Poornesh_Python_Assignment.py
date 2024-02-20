class Solution:

    def depth_first_search(self, board, row, col):
        # Function to perform depth-first search starting from given row and column
        
        rows = len(board)  # Number of rows in the board
        cols = len(board[0])  # Number of columns in the board

        # Base cases for termination of the recursion
        # If row or column is out of bounds or cell is already visited or marked 'X', return
        if(row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] == '$' or board[row][col] == 'X'):
            return

        # Mark the current cell as visited
        board[row][col] = '$'

        # Define possible moves: up, down, right, left
        row_moves = [1, -1, 0, 0]
        col_moves = [0, 0, 1, -1]

        # Explore each possible move
        for move in range(4):
            new_row = row + row_moves[move]  # Calculate new row index
            new_col = col + col_moves[move]  # Calculate new column index
            self.depth_first_search(board, new_row, new_col)  # Recursively explore the next cell


    def solve(self, board: List[List[str]]) -> None:
        
        
        rows = len(board)  # Number of rows in the board
        cols = len(board[0])  # Number of columns in the board

        # Traverse the border of the board and perform DFS on 'O' cells
        for col in range(cols):
            self.depth_first_search(board, 0, col)  # Top border
            self.depth_first_search(board, rows - 1, col)  # Bottom border

        for row in range(1, rows - 1):
            self.depth_first_search(board, row, 0)  # Left border
            self.depth_first_search(board, row, cols - 1)  # Right border

        # Convert remaining 'O' cells to 'X' and marked cells ('$') back to 'O'
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = "X"
                elif board[row][col] == "$":
                    board[row][col] = 'O'
