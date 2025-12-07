class SinglyNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        return str(self.val)

def delete_node(head, val_delete): # TODO CHECK
    # list is empty
    if not head:
        return None

    # 👾 delete head
    # if the fist node is the one that we want to delete, 
    # move the 'head' tag to the next
    if head.val == val_delete:
        return head.next

    # it is in the middle or end
    current = head

    # search the prev node 
    # if there are next node, is the val_delete?
    while current.next:
        if current.next.val == val_delete:
            current.next = current.next.next
            return head # end, return list
        current = current.next # keep searching

    return head # the value is not in the list

# auxiliar function
def printList(head): # o(n)
    curr = head
    while curr:
        print(f"{curr.val} -> ",end="")
        curr = curr.next
    print("None")

# search for node value - O(n)
def search(head,val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False

# reverse a list
def reverse_list(head):
    prev = None # there is nothing before of the head
    curr = head # start head in current node

    while curr:
        next_temp = curr.next # save the next node 
        curr.next = prev # reverse the arrow 

        # next the pointer one step
        prev = curr
        curr = next_temp
    
    return prev # prev is the new head (previous end)

def has_cycle(head):
    slow = head # tortuga
    fast = head # liebre

    while fast and fast.next: #while liebre has free path
        slow = slow.next # turtle one step
        fast = fast.next.next # liebre two steps

        if slow == fast:  # if there is a moment that both are in the same position
            return True
    return False # liebre is in the end, there is not cycle

# manual creation
node1 = SinglyNode(1)
node2 = SinglyNode(2)
node3 = SinglyNode(3)
node4 = SinglyNode(4)

# manual connection
node1.next = node2
node2.next = node3
node3.next = node4

print("Original list")
printList(node1)

print("Reverse list")
new_head = reverse_list(node1)
printList(new_head)


print("\nSearch")
print(search(node1,8))

# print("Delete 3")
# head = delete_node(node1,3)
# printList(head)


# print("Testing cycle")
# node1.next = node3
# has_cycleNode = has_cycle(new_head)
# print(f"has cycle? {has_cycleNode}" )