# -*- coding: utf-8 -*-

# Load necessary modules
import re

# Read input data
with open("day-7/input.txt", "r") as f:
    rules = f.read().split(".\n")

BAG_COLOR = "shiny gold"
CONTENT_PATTERN = "(\d)\s(\w+\s\w+)\sbag[\.s]?"


def clean_rule(rule, pattern=CONTENT_PATTERN):
    rule = rule.split(" bags contain ")
    content = [(int(amount), bag) for amount, bag in re.findall(pattern, rule[1])]
    rule = [rule[0]] + content
    return rule


rules = [clean_rule(rule) for rule in rules]


class Node:
    def __init__(self):
        self.parents = []
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)


class Graph:
    def __init__(self):
        self.data = {}

    def build_graph(self, relations):
        for relation in relations:
            # Check if parent bag node is already in graph
            if relation[0] not in self.data.keys():
                # Add parent node
                self.data[relation[0]] = Node()

            # Update children attribute
            for content in relation[1:]:
                self.data.get(relation[0]).add_child(content)
                # For each child, check if node is already in graph
                if content[1] not in self.data.keys():
                    # Add child node
                    self.data[content[1]] = Node()

                # Update parents attribute
                self.data.get(content[1]).add_parent(relation[0])

    def get_ancestors(self, node, ancestors=set()):
        if self.data.get(node).parents != []:
            for parent in self.data.get(node).parents:
                ancestors.add(parent)
                ancestors |= self.get_ancestors(parent, ancestors)
        return ancestors

    def get_number_of_bags(self, node):
        number_of_bags = 0
        for coeff, child in self.data.get(node).children:
            number_of_bags += coeff * (self.get_number_of_bags(child) + 1)
        return number_of_bags


# Part 1
graph = Graph()
graph.build_graph(rules)
print(f"Part 1: {len(graph.get_ancestors(BAG_COLOR))} different bags can contain at least one {BAG_COLOR} bag")

# Part 2
print(f"Part 2: total number of required bags is {graph.get_number_of_bags(BAG_COLOR)}")
