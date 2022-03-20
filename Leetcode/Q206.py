# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# head = [1,2,3,4,5]
# head = [1,2]
# head = []



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # give a root

        print("head = ", head)
        if not head:
            # print("This is an empty list")
            return head
        
        current = None
        current = self.copy_node(head, current)

        previous = None

        new_current = None
        current_list = []

        while True:
            # current_list.append(current.val)

            new_current = self.copy_node(current, new_current)
            if current.next == None:
                new_current.next = previous
                break
            else:

                new_current.next = previous


                previous = self.copy_node(new_current, previous)

                current = current.next

        new_head =None
        new_head = self.copy_node(new_current, new_head)

        
        return new_head
    
    def copy_node(self, target_node, result_node):

        result_node = ListNode(target_node.val, target_node.next)
        return result_node

if __name__ == "__main__":

    obj = Solution()
    ans = obj.reverseList(head)


    print(ans)
