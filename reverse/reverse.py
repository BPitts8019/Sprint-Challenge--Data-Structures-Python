class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        output = "LinkedList: [ "
        cur_node = self.head
        while cur_node is not None:
            output += f"{cur_node.get_value()} -> "
            cur_node = cur_node.get_next()

        return output + "None ]"

    def __str__(self):
        output = ""
        cur_node = self.head
        while cur_node is not None:
            output += f"{cur_node.get_value()}"
            output += f" -> " if cur_node.get_next() is not None else ""
            cur_node = cur_node.get_next()

        return output

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            return

        if node.next_node:
            self.reverse_list(node.next_node, node)
        else:
            self.head = node

        node.next_node = prev


some_list = LinkedList()
some_list.add_to_head(3)
some_list.add_to_head(2)
some_list.add_to_head(1)
print(some_list)
some_list.reverse_list(some_list.head, None)
print(some_list)
