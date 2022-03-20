# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        print("n ", n)
        print("head ", head)
        
        list_count = 0
        first_head = head
        
        while True:
            list_count = list_count + 1
            print(" mid head: ", first_head, " #", list_count)

            if first_head.next != None:
                first_head = first_head.next
            else:
                break                    
            
        # print("final head: ", head)
        
        if list_count == 1:
            # the minimum, and n at least is 1
            return None
        
        run_end_number = list_count - n
        print("run_end ", run_end_number)
        
        if run_end_number == 0:
            # remove the head
            if head.next != None:
                head = head.next
                return head
            else:
                head = None
                return head
            
        
        second_count = 0
        second_head = head
        while True:
            
            second_count = second_count + 1
            print(" second head: ", second_head, " #", second_count)

            if second_count < run_end_number:
                # do usual things
                if second_head.next != None:
                    second_head = second_head.next
                else:
                    break              
            else:
                # must be equal when it stop counting
                mid_head = second_head.next
                print("remove this, ", mid_head)
                if mid_head.next != None:
                    mid_head = mid_head.next
                    second_head.next = mid_head
                    print("next_candidate, ", mid_head)

                    break
                else:
                    print("next_candidate, None")
                    second_head.next = None
                    break
        return head


# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         sz = 0
#         p = head
#         while p != None:
#             p = p.next
#             sz += 1
#         p = head
#         if sz == n:
#             head = head.next
#         for i in range(sz-n-1):
#             p = p.next
#         if p.next != None:
#             p.next = p.next.next
#         return head


if __name__ == "__main__":

    obj = Solution()
    # ans = obj.removeNthFromEnd(intervals)


    # print(ans)