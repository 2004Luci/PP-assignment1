#Q.3.
'''
You are given a large integer represented as an integer, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example :

Input: number = 123 Output: [1,2,4]
Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4]
'''
L=[]
OL=[]
n=int(input('Enter number:'))
n+=1
def increment(number):
    t=str(n)
    for i in t:
        L.append(i)
    for j in L:
        h=int(j)
        OL.append(h)

    

increment(n)
print(OL)
    
