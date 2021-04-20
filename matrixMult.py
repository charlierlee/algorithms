
import math

LEAF_SIZE = 1
class MatrixMult:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def solve(self):
        return self.strassen(self.X, self.Y)

    def printMatrix(matrix):
        for line in matrix:
            print("\t".join(map(str, line)))

    def ikjMatrixProduct(self, A, B):
        n = len(A)
        C = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for k in range(n):
                for j in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C


    def add(self, A, B):
        n = len(A)
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, n):
            for j in range(0, n):
                C[i][j] = A[i][j] + B[i][j]
        return C


    def subtract(self, A, B):
        n = len(A)
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, n):
            for j in range(0, n):
                C[i][j] = A[i][j] - B[i][j]
        return C


    def strassenR(self, A, B):
        """
            Implementation of the self.strassen algorithm.
        """
        n = len(A)

        if n <= LEAF_SIZE:
            return self.ikjMatrixProduct(A, B)
        else:
            # initializing the new sub-matrices
            newSize = n // 2
            a11 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
            a12 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
            a21 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
            a22 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]

            b11 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
            b12 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
            b21 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
            b22 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]

            aResult = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
            bResult = [[0 for j in range(0, newSize)] for i in range(0, newSize)]

            # dividing the matrices in 4 sub-matrices:
            for i in range(0, newSize):
                for j in range(0, newSize):
                    a11[i][j] = A[i][j]  # top left
                    a12[i][j] = A[i][j + newSize]  # top right
                    a21[i][j] = A[i + newSize][j]  # bottom left
                    a22[i][j] = A[i + newSize][j + newSize]  # bottom right

                    b11[i][j] = B[i][j]  # top left
                    b12[i][j] = B[i][j + newSize]  # top right
                    b21[i][j] = B[i + newSize][j]  # bottom left
                    b22[i][j] = B[i + newSize][j + newSize]  # bottom right

            # Calculating p1 to p7:
            aResult = self.add(a11, a22)
            bResult = self.add(b11, b22)
            p1 = self.strassenR(aResult, bResult)  # p1 = (a11+a22) * (b11+b22)

            aResult = self.add(a21, a22)  # a21 + a22
            p2 = self.strassenR(aResult, b11)  # p2 = (a21+a22) * (b11)

            bResult = self.subtract(b12, b22)  # b12 - b22
            p3 = self.strassenR(a11, bResult)  # p3 = (a11) * (b12 - b22)

            bResult = self.subtract(b21, b11)  # b21 - b11
            p4 = self.strassenR(a22, bResult)  # p4 = (a22) * (b21 - b11)

            aResult = self.add(a11, a12)  # a11 + a12
            p5 = self.strassenR(aResult, b22)  # p5 = (a11+a12) * (b22)

            aResult = self.subtract(a21, a11)  # a21 - a11
            bResult = self.add(b11, b12)  # b11 + b12
            p6 = self.strassenR(aResult, bResult)  # p6 = (a21-a11) * (b11+b12)

            aResult = self.subtract(a12, a22)  # a12 - a22
            bResult = self.add(b21, b22)  # b21 + b22
            p7 = self.strassenR(aResult, bResult)  # p7 = (a12-a22) * (b21+b22)

            # calculating c21, c21, c11 e c22:
            c12 = self.add(p3, p5)  # c12 = p3 + p5
            c21 = self.add(p2, p4)  # c21 = p2 + p4

            aResult = self.add(p1, p4)  # p1 + p4
            bResult = self.add(aResult, p7)  # p1 + p4 + p7
            c11 = self.subtract(bResult, p5)  # c11 = p1 + p4 - p5 + p7

            aResult = self.add(p1, p3)  # p1 + p3
            bResult = self.add(aResult, p6)  # p1 + p3 + p6
            c22 = self.subtract(bResult, p2)  # c22 = p1 + p3 - p2 + p6

            # Grouping the results obtained in a single matrix:
            C = [[0 for j in range(0, n)] for i in range(0, n)]
            for i in range(0, newSize):
                for j in range(0, newSize):
                    C[i][j] = c11[i][j]
                    C[i][j + newSize] = c12[i][j]
                    C[i + newSize][j] = c21[i][j]
                    C[i + newSize][j + newSize] = c22[i][j]
            return C


    def strassen(self, A, B):
        assert type(A) == list and type(B) == list
        assert len(A) == len(A[0]) == len(B) == len(B[0])

        # Make the matrices bigger so that you can apply the strassen
        # algorithm recursively without having to deal with odd
        # matrix sizes
        nextPowerOfTwo = lambda n: 2 ** int(math.ceil(math.log(n, 2)))
        n = len(A)
        m = nextPowerOfTwo(n)
        APrep = [[0 for i in range(m)] for j in range(m)]
        BPrep = [[0 for i in range(m)] for j in range(m)]
        for i in range(n):
            for j in range(n):
                APrep[i][j] = A[i][j]
                BPrep[i][j] = B[i][j]
        CPrep = self.strassenR(APrep, BPrep)
        C = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j] = CPrep[i][j]
        return C
