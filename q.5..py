#Q.5.
'''
 Given a string x, return true if x is a palindrome, and false otherwise.

Example :

Input: x = 121 Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''

x=str(input('Enter string:'))
t=x[::-1]
if x==t:
    print('True')
else:
    print('False')
