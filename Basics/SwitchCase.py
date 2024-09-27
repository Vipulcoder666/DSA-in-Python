num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))

operator  = input("Enter input operator : ")


# At the place of switch we will put match in python
match operator:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)