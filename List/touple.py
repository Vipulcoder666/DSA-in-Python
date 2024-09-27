# input_tuple = (1,2,3,4,5,6)
# list=[]
# for x in reversed(input_tuple):
#     list.append(x)
# output_tuple=tuple(list)
# print(output_tuple)

l1 = [1,5,5]
l2 = [3,4,5,5,10]
l3 = [5,5,10,20]

s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

s1 = s1.intersection (s2)
s1 = s1.intersection (s3)
s1 = list(s1)
print(s1)