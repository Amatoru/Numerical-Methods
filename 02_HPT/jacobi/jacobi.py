import numpy as np


def pprint(matrix):
    ''' In ma trận gọn hơn '''
    m = len(matrix)
    n = len(matrix[0])

    print('[', end = '\t')
    for i in range(m-1):
        for j in range(n-1):
            print('{:.2f}'.format(matrix[i][j]), end='\t')
        print('{:.2f}'.format(matrix[i][n-1]), end='\n\t')
    for j in range(n-1):
        print('{:.2f}'.format(matrix[m-1][j]), end='\t')
    print('{:.2f}\t]'.format(matrix[m-1][n-1]))


#==============================================================================
def isSquare(matrix):
    return len(matrix) == len(matrix[0])

def isRowDiagonalDominance(matrix):
    ''' Kiểm tra tính chéo trội hàng '''
    if isSquare(matrix):
        n = len(matrix)
        for i in range(n):
            if matrix[i][i] < sum([matrix[i][j] for j in range(n) if j != i]):
                return False
        return True
    return False

def isColDiagonalDominance(matrix):
    ''' Kiểm tra tính chéo trội cột '''
    if isSquare(matrix):
        n = len(matrix)
        for j in range(n):
            if matrix[j][j] < sum([matrix[i][j] for i in range(n) if i != j]):
                return False
        return True
    return False

#==============================================================================
def jacobi(A, b, eps=0.001):
    ''' Phương pháp lặp Jacobi giải phương trình Ax = b '''

    n = len(A)
    x0 = np.array([ [0] for _ in range(n) ])  # Khởi tạo phần tử đầu tiên
    I = np.identity(n)

    # A là ma trận chéo trội hàng
    if isRowDiagonalDominance(A):
        # Khởi tạo các biến phục vụ việc tính toán sai số
        T = np.array([ [0.0 for _ in range(n)] for __ in range(n) ])
        for i in range(n):
            T[i][i] = 1 / A[i][i]
        B = I - np.matmul(T, A)
        norm_inf_B = np.linalg.norm(B, np.inf)
        d = np.matmul(T, b)

        x = np.matmul(B, x0) + d  # Bắt đầu lặp
        # Đánh giá sai số eps theo hậu nghiệm
        prev = x0.copy()
        cur = x.copy()
        delta = np.linalg.norm(cur-prev, np.inf)
        while ( norm_inf_B/(1-norm_inf_B)*delta > eps ):
            prev = x.copy()
            x = np.matmul(B, x) + d
            cur = x.copy()
            delta = np.linalg.norm(cur-prev, np.inf)
        return x

    # A là ma trận chéo trội cột
    if isColDiagonalDominance(A):
        # Khởi tạo các biến phục vụ việc tính toán sai số
        T = np.array([ [0.0 for _ in range(n)] for __ in range(n) ])
        max_aii = A[0][0]
        min_aii = A[0][0]
        for i in range(n):
            T[i][i] = A[i][i]
            if T[i][i] > max_aii:
                max_aii = T[i][i]
            elif T[i][i] < min_aii:
                min_aii = T[i][i]
        B1 = I - np.matmul(A, T)
        norm_1_B1 = np.linalg.norm(B, 1)
        B = I - np.matmul(T, A)
        d = np.matmul(T, b)

        x = np.matmul(B, x0) + d  # Bắt đầu lặp
        # Đánh giá sai số eps theo hậu nghiệm
        prev = x0
        cur = x
        delta = np.linalg.norm(cur-prev, 1)
        while ( (max_aii/min_aii)*(norm_1_B1/(1-norm_1_B1))*delta > eps ):
            prev = x.copy()
            x = np.matmul(B, x) + d
            cur = x.copy()
            delta = np.linalg.norm(cur-prev, 1)
        return x

    print("Sorry, Jacobi can't help you")
    return None
