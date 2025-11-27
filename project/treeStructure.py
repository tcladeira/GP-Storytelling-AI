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
    
    def __str__(self):
        if self.is_terminal():
            return str(self.value)
        return f"{self.value} ({', '.join(str(child) for child in self.children)})"


#test cases
tree1 = Node("root", [Node("B"), Node("C", [Node("D"), Node("E")])])
print(tree1) 

tree2 = tree1.get_all_nodes()
for node in tree2:
    print(node) 
print(tree2[0])