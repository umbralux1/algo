from LeetCodeTest import set_null, LeetCodeTest


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.len = 0

    def get(self, index: int) -> int:
        node = self.getNode(index)
        if node and node is not self.right and node is not self.left:
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.addNode(val, self.left, self.left.next)
        self.len += 1

    def addAtTail(self, val: int) -> None:
        self.addNode(val, self.right.prev, self.right)
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.getNode(index)
        if node:
            self.addNode(val, node.prev, node)
            self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        node = self.getNode(index)
        if node and node is not self.right and node is not self.left:
            prev, nxt = node.prev, node.next
            prev.next = nxt
            nxt.prev = prev
            self.len -= 1

    def addNode(self, val: int, prev: ListNode, nxt: ListNode) -> None:
        node = ListNode(val)
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def getNode(self, index: int) -> ListNode | None:
        if (self.len // 2) <= index:
            cur = self.left.next
            move = lambda x: x.next
        else:
            cur = self.right.prev
            index = self.len - 1 - index
            move = lambda x: x.prev

        while cur and index > 0:
            cur = move(cur)
            index -= 1

        if index == 0:
            return cur


set_null(globals())


def test1():
# Input
    commands = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    data = [[], [1], [3], [1, 2], [1], [1], [1]]
    # Output
    expected = [null, null, null, null, 2, null, 3]

    lct = LeetCodeTest(MyLinkedList, commands, data, expected)
    lct.set_str_for_linked_list()
    lct.run_test()


def test2():
    commands = ["MyLinkedList", "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex", "addAtHead", "addAtTail",
     "get", "addAtHead", "addAtIndex", "addAtHead"]

    data = [[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]

    expected = [null, null, null, null, null, null, null, null, 4, null, null, null]

    lct = LeetCodeTest(MyLinkedList, commands, data, expected)
    lct.set_str_for_linked_list()
    lct.run_test()


def test3():
    commands = ["MyLinkedList", "addAtHead", "get", "addAtHead", "addAtHead", "deleteAtIndex", "addAtHead", "get", "get", "get",
     "addAtHead", "deleteAtIndex"]

    data = [[], [4], [1], [1], [5], [3], [7], [3], [3], [3], [1], [4]]

    expected = [null, null, -1, null, null, null, null, 4, 4, 4, null, null]

    lct = LeetCodeTest(MyLinkedList, commands, data, expected)
    lct.set_str_for_linked_list()
    lct.run_test()


test1()
test2()
test3()

