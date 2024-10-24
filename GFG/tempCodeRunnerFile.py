arr = [16, 17, 4, 3, 5, 2]
count = arr[-1]
leader = [count]
print(count,end=' ')

for i in range(len(arr) -2,-1,-1):
    if arr[i] >= count:
        count = arr[i]
        leader.append(count)

leader.reverse()
print(leader,end=' ')