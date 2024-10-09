class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.left = ListNode('l')
        self.right = ListNode('r')
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        node = self.getNode(index)
        return node.val if node and node is not self.right else -1

    def addAtHead(self, val: int) -> None:
        self.addNode(ListNode(val), self.left, self.left.next)

    def addAtTail(self, val: int) -> None:
        self.addNode(ListNode(val), self.right.prev, self.right)

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.getNode(index)
        if cur:
            self.addNode(ListNode(val), cur.prev, cur)

    def deleteAtIndex(self, index: int) -> None:
        cur = self.getNode(index)
        if cur and cur is not self.right:
            prev, nxt = cur.prev, cur.next
            prev.next = nxt
            nxt.prev = prev

    def getNode(self, index: int):
        cur = self.left.next

        while cur and index > 0:
            index -= 1
            cur = cur.next

        if cur and index == 0:
            return cur

        return None

    @staticmethod
    def addNode(node, prev, nxt):
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def __str__(self):
        res = ''
        cur = self.left

        while cur:
            res += str(cur.val) + ('->' if cur.val != 'r' else '')
            cur = cur.next

        return res


# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = LinkedList()
print(myLinkedList)
myLinkedList.addAtHead(1)
print(myLinkedList)
myLinkedList.addAtTail(3)
print(myLinkedList)
myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
print(myLinkedList)
myLinkedList.get(1)              # return 2
print(myLinkedList)
myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
print(myLinkedList)
myLinkedList.get(1)              # return 3
print(myLinkedList)

print(myLinkedList)

print()

ll2 = LinkedList()
print(ll2)
ll2.addAtHead(7)
print(ll2)
ll2.addAtHead(2)
print(ll2)
ll2.addAtHead(1)
print(ll2)
ll2.addAtIndex(3, 0)
print(ll2)
ll2.deleteAtIndex(2)
print(ll2)
ll2.addAtHead(6)
print(ll2)
ll2.addAtTail(4)
print(ll2)
print(ll2.get(4))
ll2.addAtHead(4)
print(ll2)
ll2.addAtIndex(5, 0)
print(ll2)
ll2.addAtHead(6)
print(ll2)


