import random


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def is_terminal(self):
        return len(self.children) == 0


n1 = Node("And so the story begins")

print (n1.value)
