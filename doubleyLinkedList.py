class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)
    

head = tail = DoublyNode(1)

def display(head):
    curr = head
    items = []
    while curr:
        items.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(items))


#insert at beggining O(1)
def insert_beggining(head, tail, val):
    new_node = DoublyNode(val, next=head)



