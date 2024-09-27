# j = 0
# while j<10:
#     print(j)
#     j=j+1

# x = 1
# while x == 1:
#     x = x-1
#     print(x)

# n = int(input("Enter a number : "))
# for i in range(n):
#     print("*"*3)

n = int(input("Enter a number  : "))
for i in range(n):
    for j in range(1,n+1):
        print(j,end="")
    print()