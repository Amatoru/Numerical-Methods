def pprint(matrix):
    m = len(matrix)
    n = len(matrix[0])

    print('[', end = '\t')
    for i in range(m-1):
        for j in range(n-1):
            print('{}'.format(matrix[i][j]), end='\t')
        print('| {}'.format(matrix[i][n-1]), end='\n\t')
    for j in range(n-1):
        print('{}'.format(matrix[m-1][j]), end='\t')
    print('| {}\t]'.format(matrix[m-1][n-1]))


def gauss(matrix):
    m = len(matrix)         # m phương trình
    n = len(matrix[0]) - 1  # n ẩn
    ind = []                # Danh sách vị trí khác 0 đầu tiên ở mỗi hàng

    i = j = 0
    while (i < m and j < n+1):
        # Tìm vị trí đầu tiên khác không của mỗi hàng
        if matrix[i][j] != 0:
                ind.append(j)
        else:
            found_non_zero = False
            for t in range(i+1, m):
                if matrix[t][j] != 0:
                    found_non_zero = True
                    temp = matrix[t]
                    matrix[t] = matrix[i]
                    matrix[i] = temp
                    ind.append(j)
                    break
            if found_non_zero == False:
                j += 1
                continue

        if ind[i] == n:
            print("Hệ phương trình vô nghiệm")
            return

        # Khử các vị trí dưới
        for k in range(i+1, m):
            c = matrix[k][j] / matrix[i][j]
            matrix[k] = [matrix[k][_] - c * matrix[i][_] for _ in range(n+1)]

        i += 1
        j += 1

    # Khử các vị trí trên
    for j in list(reversed(ind)):
        i = ind.index(j)
        for k in range(i-1, -1, -1):
            c = matrix[k][j] / matrix[i][j]
            matrix[k] = [ matrix[k][_] - c * matrix[i][_] for _ in range(n+1)]

    for i, j in list(enumerate(ind)):
        matrix[i] = [matrix[i][_] / matrix[i][j] for _ in range(n+1)]

    # Đọc nghiệm

    inde = [_ for _ in range(n) if _ not in ind]  # Lưu các vị trí có biến tự do
    for i, j in enumerate(ind):
        BTTD = ''
        for k in inde:
            if matrix[i][k] not in [0, 0.0, -0.0]:
                if matrix[i][k] > 0:
                    BTTD += ' -{}*x{} '.format(matrix[i][k], k)
                else:
                    BTTD += ' +{}*x{} '.format(-matrix[i][k], k)

        print('x{} = {}'.format(j, matrix[i][n]) + BTTD)

