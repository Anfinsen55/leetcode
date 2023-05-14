'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

'''

class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		res=0
		presum=0
		dict1={0:1}

		for i in  nums:
			presum = presum + i

			if (presum-k) in dict1:
				res = res + dict1[presum-k]

			if presum not in dict1:
				dict1[presum] = 1
			else:
				dict1[presum] = dict1[presum]+1

		return res
  
  
'''
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
'''
