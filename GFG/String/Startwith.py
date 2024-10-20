# String Functions - II - Python

# Given a string S, the task is to determine whether the string starts and ends with the characters 'gfg' (case insensitive). In order to complete this task, you need to utilize the string functions S.lower(), S.upper(), S.startswith('string2'), and S.endswith('string2'). By using these functions, you can check if the given string S meets the specified conditions of starting and ending with 'gfg'.

# Example 1:

# Input:
# S: "gFgabcdEGfG"
# Output:
# Yes
# Explanation:
# The given string "gFgabcdEGfG" starts with "gfg" and also ends with "gfg" after converting it to lowercase ("gfgabcdegfg"), so the output is Yes.

def gfg(S):
    b = S.lower()
    # startswith()  and endswith ()
    if(b.startswith("gfg") and b.endswith("gfg")):  
        print ("Yes")
    else:
        print ("No")