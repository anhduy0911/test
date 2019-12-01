def findPath(matrix):
    x0 = 0
    y0 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                x0 = i
                y0 = j
                break
    flag = 0
    target = 2
    while flag == 0:
        if target > len(matrix) * len(matrix[0]):
            break
        if x0 < len(matrix) - 1:
            if matrix[x0+1][y0] == target:
                x0 += 1
                target += 1
                continue
        if x0 > 0:
            if matrix[x0-1][y0] == target:
                x0 -= 1
                target += 1
                continue
        if y0 > 0:
            if matrix[x0][y0-1] == target:
                y0 -= 1
                target += 1
                continue
        if y0 < len(matrix[0]) - 1:
            if matrix[x0][y0+1] == target:
                y0 += 1
                target += 1
                continue
        else:
            flag = 1
    if flag == 1:
        return False
    else:
        return True

print(findPath([[2,3,4,5],[1,8,7,6],[12,9,10,11]]))

#this is a change made to the file to see what happen