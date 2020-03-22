#ans
a=int(input())
b=a*a
c=str(b)
d=int(c[::-1])
e=str(a)
f=e[::-1]
g=int(f)
h=g*g
if d==h:
    print("Adam No")
else:
    print("Not Adam No")
    
    
    
  
#que
Write a program to check whether the given number is an adam number or not. Adam number is a number when reversed, the square of the number and the square of the reversed number should be numbers which are reverse of each other.

Input Format

Input format will be an integer

Constraints

1 = num = 100000000

Output Format

Print Adam No. or Not Adam No.

Sample Input 0

12
Sample Output 0

Adam No
Explanation 0

Input : 12 Output : Adam Number Explanation: Square of 12 = 144 Reverse of 12 = 21 Square of 21 = 441 Now Square of 12 and square of reverse of 12 are reverse of each other. Therefore 12 is Adam number.

