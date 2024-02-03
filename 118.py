def generate(numRows):
    res = [[1]]
    if numRows == 1 :
        return res
    for j in range(numRows - len(res)):
        last = [1]
        for i in range(len(res[len(res)-1])-1):
            last.append(res[len(res)-1][i] + res[len(res)-1][i+1])
        last.append(1)
        res.append(last)
    return res
