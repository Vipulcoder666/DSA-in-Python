arr = [1,2,3,5]
n = len(arr)+1
sum = n*(n+1)//2
arr_sum = 0

for i in range(len(arr)):
    arr_sum += arr[i]
ans = sum - arr_sum
print(ans)