def read_input(filename):
    ret_matrix = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            ret_matrix.append(list(map(int, line.split())))
    return ret_matrix

if __name__ == '__main__':
    matrix = read_input('input.txt')
    ans = 0
    for i in range(0, len(matrix)):
        innerLen = len(matrix[i])
        # if abs(matrix[i][0] - matrix[i][innerLen - 1]) > innerLen*3+1:
        #     print(matrix[i])
        #     continue


        sign = 1 if matrix[i][0] - matrix[i][1] >=0 else -1
        passed = True
        for j in range(0, innerLen-1):
            opsign = 1 if matrix[i][j] - matrix[i][j+1] >=0 else -1
            if sign != opsign:
                passed = False
                break

            if abs(matrix[i][j] - matrix[i][j+1]) > 3 or abs(matrix[i][j] - matrix[i][j+1]) < 1:
                passed = False
                break

        if passed:
            print(matrix[i])
            ans+=1

    print(ans)