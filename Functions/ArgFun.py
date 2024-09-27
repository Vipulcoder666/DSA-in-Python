def Sum(*args):
    total = 0
    for i in args:
        total += i
    return total

output = Sum(1,2,3,4,5)
print("The sum is : ",output)

# Arbitary arguments  are used where we dont know that how many parameters we have to enter in the function.
# we can add n numbers of parameter by using Arbitary arguments .