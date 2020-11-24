# Napište program koji izrađuje kopiju stabla. Stablo mora biti implementirano kao
# povezana struktura podataka (ne kao Pythonova lista).


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def insert(self, value):
        self.children.append(value)

    def print(self):
        self.print_tree(self, 0)

    def print_tree(self, node, indent):
        print("\t" * indent, node.value)
        for child in node.children:
            self.print_tree(child, indent + 1)

    def clone(self):
        return self.clone_tree(self)

    def clone_tree(self, node):
        if node is None:
            return None
        new_node = Node(node.value)
        for child in node.children:
            new_node.insert(self.clone_tree(child))
        return new_node


if __name__ == "__main__":
    root = Node(1)

    a = Node(2)
    a.insert(Node(5))
    a.insert(Node(6))
    a.insert(Node(7))

    b = Node(3)
    b.insert(Node(8))
    b.insert(Node(9))
    b.insert(Node(10))

    c = Node(4)
    c.insert(Node(11))
    c.insert(Node(12))
    c.insert(Node(13))

    root.insert(a)
    root.insert(b)
    root.insert(c)

    root_clone = root.clone()
    root_clone.print()
