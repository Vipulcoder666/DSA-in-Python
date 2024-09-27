num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")

choice = int(input("Please enter the chouce : "))

if choice == 1:
    print("Addition of ", num1, "and" ,num2, "is : ", num1+num2)
elif choice == 2:
    print("Sub of",num1, "and", num2 ,"is : ",num1-num2)
elif choice == 3:
    print("Mul of ",num1,"and",num2,"is : ",num1*num2)
elif choice == 4:
    print("Division of ",num1,"and",num2 , "is : ",num1/num2)
else:
    print("Invalid no. entered !!!!!")