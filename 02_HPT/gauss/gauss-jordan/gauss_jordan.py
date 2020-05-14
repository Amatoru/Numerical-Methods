import itertools


def pprint(matrix):
    m = len(matrix)
    n = len(matrix[0])

    print('[', end = '\t')
    for i in range(m-1):
        for j in range(n-1):
            print('{:.2f}'.format(matrix[i][j]), end='\t')
        print('| {:.2f}'.format(matrix[i][n-1]), end='\n\t')
    for j in range(n-1):
        print('{:.2f}'.format(matrix[m-1][j]), end='\t')
    print('| {:.2f}\t]'.format(matrix[m-1][n-1]))


def findMax(matrix, row, col):
    """ finf max in a region of matrix """
    for i in itertools.product(row, col):
        a = i[0]
        b = i[1]
        x = abs(matrix[a][b])

        if 'Max' in locals():
            if x > Max:
                Max = x
                pivot = i
        else:
            Max = x
            pivot = i

    return pivot


def findPriorityNumber(matrix,row, col, priorities=[1]):
    """ look for priority numbers in a region of matrix """
    for priority_number in priorities:
        for i in itertools.product(row, col):
            a = i[0]
            b = i[1]
            if priority_number == matrix[a][b]:
                return i


def gauss_jordan(matrix):
    m = len(matrix)                 # m phương trình
    n = len(matrix[0]) - 1          # n ẩn
    ind = [-1 for _ in range(m)]   # Danh sách vị trí chọn để khử
    row = [_ for _ in range(m)]     # các hàng cần duyệt
    col = [_ for _ in range(n)]     # các cột cần duyệt

    while row != [] and col != []:
        if findPriorityNumber(matrix, row, col) != None:
            a, b = findPriorityNumber(matrix, row, col)
        else:
            a, b = findMax(matrix, row, col)
        row.remove(a)
        col.remove(b)

        if matrix[a][b] != 0:  # Nếu max khác 0 thì bắt đầu khử
            ind[a] = b
            for i in [_ for _ in range(m) if _ != a]:
                c = matrix[i][b] / matrix[a][b]
                matrix[i] = [matrix[i][_] - c * matrix[a][_] for _ in range(n+1)]
        else:
            break

    for i, j in enumerate(ind):
        if matrix[i][j] != 0:
            matrix[i] = [matrix[i][_] / matrix[i][j] for _ in range(n+1)]

    # Kiểm tra xem hệ có vô nghiệm không
    for i, j in enumerate(ind):
        if j == -1:
            if matrix[i][n] != 0:
                print('Hệ phương trình vô nghiệm')
                return

    # Nếu không vô nghiệm thì đọc nghiệm
    inde = [_ for _ in range(n) if _ not in ind]  # Danh sách các ẩn tự do
    for i, j in enumerate(ind):
        if j != -1:
            BTTD = ''
            for k in inde:
                if matrix[i][k] not in [0, 0.0, -0.0]:
                    if matrix[i][k] > 0:
                        BTTD += ' - {:.2f}*x{}'.format(matrix[i][k], k)
                    else:
                        BTTD += ' + {:.2f}*x{}'.format(-matrix[i][k], k)
            print('x{} = {:.2f}'.format(j, matrix[i][n]) + BTTD)

