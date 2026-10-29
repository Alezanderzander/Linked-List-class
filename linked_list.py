from node import Node
class linked_list:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            old_last = self.last
            new_node.before = old_last
            old_last.after = new_node
            self.last = new_node
        self.size += 1

    def get_node(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        if index > self.size // 2:
            current = self.last
            for i in range(self.size -1 - index):
                current = current.before
        else:
            current = self.first
            for i in range(index):
                current = current.after

        return current

    def get(self, index):
        return self.get_node(index).value

    def insert_after(self, value, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")

        previous_node = self.get_node(index)
        next_node = previous_node.after

        new_node = Node(value)

        new_node.before = previous_node
        new_node.after = next_node

        previous_node.after = new_node
        if next_node is not None:
            next_node.before = new_node
        else:
            self.last = new_node
        self.size += 1

