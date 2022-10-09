 #!/usr/bin/python
"""
Python  Functions
"""
import math
from math import sqrt

"""
Question 1: 

Finish the function valid_brackets() to solve the following question.

Given a string s containing just the characters '(', ')' determine if the input string is valid.
An input string is valid if:
1.All brackets are closed in the correct order.
2.Open bracket must be placed before close bracket.

Example 1:
 Input: s = "()"
 Output: True
Example 2:
 Input: s = "("
 Output: False
Example 3:
 Input: s = "(()"
 Output: False
Example 4:
 Input: s = ")("
 Output: False
Example 5:
 Input: s = "()()"
 Output: True
Example 6:
 Input: s = "(()())"
 Output: True
Example 7:
 Input: s = ""
 Output: True
"""
def valid_brackets(s):
 leftSymbols = []
    # Loop for each character of the string
 for c in s:
        # If left symbol is encountered
       if c in ['(', '{', '[']:
           leftSymbols.append(c)
        # If right symbol is encountered
       elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
           leftSymbols.pop()
       elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
           leftSymbols.pop()
       elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
           leftSymbols.pop()
        # If none of the valid symbols is encountered
       else:
           return False
 return leftSymbols == []



"""
Question 2:

Finish the function is_prime() to solve the following question.

Given a number n determine if the number string is Prime number.

Example 1:
    Input: n = 1
    Output: False
    
Example 2:
    Input: n = 2
    Output: True
    
Example 3:
    Input: n = 6
    Output: False

Example 4:
    Input: n = 97
    Output: True
    
Example 5:
    Input: n = 9973
    Output: True

"""
def is_prime(n):
 prime_flag = 0
 if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        return(True)
    else:
        return(False)
 else:
   return(False)



"""
Question 3:

Finish the function GCD() to solve the following question.
 
Find Greatest Common Divisor of two positive integer a and b. 

Example 1:
    Input: a = 6 , b = 12
    Output: 6
    
Example 2:
    Input: a = 9 , b = 12
    Output: 3

Example 3:
    Input: a = 42 , b = 12
    Output: 6
    
Example 4:
    Input: a = 97 , b = 7
    Output: 1
"""


def GCD(a, b):
 hcf = math.gcd(a,b)
 return(hcf)


