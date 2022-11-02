#Time Complexity:: O(n)-all nodes are traversed in the list+worst case O(2*n) when len(n)-1 = k
#Space Complexity:: O(1)-no extra space is ued
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0 #initially the length of linked list is 0
        temp = head #create  a temperory head
        
        if head==None or head.next==None: #edge case
            return head
        
        while temp!=None: #length of nodes is found
            temp= temp.next 
            length+=1
        
        if k>length:
            k=k%length #if the rotation is happending more times than the number of nodes then we can reduce the rotation
        currentHead= head
        while k>0:  #run while loop till all the rotations of the linked list are completed
            prev = currentHead #keep track of the previous node
            curr = currentHead.next #keep moving the current head
            while curr.next!=None: #move current head till the edn
                curr=curr.next
                prev=prev.next
            prev.next = None #make the previous node the end of the linked list
            curr.next = currentHead 
            currentHead = curr #make the curr as the new head
            k-=1 #keep reducing the number of rotations after each while loop iteration
       
        return currentHead