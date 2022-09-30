import numpy as np

class MatrixOps:
    def __init__(self, seed=None):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)

        self._matrix = np.random.randint(0,10, size=(10,10))
        self._kernel = np.random.randint(-2,2, size=(3,3))
    
    def largest_index(self, matrix):
        #sets maxVal bellow minimum value
        maxVal = -10
        maxTup = (0, 0)

        #iterates row by row, column by column throuogh matrix
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row, col] > maxVal:
                    #if new value is found, update maxTup and maxVal
                    maxTup = (row, col)
                    maxVal = matrix[row, col]

        return maxTup

    def convolve(self, kernel, matrix):
        #kernel Inversion
        invKernel = np.zeros((len(kernel), len(kernel[0])))
        for col in range(0, len(kernel)):
            for row in range(0, len(kernel[0])):
                invKernel[col, row] = kernel[row, col]

        # padding matrix (generalized for kernal of any size)
        width = (len(matrix) + (2 * (len((kernel)) - 1)))
        length = (len(matrix[0]) + (2 * (len((kernel[0])) - 1)))
        tuple = (width, length)

        #initialize 2d arrays for padded copy and
        newMat = np.zeros((width-(len(kernel)+1), length-(len(kernel[0])+1)))
        copyMat = np.zeros((width, length))
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                copyMat[((len(kernel) - 1) + row), ((len(kernel[0]) - 1) + col)] = matrix[row, col]

        #matrix convolution
        for row in range(0, width - len(kernel) - 1):
            for col in range(0, length - len(kernel[0]) - 1):
                total = 0
                for kRow in range(0, len(kernel)):
                    for kCol in range(0, len(kernel[0])):
                        total = total + invKernel[kRow, kCol] * copyMat[(row + kRow), (col + kCol)]
                newMat[row, col] = total

        return newMat

    def run(self):
        print("Largest index is at ", self.largest_index(self._matrix))
        
        print("Result of convolution:")
        print(self.convolve(self._kernel, self._matrix))


if __name__ == "__main__":
    # If this file is run directly from the command line, run a test of the program
    m = MatrixOps()


    print("Running with matrix ")
    print(m._matrix)
    print("and kernel ")
    print(m._kernel)

    m.run() 