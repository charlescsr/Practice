import sys
def hourglassSum(arr):
    m=-sys.maxsize-1
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            m=max(m,arr[i][j]+arr[i][j+1] + arr[i][j+2]+ arr[i+1][j+1]+ arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])

    return m

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
hourglassSum(arr)