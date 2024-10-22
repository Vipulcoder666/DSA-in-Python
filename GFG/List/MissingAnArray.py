arr = [1,2,3,5]
n=5
sum = (n*(n+1))/2
arr_sum = 0
for i in range(0,len(arr)):
    arr_sum += arr[i]
print("Sum of first n numbers:", sum)
print("Sum of elements in array:", arr_sum)

sol = (sum - arr_sum)
print(sol)