# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        recorded_link_set = set([])
        is_looped = False
        current_node = head
        pos = 0
        
        if current_node != None:
            while current_node.next != None:
                if current_node in recorded_link_set:
                    print(recorded_link_set)
                    is_looped = True
                    return is_looped
                else:
                    ## not exist before
                    recorded_link_set.add(current_node)
                
                current_node = current_node.next

            if is_looped == False:
                pos = -1

        print(pos)
        return is_looped

        # slow_runner = head
        # fast_runner = head
        
        # while fast_runner is not None and fast_runner.next is not None:
        #     slow_runner = slow_runner.next
        #     fast_runner = fast_runner.next.next
            
        #     if slow_runner == fast_runner:
        #         return True
            
        # return False



    def copy_node(self, target_node, result_node):

        result_node = ListNode(target_node.val)
        result_node.next = target_node.next
        return result_node