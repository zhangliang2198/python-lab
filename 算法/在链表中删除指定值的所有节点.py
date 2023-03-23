from typing import Any


class SingleNode:
    def __init__(self, data: int, next_node):
        self.data = data
        self.next_node = next_node


class DoubleNode:
    def __init__(self, data, pre_node, next_node):
        self.date = data
        self.next_node = next_node
        self.pre_node = pre_node


def make_node() -> SingleNode:
    # 创建一些node
    node5 = SingleNode(4, None)
    node4 = SingleNode(3, node5)
    node3 = SingleNode(2, node4)
    node2 = SingleNode(1, node3)
    node1 = SingleNode(0, node2)
    return node1


def delete_node(head_node: SingleNode, delete_node_s: SingleNode) -> SingleNode | None:
    if head_node.next_node is None:
        # 如果只有一个节点
        if head_node == delete_node_s:
            return None
        else:
            return head_node
    if head_node == delete_node_s:
        # 当要删除的节点等于头节点的时候，则返回第二个节点
        res = head_node.next_node
        # 删除第一个节点
        head_node.next_node = None
        del head_node
        return res
    # 开始正片
    o_head = head_node
    while head_node:
        org = head_node.next_node
        if delete_node_s == head_node.next_node:
            head_node.next_node = head_node.next_node.next_node
            org.next_node = None
            del org
        head_node = head_node.next_node
    return o_head


def delete_value(head_node: SingleNode, param: int) -> SingleNode | None:
    if head_node.next_node is None:
        if head_node.data == param:
            return None
        else:
            return head_node
    # 删除指定值的所有节点
    r_head = head_node
    pre = head_node
    curr = head_node.next_node
    while curr:
        if pre.data == param:
            r_head = curr
            pre = curr
            curr = curr.next_node
        else:
            if curr.data == param:
                pre.next_node = curr.next_node
                curr = curr.next_node
            else:
                pre = pre.next_node
                curr = curr.next_node
    return r_head


if __name__ == "__main__":
    # 创建一些node
    node1 = make_node()
    while node1:
        print(node1.data)
        node1 = node1.next_node

    node1 = make_node()
    head = delete_node(node1, node1.next_node)

    while head:
        print(head.data)
        head = head.next_node

    node1 = make_node()
    head_node = delete_value(node1, 4)
    while head_node:
        print(head_node.data)
        head_node = head_node.next_node
