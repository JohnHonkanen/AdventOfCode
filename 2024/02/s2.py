def read_input(filename):
    ret_matrix = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            ret_matrix.append(list(map(int, line.split())))
    return ret_matrix

def is_safe(x,y):
    opsign = -1 if x - y >= 0 else 1
    if abs(x - y) > 3 or abs(x - y) < 1:
        return False, opsign
    return True, opsign

if __name__ == '__main__':
    matrix = read_input('input.txt')
    matrix =[[9,1,8,7,6,5,4], [8,9,8,7,6,5,4,3,2,1], [3,4,5,6,1,8,9], [1,2,3,4,5,6], [6,5,4,3,2,1], [1,5,3,5,3,2,1]]
    matrix =[[1,5,3,5,3,2,1]]

    ans = 0
    for i in range(0, len(matrix)):
        innerLen = len(matrix[i])
        pos = list()
        neg = list()
        total_fail = 0
        for j in range(0, innerLen-1):
            [safe, sign] = is_safe(matrix[i][j], matrix[i][j+1])

            if safe:
                if sign == 1:
                    pos.append(j)
                else:
                    neg.append(j)
            else:
                total_fail += 1

        print(total_fail, len(pos), len(neg), innerLen)

        if total_fail < 3:
            if len(pos) + total_fail < 3:
                ans += 1
            if len(neg) + total_fail < 3:
                ans += 1

    print(ans)