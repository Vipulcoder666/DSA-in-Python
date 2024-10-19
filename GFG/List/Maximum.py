# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# union_list = list(set(list1) | set(list2))
# print(union_list)


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

c = list(set(list1) | set(list2))
print("The union is : ",c)
print(len(c))

# for i in range(0,len(c)):
#     print(i)