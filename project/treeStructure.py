import random
import  matplotlib.pyplot as plt
import regex
import nltk

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []
 
    def add_child(self, child_node):
        self.children.append(child_node)

    def is_terminal(self):
        return len(self.children) == 0
    
    def get_all_nodes(self):
        nodes = [self]
        for child in self.children:
            nodes.extend(child.get_all_nodes())
        return nodes
    
    def copy(self):
        new_copy = Node(self.value)
        new_copy.children = [child.copy() for child in self.children]
        return new_copy
    
    def depth(self):
        if self.is_terminal():
            return 1
        return 1 + max(child.depth() for child in self.children)
    
    def __str__(self):
        if self.is_terminal():
            return str(self.value)
        return f"{self.value} ({', '.join(str(child) for child in self.children)})"

