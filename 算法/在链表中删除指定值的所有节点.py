class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, value):
        if not self.head:
            return

        while self.head.value == value:
            self.head = self.head.next

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
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

    linked_list.remove(3)
    print("删除元素 3 后的链表：")
    linked_list.display()

    linked_list.remove(1)
    print("删除元素 1 后的链表：")
    linked_list.display()
