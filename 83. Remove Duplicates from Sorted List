'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=head
        while c:
            while c.next and c.next.val==c.val:
                c.next=c.next.next
            c=c.next
        return head
        
        
'''
Example 1:


Input: head = [1,1,2]
Output: [1,2]
'''
