# --------------
#Code starts here
import sys
def palindrome(num):
    numstr = str(num)
    for i in range(num+1, sys.maxsize):
        if str(i) ==str(i)[:: -1]:
            return i
print(palindrome(12))


# --------------
def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)
a_scramble("ticket","chat")


# --------------
#Code starts here
from math import sqrt

#Code starts here

#Function to check for perfect square 
def is_perfect_square(x):
 
    s = sqrt(x)
    return (int(s)*int(s) == x) 
 
#Function to check for fibonacci number
def check_fib(num):
    if is_perfect_square((5*num*num) + 4) or is_perfect_square((5*num*num) - 4): #Formula for checking fibonacci number
        return True
    
    return False 


# --------------
#Code starts here
def compress(word):
    word = word.casefold()
    count=1
    length=""
    if len(word)>1:
        for i in range(1,len(word)):
            if word[i-1]==word[i]:
                count+=1
            else :
                length += word[i-1] + str(count)
                count=1
        
    else:
        i=0
    length += (word[i] + str(count))
    return length

compress("Ss")


# --------------
#Code starts here
def k_distinct(string, k):
    string = string.casefold()
    x = len(set(string))
    if x == k:
        return True
    else:
        return False

k_distinct('banana',4)


