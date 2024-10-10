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
        self.len = 0

    def get(self, index: int) -> int:
        node = self.getNode(index)
        return node.val if node is not None and node is not self.right and node is not self.left else -1

    def addAtHead(self, val: int) -> None:
        self.addNode(val, self.left, self.left.next)
        self.len += 1

    def addAtTail(self, val: int) -> None:
        self.addNode(val, self.right.prev, self.right)
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.getNode(index)
        if cur:
            self.addNode(val, cur.prev, cur)
            self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        cur = self.getNode(index)
        if cur and cur is not self.right and cur is not self.left:
            prev, nxt = cur.prev, cur.next
            prev.next = nxt
            nxt.prev = prev
            self.len -= 1

    def getNode(self, index: int) -> ListNode:
        if index == self.len:
            return self.right

        if index < self.len // 2:
            cur = self.left.next
            move = lambda x: x.next
        else:
            cur = self.right.prev
            move = lambda x: x.prev
            index = self.len - 1 - index

        while cur and index > 0:
            cur = move(cur)
            index -= 1

        if cur and index == 0:
            return cur

    def addNode(self, val: int, prev: ListNode, nxt: ListNode) -> None:
        node = ListNode(val)
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


# # Your MyLinkedList object will be instantiated and called as such:
# myLinkedList = LinkedList()
# print(myLinkedList)
# myLinkedList.addAtHead(1)
# print(myLinkedList)
# myLinkedList.addAtTail(3)
# print(myLinkedList)
# myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
# print(myLinkedList)
# myLinkedList.get(1)              # return 2
# print(myLinkedList)
# myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
# print(myLinkedList)
# myLinkedList.get(1)              # return 3
# print(myLinkedList)
#
# print(myLinkedList)
#
# print()
#
# ll2 = LinkedList()
# print(ll2)
# ll2.addAtHead(7)
# print(ll2)
# ll2.addAtHead(2)
# print(ll2)
# ll2.addAtHead(1)
# print(ll2)
# ll2.addAtIndex(3, 0)
# print(ll2)
# ll2.deleteAtIndex(2)
# print(ll2)
# ll2.addAtHead(6)
# print(ll2)
# ll2.addAtTail(4)
# print(ll2)
# print(ll2.get(4))
# ll2.addAtHead(4)
# print(ll2)
# ll2.addAtIndex(5, 0)
# print(ll2)
# ll2.addAtHead(6)
# print(ll2)


def run_test(commands: list[str], data: list[list[int]], res: list[int | None]):
    ll = LinkedList()
    for c, d, r in zip(commands[1:], data[1:], res[1:]):
        print(LinkedList.__dict__[c](ll, *d) == r, c, d, r, ll)


def test1():
    commands = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    data = [[], [1], [3], [1, 2], [1], [1], [1]]
    null = None
    res = [null, null, null, null, 2, null, 3]

    run_test(commands, data, res)


def test2():
    commands = ["MyLinkedList", "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex", "addAtHead",
                "addAtTail", "get", "addAtHead", "addAtIndex", "addAtHead"]
    data = [[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]
    null = None
    res = [null, null, null, null, null, null, null, null, 4, null, null, null]

    run_test(commands, data, res)


test1()
print()
test2()
