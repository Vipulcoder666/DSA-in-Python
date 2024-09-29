def factorial(n):
    answ = 1
    if n == 0:
        answ = 1
    else:
        for i in range(1,n+1):
            answ *= i
        return answ


n = int(input("Enter n : "))
output = factorial(n)
print(output)