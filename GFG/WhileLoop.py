#  Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.

def printInDecreasing(x):
    # Complete the code below
    while(x >= 0):
      
        x -= 1
        
        print(x+1,end=" ")