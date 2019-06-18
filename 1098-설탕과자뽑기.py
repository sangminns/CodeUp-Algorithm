row, col = input().split(" ")

row = int(row)
col = int(col)

n = int(input())

arr = [[0]*100 for i in range(100)]

for i in range(n):
    stick_l, stick_d, x, y = input().split(" ")
    stick_l = int(stick_l)
    stick_d = int(stick_d)
    x = int(x)
    y = int(y)
    
    arr[x-1][y-1] = 1
    for j in range(1, stick_l):
        
        if stick_d == 1:
            arr[x-1+(stick_l-j)][y-1] = 1
        else:
            arr[x-1][y-1+(stick_l-j)] = 1

for i in range(row):
    for j in range(col):
        print(arr[i][j], end=" ")
    print("")
