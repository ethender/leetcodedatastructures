"""
347. Top K Frequent Elements


Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

- 1 <= nums.length <= 105
-  -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        temp = {}

        '''
            - append the keys in dict
        '''
        for i in nums:
            if i in temp:
                temp[i] = 1+temp[i]
            else:
                temp[i] = 1

        '''
            Sort the keys in frequent manner
        '''
        for i in range(1,k+1):
            counter = 0
            key=""
            for ikey in temp.keys():
                if temp[ikey] > counter:
                    counter = temp[ikey]
                    key = ikey
            
            result.append(key)
            temp.pop(key,None)
        
        return result