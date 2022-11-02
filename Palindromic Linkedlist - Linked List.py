#Time Complexity:: O(n)-all nodes are visited more than twice a single traversal
#Space Complexity:: O(1)-no extra space used
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reverse = None #create reverse node
        slow = head
        fast = head
        while fast and fast.next: #runs loop till fast reaches the second last node
            fast = fast.next.next #move fast twice as fast as slow
            reverse, reverse.next, slow = slow, reverse, slow.next #reverse the linked list from the slow node
        if fast: #if fast is not none
            slow = slow.next #then move slow
        while reverse and reverse.val == slow.val: #while both ends of the original linked list have same value 
            slow = slow.next #keep moving slow pointer
            reverse = reverse.next #keep moving reverse pointer
        return not reverse #if reverse pointer hits none then not none=True is returned, otherwise if reverse node is stopped on a node in the reversed half of linked list then return not True node= False is returned. 