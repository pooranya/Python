#que
Write a program to receive a number and check whether it is two’s power or not? In mathematics, a power of two is a number of the form 2^n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the exponent. ... Because two is the base of the binary numeral system, powers of two are common in computer science.

Input Format

Input contains an Integer

Constraints

1 = n1 = 200000000

Output Format

Print Yes or No

Sample Input 0

3
Sample Output 0

No




#ans
import math 
def Log2(x): 
    if x == 0: 
        return false; 
    return (math.log10(x) / math.log10(2)); 
def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n)));
a=int(input())
if(isPowerOfTwo(a)): 
    print("Yes"); 
else: 
    print("No"); 
    
