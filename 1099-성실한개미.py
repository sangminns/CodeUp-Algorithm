def ant_func(temp, x, y):
    if int(temp[x][y]) == 0:
        temp[x][y] = 9
        ant_func(temp, x, y+1)
    elif int(temp[x][y]) == 1:
        if int(temp[x+1][y-1]) == 1:
            return
        ant_func(temp, x+1, y-1)
    else:
        temp[x][y] = 9
        return
        
arr = [[0]*10 for i in range(10)]

for i in range(10):
    li = input().split(" ")
    for j in range(10):
        arr[i][j] = li[j]
        
ant_func(arr, 1, 1)

for i in range(10):
    for j in range(10):
        print(arr[i][j], end=" ")
    print("")