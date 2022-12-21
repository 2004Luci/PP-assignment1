#Q.1.
'''
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target. You may assume that each input would have exactly one solution,
and you may not use the same element twice. You can return the answer in any order.

Example :

Input: nums = [2,7,11,15], target = 9 Output: [0,1] Explanation: Because nums[0] + nums[1] == 9,
we return [0, 1].
'''
L=[]
OL=[]
def two_sum(List,target):
    for i in range(len(List)):
        r=target-List[i]
        for j in List:
            if r==j:
                m=List.index(r)
                OL.append(m)
                
        


n=int(input("Enter value for n{Length of list}:"))
for j in range(n):
    ele=int(input("Enter element:"))
    L.append(ele)

print("Entered list:",L)

t=int(input("Enter value for target:"))

two_sum(L,t)

print(OL)
