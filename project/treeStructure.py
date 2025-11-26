import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def is_terminal(self):
        return len(self.children) == 0

    def __repr__(self):
        return f"Node({self.name})"


