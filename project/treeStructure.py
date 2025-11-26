import random
import  matplotlib.pyplot as plt
import regex
import nltk

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def is_terminal(self):
        return len(self.children) == 0


n1 = Node("And so the story begins")
n2 = Node("Once upon a time")
n1.add_child(n2)
print (n1.value)
print (n1.children[0].value)

print (n1.is_terminal())
print (n2.is_terminal())