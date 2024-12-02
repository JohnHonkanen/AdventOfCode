def read_input(filename):
    ret_matrix = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            ret_matrix.append(list(map(int, line.split())))
    return ret_matrix

if __name__ == '__main__':
    matrix = read_input('input.txt')
    matrix = [[8, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
    ans = 0
    for i in range(0, len(matrix)):
        innerLen = len(matrix[i])

        sign = 1 if matrix[i][0] - matrix[i][1] >=0 else -1
        failedNum = 0
        for j in range(0, innerLen-1):
            if failedNum > 1:
                break

            cacheOp = abs(matrix[i][j] - matrix[i][j + 1])
            opsign = 1 if cacheOp >=0 else -1
            if sign != opsign:
                failedNum += 1
                if j == 0:
                    sign = 1 if matrix[i][1] - matrix[i][2] >=0 else -1
                continue

            if cacheOp > 3 or cacheOp < 1:
                failedNum += 1
                continue

        if failedNum < 2:
            print(matrix[i])
            ans+=1

    print(ans)