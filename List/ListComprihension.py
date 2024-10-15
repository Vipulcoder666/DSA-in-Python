# normal way to find cubes

# cubes = []
# for x in range(10):
#     if x%2 == 0:
#         print(x ** 3)


# List comprihension way


cubes = [x ** 3 for x in range (10) if x%2==0]
print(cubes)
