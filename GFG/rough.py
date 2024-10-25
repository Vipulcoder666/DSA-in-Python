arr = [0, 2, 1, 2, 0]
for i in range(len(arr)):
    if arr[0] >= arr[i]:
        arr[0] += 1
    else:
        arr[i] += 1
print(arr)