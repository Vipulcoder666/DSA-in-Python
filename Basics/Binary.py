arr = [10,20,30,40,50]
target = 40
left,right = 0,len(arr)-1
while left <= right:
    mid = (left + right)//2
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        left = mid+1
    else:
        right = mid-1
