import numpy as np
import time


class Game:
    def __init__(self, size=(8,8), seed=None, max_gen=10):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)
        
        # Initialize the board with a random series of 1s and 0s
        self._board = np.random.randint(0,2,size)
        self._gen = 0
        self._max_gen = max_gen

    
    def update(self):
        board = np.copy(self._board)

        #naive implementation
        '''
        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                areaSum = 0
                for n in range(row-1, row+2):
                    if n >= 0 and n < len(board):
                        for m in range(col-1, col+2):
                            if m >= 0 and m < len(board[row]):
                                areaSum += self._board[n, m]
                #print("loc", row, col,"value", board[row, col], "sum", areaSum)
                if board[row, col] == 1 and (areaSum == 4 or areaSum == 3):
                    board[row, col] = 1
                elif board[row, col] == 0 and (areaSum == 3):
                    board[row, col] = 1
                else:
                    board[row, col] = 0
        '''

        #'''
        #improving upon naive implementation
        #note: an object oriented approach to this problem would be able to yield a
        #better result, however that is outside the scope of this challenge.
        weights = np.zeros((2, len(board), len(board[0])), dtype=int)
        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                if self._board[col, row] == 1:
                    weights[1, col, row] = 1
                    for n in range(row - 1, row + 2):
                        if n >= 0 and n < len(board):
                            for m in range(col - 1, col + 2):
                                if m >= 0 and m < len(board[0]):
                                    if n != row or m != col:
                                        weights[0, m, n] += 1


        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                if weights[1, col, row] == 1 and (weights[0, col, row] == 2 or weights[0, col, row] == 3):
                    board[col, row] = 1
                elif weights[1, col, row] == 0 and weights[0, col, row] == 3:
                    board[col, row] = 1
                else:
                    board[col, row] = 0
        '''
        if self._gen == 0 or self._gen == 1 or self._gen == 2:
            print(weights[0, 7, 0])
            print(weights[1, 7, 0])
            print(board[1, 0])
        '''

        self._board = board


    def play(self, delay=.1):
        while self._gen < self._max_gen:
            # Start the generation by drawing the current board
            self.draw()
            
            # Next we update each of the cells according to the rules 
            self.update()

            # Increment the generation and sleep to make the visualization easier
            self._gen += 1
            time.sleep(delay)

    def time_run(self, gens=1000):
        start = time.time()
        for _ in range(gens):
            self.update()
        print(f'Average update time: {(time.time()-start)/gens*1000} ms')

    def draw(self):
        for row in self._board:   
            # Print a full block for each alive cell and an empty one for dead cells bounded by |
            print('|'.join(['▇' if c else ' ' for c in row]))

        print(f'Generation: {self._gen}')


if __name__ == "__main__":
    # If this file is run directly from the command line, run the game
    g = Game()
    g.time_run()
    g.play()  # Uncomment this to see the generational progression