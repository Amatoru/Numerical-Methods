

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


def LU_decompostion(matrix):
    ''' Phân tách ma trận cỡ nxn về 2 ma trận L(ower) và U(pper) '''
    n = len(matrix)
    L = [ [0 for __ in range(n)] for _ in range(n) ]
    U = [ [0 for __ in range(n)] for _ in range(n) ]
    for i in range(n):
        U[i][i] = 1

    if len(matrix[0]) == n:
        for _ in range(n):
            L[_][0] = matrix[_][0]
            U[0][_] = matrix[0][_] / L[0][0]

        for t in range(1, n):
            for i in range(t, n):  # Tính các phần tử ở cột t của L
                L[i][t] = matrix[i][t] - sum([ L[i][_]*U[_][t] for _ in range(t) ])

            if L[t][t] == 0:
                break
            for k in range(t+1, n):  # Tính các phần tử ở hàng t của U
                U[t][k] = (matrix[t][k] - sum([ L[t][_]*U[_][k] for _ in range(t) ])) / L[t][t]
        if t == n-1:
            return L, U

    print("Error: can't do LU decomposition for this matrix")
    return None

