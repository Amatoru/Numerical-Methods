import cmath


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


def isSymmetric(matrix):
    ''' Kiểm tra ma trận đối xứng '''
    n = len(matrix)

    # Kiểm tra ma trận vuông
    for i in range(n):
        if n != len(matrix[i]):
            return False

    # Kiểm tra tính đối xứng
    for i in range(n):
        for k in range(i):
            if matrix[i][k] != matrix[k][i]:
                return False
    return True


def cholesky(matrix):
    ''' Phân tách ma trận cỡ nxn về 2 ma trận L(ower) và U(pper) '''

    n = len(matrix)
    L = [ [0+0j for __ in range(n)] for _ in range(n) ]
    U = [ [0+0j for __ in range(n)] for _ in range(n) ]

    # Thực hiện thuật toán nếu matrix là ma trận đối xứng
    if isSymmetric(matrix):
        for i in range(n):
            U[i][i] = L[i][i] = cmath.sqrt(matrix[i][i] - sum([U[_][i]**2 for _ in range(i)]))
            if L[i][i] == 0:
                break
            for k in range(i, n):
                U[i][k] = L[k][i] = (matrix[i][k] - sum([U[_][i]*U[_][k] for _ in range(i)])) / U[i][i]
        if i == n-1:
            return L, U
    return None
