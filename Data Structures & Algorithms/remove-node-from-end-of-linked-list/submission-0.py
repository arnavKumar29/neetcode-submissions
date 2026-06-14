# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0;
        temp=head;
        while(temp):
            count+=1;
            temp=temp.next;
        remove=count-n;
        if(remove==0):
            return head.next;
        curr=head;
        for i in range(count-1):
            if(i+1)==remove:
                curr.next=curr.next.next
                break
            curr=curr.next
        return head
        
        


        