arr = [[0]*19 for i in range(19)]

for i in range(0, 19):
  input_arr = input().split(" ")
  for j in range(0, 19):
    arr[i][j] = input_arr[j]

n = int(input())

for k in range(n):
  n_x, n_y = input().split(" ")
  n_x = int(n_x)
  n_y = int(n_y)
  for i in range(19):
    if arr[i][n_y-1] == 0:
      arr[i][n_y-1] = 1
    else :
      arr[i][n_y-1] = 0
    for j in range(19):
      if arr[n_x-1][j] == 0:
        arr[n_x-1][j] = 1
      else:
        arr[n_x-1][j] = 0


for i in range(19):
  for j in range(19):
    print(arr[i][j], end=" ")
  print("")
