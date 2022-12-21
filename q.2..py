#Q.2.
#Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
'''
Example :

Input: x = 2.00000, n = 10 Output: 1024.00000
'''

def pow(x,n):
    r=x**n
    print(x, ' raised to the power', n, ' is equal to',r)

x=int(input("Enter value for base number:"))
n=int(input("Enter value for exponent:"))
pow(x,n)
