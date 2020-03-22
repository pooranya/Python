#ans
a=int(input())
if a<1:
    print("Wind condition is Calm")
elif a>=1 and a<=3:
    print("wind condition is Light Air")
elif a>=4 and a<=27:
    print("Wind condition is Breeze")
elif a>=28 and a<=47:
    print("Wind condition is Gale")
elif a>=48 and a<=63:
    print("Wind condition is Storm")
elif a>63:
    print("Wind condition is Hurricane")
    
 
 
 
 #que
 Here is a simplified version of the Beaufort scale, which is used to estimate the wind force. Write a program receives an integer input,then displays the corresponding description. Speed Description Less than 1 is Calm, 1- 3 is Light Air, 4 - 27 is Breeze, 28 – 47 is Gale, 48 – 63 is Storm and Above 63 is Hurricane

Input Format

Input Condition Interger

Constraints

1 = n1 = 100

Output Format

Wind condition is Calm / Light Air / Breeze/ Gale / Storm / Hurricane

Sample Input 0

2
Sample Output 0

wind condition is Light Air
    
   
