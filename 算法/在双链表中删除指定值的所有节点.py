class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = ListNode(value)
        # 第一个节点
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        current = self.head
        # 添加到最后一个节点
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        self.tail = new_node

    def remove(self, value):
        if not self.head:
            return

        while self.head.value == value:
            self.head.next.prev = None
            self.head = self.head.next

        current = self.head
        while current.next:
            if current.next.value == value:
                if current.next.next == None:
                    self.tail = current
                else:
                    current.next.next.prev = current
                current.next = current.next.next
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print("None")

    def display_rev(self):
        current = self.tail
        while current:
            print(current.value, end=' -> ')
            current = current.prev
        print("None")


if __name__ == "__main__":
    # 示例用法：
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    print("原始链表：")
    linked_list.display()
    linked_list.display_rev()

    linked_list.remove(3)
    print("删除元素 3 后的链表：")
    linked_list.display()
    linked_list.display_rev()

    linked_list.remove(1)
    print("删除元素 1 后的链表：")
    linked_list.display()
    linked_list.display_rev()
