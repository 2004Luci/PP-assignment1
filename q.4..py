#Q.4.
'''
You are given an array prices where prices [i] is the price of a given stock on
the ith day. You want to maximize your profit by choosing a single day to buy 
one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example :

Input: prices = [7,1,5,3,6,4]; Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed
because you must buy before you sell.
'''
def max_profit(prices):
    maximum= prices[1]-prices[0]
    for index in range(len(prices)):
        for i in range (index+1,len(prices)):
            maximum=max(prices[i]-prices[index], maximum)
    if maximum>0:       
     print (maximum) 
    else: 
     print(0) 

arrays=[]
n=int(input("Enter the number of elements in array"))
for i in range (n):
 val=int(input("Enter the prices of stocks"))
 arrays.append(val)

max_profit(arrays)
