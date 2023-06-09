'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Arr1=sorted(nums1)
        Arr2=sorted(nums2)

        i=0
        j=0

        result=[]
        while i<len(Arr1) and j<len(Arr2):
            if Arr1[i] < Arr2[j]:
                i += 1
            elif Arr2[j]<Arr1[i]:
                j += 1
            else:
                result.append(Arr1[i])
                i += 1
                j += 1
        return result
        
        
'''
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
'''
# secondary solution

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        a = Counter(nums1)
        b = Counter(nums2)
        for i,j in a.items():
            if i in b:
                l+=[i]*min(j,b[i])
        return l
