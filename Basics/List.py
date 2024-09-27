# x=int(input("Enter the number : "))
# while x<11:
#     print("Hello")
#     x=x+1


# x=int(input("Enter the number : "))
# while x<10:
#     print("Vipul")
#     x=x+1
# x = 4+5.5
# print(x)

# implicit = 41.4 + False
# print(implicit)

# explicit = int(22.2)
# print(explicit)




#Example of implicit conversion
# x=10
# print(" x is type of : ",type(x))
# y=10.6
# print("Y is the type of : ",type(y))
# z = x+y
# print(z)
# print("z is the type of : ",type(z))



#table of any number
# x=int(input("Enter the number : "))
# for i in range(1,11):
#     print(x*i)

# for i in range(1,11):
#     if(i==5):
#         break
#     print(i)

# x=int(input("Enter X : "))
# y=int(input("Enter Y : "))
# x=x+y
# y=x-y
# x=x-y
# print("After Swapping x : ",x)
# print("After swapping Y : ",y)

# def cube(x):
#     return x*x*x
# x=cube(3)
# print x

# for letter in 'Python' :
#     if letter == 'h':
#         break
#     print(letter)


# for letter in 'Python':
#     if letter == 'h':
#         continue
#     print(letter)

# for letter in 'Python':
#     if letter == 'h':
#         pass
#     print(letter)

# for letter in 'Python':
#     if letter == 'h':
#         pass
#     print(letter)

# n=3
# if n%2==0:
#     print("even")
# elif 

# y = int(input('Enter the Year : '))
# if(y%400==0) and (y%100==0):
#     print("{0} is a leap year".format(y))
# elif(y%4==0)and (y%100!=0):
#     print("{0} is a leap year : ".format(y))
# else:
#     print("{0} is not an leap year".format(y))
# count = 0
# while(count<3):
#     count = count+1
#     print(count)

# def isPalindrome(s):
#     return s == s[::-1]

# # s='malayalam'
# s=input("Enter word : ")
# ans=isPalindrome(s)

# if ans:
#     print("Yes")
# else:
#     print("No")
fruit = ['banana','litchi','guava']
if 'litchi' in fruit:
    print("yes")
if 'kiwi' not in fruit:
    print("no")